# CS50_Projects
Projects from the Harvard CS50 online course. Programmed in C, Python, SQL, HTML/CSS, and JavaScript.

# Project Summary
## Week 1: C
### Population Growth

A program which calculates the number of years required for a llama population to grow. The user is prompted for a starting population size which is required to be greater than or equal to 9. Additionally, the user is prompted for an final population size which is either greater than or equal to the starting population size. As a result the program will calculate and print the number of years the llama population is expected to grow. 
#### Example Output:
```
$ ./population
Start size: 100
End size: 200
Years: 9
```
#### Associated Files:
* [population.c](https://github.com/alex-gillard/CS50_Projects/blob/main/population.c)

### Hello
Introductory print syntax in the C Programming Language.
#### Associated Files:
* [hello.c](https://github.com/alex-gillard/CS50_Projects/blob/main/hello.c)

### Mario
Using hashes '#' and gaps ' ', right-aligned block pyramids are created based on the objects seen from Super Mario Brothers. The user is expected to input a height value between the integers 1 and 8, inclusive. As a result, the pyramid is printed based on the height value.

![Right-aligned block pyramid from Super Mario Brothers](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)
#### Example Output:
```
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```
#### Associated Files:
* [mario.c](https://github.com/alex-gillard/CS50_Projects/blob/main/mario.c)

### Cash
In the program cash.c, the user is prompted to enter the number of cents a customer is owed, and the program then displays the minimum coins required for the change. The main function is already provided, but several sub-functions required completion. Specifically, the get_cents function should prompt the user for an amount in cents, ensuring it's not negative. The functions calculate_quarters, calculate_dimes, calculate_nickels, and calculate_pennies are tasked with determining the number of respective coins needed for a given cent value. Each function should handle any cent value, and only the provided TODOs and return values should be replaced without altering other distribution code.
#### Example Output:
#### Associated Files:
```
$ ./cash
Change owed: -41
Change owed: foo
Change owed: 41
4
```
* [cash.c](https://github.com/alex-gillard/CS50_Projects/blob/main/cash.c)

## Week 2: Arrays
### Scrabble

In the program scrabble.c, players enter a word each, and the one with the higher score wins. The scores for individual letters are stored in the POINTS array. A helper function, compute_score(), calculates the word's total score using the POINTS array, treating non-letter characters as zero points and considering both upper and lowercase letters equally. The main function then compares the scores and announces the winner or declares a tie, without checking for dictionary-validity of words.
#### Example Output:
```
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```
#### Associated Files
[scrabble.c](https://github.com/alex-gillard/CS50_Projects/blob/main/scrabble.c)

### Readability
In the readability.c program, the Coleman-Liau index is calculated for a given text to predict the U.S. grade level needed to understand it. The program should prompt the user for a text, count its letters, words, and sentences, and then use these counts to compute the index. The result should be displayed as a grade level, rounding as necessary, with special outputs for grades below 1 or above 16.
#### Example Output:
```
$ ./readability
Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an twelfth-grade reading level.
Grade 12
```
#### Associated Files:
* [readability.c](https://github.com/alex-gillard/CS50_Projects/blob/main/readability.c)

### Bulbs

kes a user-inputted message and encodes it using light bulbs to represent binary numbers. Each character in the message is converted into its ASCII decimal value, which is then represented as an 8-bit binary number. These binary numbers are displayed using emojis, with one emoji for 'on' (🟡) and another for 'off' (⚫). Each set of 8 emojis (representing one byte) is printed on a new line. The program is implemented in a file named bulbs.c.
#### Example Output:
```
# ./bulbs
Message: HI MOM
⚫🟡⚫⚫🟡⚫⚫⚫
⚫🟡⚫⚫🟡⚫⚫🟡
⚫⚫🟡⚫⚫⚫⚫⚫
⚫🟡⚫⚫🟡🟡⚫🟡
⚫🟡⚫⚫🟡🟡🟡🟡
⚫🟡⚫⚫🟡🟡⚫🟡
```
#### Associated Files:
* [bulbs.c](https://github.com/alex-gillard/CS50_Projects/blob/main/bulbs.c)
