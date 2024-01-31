import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Library used to obtain current date
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Index Function
# TODO: Show in table:
# User logged in
# Which stock user owns
# Number of shares owned
# Current price of stock
# Total value of each holding (shares * price)
# User cash balance
# Grand total (Stock value + cash)
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        purch_data = db.execute(
            "SELECT * FROM purchases WHERE user_id = ?", session["user_id"]
        )
        hist_data = db.execute(
            "SELECT * FROM history WHERE user_id = ?", session["user_id"]
        )
        user_data = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        return render_template(
            "index.html",
            user_data=user_data,
            hist_data=hist_data,
            purch_data=purch_data,
        )
    return apology("Error: Failed to load page")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        # Stock symbol inputted by user
        symb = request.form.get("symbol")
        stock_symb = lookup(symb)
        # Boolean flags switch to true when positive conditions are met (Stock symbol exists and share number is non-negative)
        stock_flag = False
        share_flag = False
        # Checks if stock symbol is either blank or does not exist
        if stock_symb is None or not stock_symb["symbol"]:
            return apology("Invalid stock symbol")
        else:
            stock_flag = True
        # Number of shares inputted by user
        shares = int(request.form.get("shares"))
        # Checks if shares is a non-negative number
        try:
            shares_float = float(shares)
        except ValueError:
            return apology("Number of shares must be a non-negative number", 400)
        if not shares_float or shares_float <= 0:
            return apology("Number of shares must be a non-negative number", 400)
        else:
            share_flag = True
        # Checking if positive conditions are met
        if stock_flag and share_flag is True:
            buy_time = datetime.now()
            # Obtain current cash balance
            cash_rows = db.execute(
                "SELECT cash FROM users WHERE id = ?", session["user_id"]
            )
            cash = cash_rows[0]["cash"]
            # Calculate price of purchase
            price = shares * stock_symb["price"]
            # Check if user has enough cash
            if cash < price:
                return apology("Insufficient cash available")
            else:
                # Update cash balance
                db.execute(
                    "UPDATE users SET cash = cash - ? WHERE id = ?",
                    price,
                    session["user_id"],
                )
                # Record purchase data into purchases
                buy = db.execute(
                    "INSERT INTO purchases (user_id, stock, price, buy_time, num_shares) VALUES (?, ?, ?, ?, ?)",
                    session["user_id"],
                    stock_symb["symbol"],
                    price,
                    buy_time,
                    shares,
                )
                # Record purchase data into history
                db.execute(
                    "INSERT INTO history (user_id, stock, trans_type, num_shares, trans_time, price) VALUES (?, ?, 'BUY', ?, ?, ?)",
                    session["user_id"],
                    stock_symb["symbol"],
                    shares,
                    buy_time,
                    price,
                )
            return redirect("/")

        return render_template("buy.html", stock_symb=stock_symb, buy=buy)

    return apology("Error: Failed to load page")


# History Function
# Fields to display:
# Transaction type (Buy, Sell)
# How many shares were bought or sold
# When transaction took place
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        hist_data = db.execute(
            "SELECT * FROM history WHERE user_id = ?", session["user_id"]
        )
        return render_template("history.html", hist_data=hist_data)
    return apology("Error: could not load page")


# Fully implemented for you
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# Fully implemented for you
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Quote Function
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        ticker = request.form.get("symbol")
        # Call the lookup function for a given stock symbol entered by a user
        stock_quote = lookup(ticker)
        # Check if text field is empty
        if stock_quote is None:
            return apology("Invalid stock symbol", 400)
        # Specify the name, symbol, and price from the lookup function
        name = stock_quote["name"]
        symbol = stock_quote["symbol"]
        price = stock_quote["price"]
        return render_template("quoted.html", stock_quote=stock_quote)
    return apology("Error: could not load page", 400)


# Register Function
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Load register.html
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        user_name = request.form.get("username")
        pw_name = request.form.get("password")
        conf_name = request.form.get("confirmation")

        # Ensure username, password, and confirmation are filled in
        if not user_name or not pw_name or not conf_name:
            return apology("Please enter username, password, and confirmation", 400)
        if user_name and (not pw_name or not conf_name):
            return apology("Please enter password and confirmation", 400)
        if user_name and pw_name and not conf_name:
            return apology("Please enter password confirmation", 400)
        # Check if password matches confirmation
        if pw_name != conf_name:
            return apology("Password and Confirmation do not match", 400)

        # Check if username is in database
        user_row = db.execute("SELECT * FROM users WHERE username = ?", user_name)
        user_flag = False
        # Checking username
        if not user_row:
            user_flag = True
        else:
            return apology("Error: Username already exists", 400)
        if user_flag == True:
            # Add username and password to users database
            pw_hash = generate_password_hash(pw_name)
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", user_name, pw_hash
            )
            return redirect("/")
    else:
        return apology("Error: Could not load page", 400)


# Sell Function
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        stock_data = db.execute(
            "SELECT stock FROM purchases WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", stock_data=stock_data)
    if request.method == "POST":
        # Validate user input
        symb = request.form.get("symbol")
        if not symb:
            return apology("Stock not found. Select stock to sell", 400)
        shares = request.form.get("shares")
        # Check if shares is not entered, shares is not a digit, or shares is not a positive integer
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid number of shares", 400)
        # Setting up variables for DB queries
        Lookup = lookup(symb)
        priceLookup = Lookup["price"]

        if Lookup:
            sell_price = priceLookup * int(shares)
            # Update purchases table with sale
            db.execute(
                "UPDATE purchases SET price = price - ?, num_shares = num_shares - ? WHERE user_id = ? AND stock = ?",
                sell_price,
                shares,
                session["user_id"],
                symb,
            )
            # Update users table with sale
            db.execute(
                "UPDATE users SET cash = cash + ? WHERE id = ?",
                sell_price,
                session["user_id"],
            )
            # Update history table with sale
            sell_time = datetime.now()
            db.execute(
                "INSERT INTO history (user_id, stock, trans_type, num_shares, trans_time, price) VALUES (?, ?, 'SELL', ?, ?, ?)",
                session["user_id"],
                symb,
                shares,
                sell_time,
                sell_price,
            )
            # PERSONAL TOUCH: "House-Cleaning" the data within the "purchases" table so rows are removed when price and num_share fields are equal to zero. This will also automatically remove the stock from the drop-down options within Sell.
            # Fetch the current price and current number of shares after a sell event happens
            price_data = db.execute(
                "SELECT price FROM purchases WHERE user_id = ?", session["user_id"]
            )
            shares_data = db.execute(
                "SELECT num_shares FROM purchases WHERE user_id = ?", session["user_id"]
            )
            # Fetch number of rows from price and shares data
            num_rows = len(price_data)
            for i in range(num_rows):
                if price_data[i]["price"] == 0 or shares_data[i]["num_shares"] == 0:
                    db.execute(
                        "DELETE FROM purchases WHERE price = 0 AND num_shares = 0"
                    )

            return redirect("/")
        return render_template("sell.html")

    return apology("Error: could not load page")
