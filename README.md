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

In this program user-inputted messages are encoded using light bulbs to represent binary numbers. Each character in the message is converted into its ASCII decimal value, which is then represented as an 8-bit binary number. These binary numbers are displayed using emojis, with one emoji for 'on' (🟡) and another for 'off' (⚫). Each set of 8 emojis (representing one byte) is printed on a new line. The program is implemented in a file named bulbs.c.
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

## Week 3: Algorithms
### Sort

In this CS50 assignment, three pre-compiled C programs were analyzed, each implementing a different sorting algorithm: selection sort, bubble sort, or merge sort. The task involved identifying which algorithm each program used by testing them on various .txt files containing reversed, shuffled, or sorted number sequences. The programs were executed on the command line with performance time measurement to facilitate comparison. Findings and analytical reasoning were meticulously recorded in an answers.txt file. An Excel spreadsheet, "Sorting Algorithm Speeds" was added to visualize the sorting algorithm speeds for effective comparison.

#### Associated Files:

* [answers.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/answers.txt)
* [Sorting Algorithm Speeds.xlsx](https://github.com/alex-gillard/CS50_Projects/blob/main/Sorting%20Algorithm%20Speeds.xlsx)
* [random10000.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/random10000.txt)
* [random5000.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/random5000.txt)
* [random50000.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/random50000.txt)
* [sorted10000.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/sorted10000.txt)
* [sorted5000.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/sorted5000.txt)
* [sorted50000.txt ](https://github.com/alex-gillard/CS50_Projects/blob/main/sorted50000.txt)

### Plurality

In this CS50 assignment, plurality.c was implemented to simulate a plurality vote election system. This simplest form of election allows each voter to choose one candidate, with the candidate receiving the most votes declared the winner. The assignment involved completing two functions in the code: vote, which updates the vote total for a candidate if the vote is valid, and print_winner, which prints the name(s) of the candidate(s) with the most votes. The program structure included defining a maximum number of candidates, structuring candidate data, and processing user input for the number of voters and votes. This exercise was a practical application of arrays, structures, and control flow in C programming.

#### Example Output
```
$ ./plurality Alice Bob Charlie
Number of voters: 4
Vote: Alice
Vote: Bob
Vote: Charlie
Vote: Alice
Alice
```

#### Associated Files
[plurality.c](https://github.com/alex-gillard/CS50_Projects/blob/main/plurality.c)

### Runoff

In this CS50 assignment, the task was to implement a program simulating a runoff election using ranked-choice voting. Unlike plurality voting, this system allows voters to rank candidates in order of preference. The program, runoff.c, involves several key functions: vote, to record each voter's ranked preferences; tabulate, to count votes for non-eliminated candidates; print_winner, to declare a winner if someone has more than half the votes; find_min, to find the minimum number of votes any candidate currently holds; is_tie, to check if there's a tie; and eliminate, to remove the candidate(s) with the least votes. The program iterates through these steps, eliminating the least popular candidates and redistributing votes, until a candidate achieves a majority. This assignment not only involved understanding the runoff voting process but also required careful handling of arrays, structures, and control logic in C programming.

#### Example Output
```
./runoff Alice Bob Charlie
Number of voters: 5
Rank 1: Alice
Rank 2: Bob
Rank 3: Charlie

Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob

Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice

Rank 1: Bob
Rank 2: Alice
Rank 3: Charlie

Rank 1: Charlie
Rank 2: Alice
Rank 3: Bob

Alice
```

#### Associated Files

* [runoff.c](https://github.com/alex-gillard/CS50_Projects/blob/main/runoff.c)

## Week 4: Memory
### Volume

In this CS50 assignment, a program named volume.c was developed to modify the volume of an audio file in WAV format. The program accepts three command-line arguments: the name of the original audio file, the name for the new audio file, and a scaling factor for the volume. WAV files consist of a 44-byte header and audio samples, each being a 2-byte (16-bit) integer. The program's key function is to read and write this header unchanged to the output file, then process each audio sample. Samples are multiplied by the given scaling factor to adjust the volume, for instance, doubling if the factor is 2.0 or halving if it's 0.5. The modified samples are written to the output file. This assignment emphasizes file I/O operations in C, binary data handling, and understanding of data types and memory management.

#### Example Output
```
$ ./volume INPUT.wav OUTPUT.wav 2.0
```
Note that .wav files are generated from this program

#### Associated Files
* [volume.c](https://github.com/alex-gillard/CS50_Projects)

### Filter

In this CS50 assignment, a program called filter.c was implemented to apply filters to bitmap images (BMP files). The program uses different filters: grayscale, sepia, reflection, and blur. Grayscale converts the image into black and white, sepia gives it a reddish-brown tone, reflection mirrors the image horizontally, and blur applies a box blur effect. Each filter is applied by manipulating the RGB values of each pixel in the image. The task involved reading BMP headers, processing the pixel array, and applying the desired transformations. This exercise focused on understanding bitmap file structures, working with arrays and nested loops, and applying algorithms to manipulate pixel data in C.

#### Example Input
```
$ ./filter -r IMAGE.bmp REFLECTED.bmp
```

#### Input Images

![stadium.bmp](https://github.com/alex-gillard/CS50_Projects/assets/77037153/31d90d5b-53a8-4c29-8750-5e5ab02f77e8)
![tower.bmp](https://github.com/alex-gillard/CS50_Projects/assets/77037153/b5dc5b88-f382-4681-9940-96651328ac04)
![courtyard.bmp](https://github.com/alex-gillard/CS50_Projects/assets/77037153/968ef1ec-6128-4e61-a3bd-bfedf0c5cd2a)
![yard.bmp](https://github.com/alex-gillard/CS50_Projects/assets/77037153/0e2ed7c1-e199-4de9-8b61-90d7d573fe62)


#### Output Images

![stadium output](https://github.com/alex-gillard/CS50_Projects/assets/77037153/d4e49afc-4f4f-41d2-b2ee-d0b14ab2e2da)
![tower output](https://github.com/alex-gillard/CS50_Projects/assets/77037153/7180e845-7ab5-426c-9c11-cd39e52931fd)
![courtyard output](https://github.com/alex-gillard/CS50_Projects/assets/77037153/98fcfba2-7815-4212-9a80-550f61612acf)
![yard output](https://github.com/alex-gillard/CS50_Projects/assets/77037153/5366a210-b641-4212-b8f9-f69ebbb97ee8)

#### Associated Files
* [filter.c](https://github.com/alex-gillard/CS50_Projects/blob/main/filter.c)
* [Makefile.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/Makefile.txt)
* [helpers.c](https://github.com/alex-gillard/CS50_Projects/blob/main/helpers.c)
* [helpers.h](https://github.com/alex-gillard/CS50_Projects/blob/main/helpers.h)
* [bmp.h](https://github.com/alex-gillard/CS50_Projects/blob/main/bmp.h)

### Reverse

In this CS50 assignment, a program named reverse.c was created to reverse audio in WAV files, a technique known as "backmasking." Unlike compressed formats like MP3, WAV files are easier to manipulate due to their straightforward structure, which includes a 44-byte header followed by audio data. The assignment involved writing a program that takes an input WAV file and produces a reversed output WAV file.

The process began with ensuring the program accepts two command-line arguments: the names of the input and output WAV files. The next steps included opening the input file in read-only mode, reading its header, and validating that the file is in WAV format using a provided WAVHEADER struct. After confirming the file format, the output file was opened for writing.

The key part of the assignment was reversing the audio. This required calculating the block size of the WAV file (the unit of auditory data) and iterating through the audio data from the end of the input file, simultaneously writing each block to the output file in reverse order. The challenge lay in maintaining the order of channels for each audio block while reversing their sequence. Finally, the program closed all opened files. This exercise honed skills in file I/O, data manipulation, and working with audio data in C.

#### Example Output
```
$ ./reverse input.wav
Usage: ./reverse input.wav output.wav
```
Note that this program outputs .wav files

#### Associated Files
* [wav.h](https://github.com/alex-gillard/CS50_Projects/blob/main/wav.h)
* [reverse.c](https://github.com/alex-gillard/CS50_Projects/blob/main/reverse.c)

## Week 5: Data Structures
### Inheritance

In this CS50 assignment, a program named inheritance.c was developed to simulate the inheritance of blood types across three generations of a family. The simulation models how alleles (A, B, O) are passed from parents to children, determining each person's blood type through a combination of inherited alleles.

The program starts by creating a family tree using dynamic memory allocation for each family member, including the person, their parents, and grandparents. For the oldest generation, alleles are assigned randomly. For subsequent generations, each person inherits one random allele from each parent. This inheritance is achieved through recursive calls to the create_family function, which constructs the family tree by allocating memory for each person, assigning parents and alleles appropriately, and ensuring the oldest generation has no parents (indicated by NULL pointers) and randomly assigned alleles.

After constructing the family tree, the program prints out the blood type of each family member, demonstrating the inherited blood types across generations. Finally, the program frees the allocated memory for each person in the family tree using the free_family function. This function recursively frees memory for all ancestors of a given person, ensuring no memory leaks occur. This assignment emphasizes the concepts of dynamic memory allocation, recursion, and pointers in C programming, illustrating how data structures can be used to model complex relationships and processes.

#### Example Output
```
$ ./inheritance
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```

#### Associated Files
* [inheritance.c](https://github.com/alex-gillard/CS50_Projects/blob/main/inheritance.c)

### Speller

In this CS50 assignment, the challenge was to implement a spell-checking program using a hash table to efficiently manage dictionary operations. The program, speller, reads a dictionary of words from disk into memory and then checks a text file for misspellings, identifying words not found in the dictionary.

The implementation required completing several key functions in dictionary.c: load, to read the dictionary and store it in a hash table; hash, to convert words into numerical indices for the hash table; size, to return the total number of words in the dictionary; check, to determine if a word is spelled correctly according to the dictionary; and unload, to free memory used by the hash table. A suitable hash function had to be devised to minimize collisions and distribute words evenly across the hash table.

Efficiency was paramount, as the program's performance was measured in terms of the time taken to load the dictionary, check words, determine the dictionary's size, and unload the dictionary from memory. The program was designed to be case-insensitive and handle variations in capitalization without compromising the speed or accuracy of the spell check.

This assignment emphasized the importance of data structure choice—in this case, a hash table—for optimizing the performance of real-world applications like spell-checking. It challenged students to consider both time complexity and memory usage, requiring careful planning and optimization to balance the two. The end goal was to create a spell checker that was not only functionally correct but also as fast and memory-efficient as possible.

#### Example Output
```
$ ./speller texts/lalaland.txt
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
```

#### Associated Files
* [dictionary.c](https://github.com/alex-gillard/CS50_Projects/blob/main/dictionary.c)
* [dictionary.h](https://github.com/alex-gillard/CS50_Projects/blob/main/dictionary.h)
* [large.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/large.txt)
* [small.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/small.txt)
* [speller.c](https://github.com/alex-gillard/CS50_Projects/blob/main/speller.c)
* [Makefile.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/Makefile.txt)

## Week 6: Python
### World Cup

In the CS50 World Cup simulation project, a program was written to simulate FIFA World Cup tournaments and calculate each team's probability of winning based on FIFA ratings. The process involved reading team data from a CSV file, where each team was represented as a dictionary containing its name and rating. The program, tournament.py, utilized command-line arguments to select the appropriate team CSV file for the men's or women's World Cup data.

The core of the simulation involved implementing the simulate_tournament function, which simulated the knockout rounds by repeatedly calling the simulate_round function until a single winning team remained. This tournament simulation was run multiple times (defaulted to 1000 simulations) to aggregate the win counts for each team.

The main function managed the simulation process, reading the team data into memory, executing the tournament simulations, and keeping track of wins in a counts dictionary to calculate each team's winning probability. The results were sorted and printed, showing the estimated chances of each team winning the World Cup, demonstrating a practical application of Python for data processing and simulation in a sports context.

#### Example Output
```
$ python tournament.py 2018m.csv
Belgium: 20.9% chance of winning
Brazil: 20.3% chance of winning
Portugal: 14.5% chance of winning
Spain: 13.6% chance of winning
Switzerland: 10.5% chance of winning
Argentina: 6.5% chance of winning
England: 3.7% chance of winning
France: 3.3% chance of winning
Denmark: 2.2% chance of winning
Croatia: 2.0% chance of winning
Colombia: 1.8% chance of winning
Sweden: 0.5% chance of winning
Uruguay: 0.1% chance of winning
Mexico: 0.1% chance of winning
```

#### Associated Files
* [tournament.py](https://github.com/alex-gillard/CS50_Projects/blob/main/tournament.py)
* [2018m.csv](https://github.com/alex-gillard/CS50_Projects/blob/main/2018m.csv) 2018 Men's FIFA Ratings
* [2019w.csv](https://github.com/alex-gillard/CS50_Projects/blob/main/2019w.csv) 2019 Women's FIFA Ratings

### Mario

In the Python version of the CS50 Mario assignment, a program was developed to print a half-pyramid of a specified height, mimicking the structure found in the classic Mario game. The program, mario.py, prompts the user to input a height value between 1 and 8, inclusive. Upon receiving a valid input, it generates the half-pyramid using hash symbols (#) for blocks, aligning the pyramid's bottom-left corner with the left-hand edge of the terminal window.

The implementation required careful use of loops and conditionals to ensure the program re-prompts the user for input upon receiving invalid data, such as negative numbers, numbers greater than 8, non-integer values, or no input at all. The focus was on leveraging Python's control structures to validate user input and dynamically generate the pyramid's structure based on the specified height, demonstrating fundamental programming concepts in Python.
  
#### Example Output
```
$ python mario.py
Height: 4
   #
  ##
 ###
####
```

#### Associated Files
* [mario.py](https://github.com/alex-gillard/CS50_Projects/blob/main/mario.py)

### Cash

In the Python version of the CS50 Cash assignment, a program was developed to calculate the minimum number of coins required to make change for a given amount of money. The program, cash.py, prompts the user for an amount of change owed, expressed in dollars, and calculates the smallest number of quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢) needed to make that change.

Utilizing the get_float function from the CS50 Library to handle user input, the program ensures the amount entered is non-negative and repeatedly prompts for a valid input if necessary. Upon receiving a valid amount, it efficiently computes the coin count by sequentially subtracting the largest coin values possible and incrementing a coin counter until the remaining change owed is zero.

The implementation showcases fundamental programming concepts in Python, such as loops and conditionals, while also emphasizing precision in handling floating-point arithmetic to deal with money values accurately. The output is the minimum number of coins required, displayed as a single integer followed by a newline, aligning with the specifications for automated correctness testing.

#### Example Output
```
$ python cash.py
Change owed: 0.41
4
```

#### Associated Files
* [cash.py](https://github.com/alex-gillard/CS50_Projects/blob/main/cash.py)

### Readability

In the Python adaptation of the CS50 Readability assignment, a program named readability.py was crafted to compute the grade level necessary to understand a given piece of text, employing the Coleman-Liau index formula. The program prompts the user for a block of text and outputs the corresponding grade level needed for comprehension. This task involves calculating the number of letters, words, and sentences within the input text to determine its complexity.

The program utilizes Python's string manipulation capabilities to accurately count characters that qualify as letters and delimiters that signify the end of sentences, such as periods, exclamation points, or question marks. It carefully calculates the average number of letters per 100 words and the average number of sentences per 100 words, feeding these averages into the Coleman-Liau formula to derive a grade level, which is then rounded to the nearest whole number for output.

Special conditions are handled gracefully: if the computed grade level is 16 or above, indicating a reading level at or above that of a senior in high school, the program outputs "Grade 16+." Conversely, for texts assessed to be below a first-grade reading level, it outputs "Before Grade 1." This project not only demonstrates proficiency in Python programming but also showcases the practical application of computational thinking in evaluating and interpreting textual data.

#### Example Output
```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

#### Associated Files
* [readability.py](https://github.com/alex-gillard/CS50_Projects/blob/main/readability.py)

### DNA

In the Python-based CS50 DNA project, a program named dna.py was created to identify individuals based on their DNA. The program takes two command-line arguments: a CSV file with STR (Short Tandem Repeat) counts for a list of individuals and a text file containing the DNA sequence to be identified. It reads the STR sequences and their counts from the CSV file into memory and then analyzes the provided DNA sequence to compute the longest run of consecutive repeats for each STR listed in the CSV file's header.

The analysis involves leveraging a helper function, longest_match, which calculates the maximum number of times an STR repeats in the DNA sequence. The program compares these calculated STR counts against those in the CSV file to find a match. If the STR counts align exactly with one of the individuals in the database, the program prints the individual's name. If there is no exact match, it outputs "No match."

This project underscores the application of computational techniques to biological data, requiring proficiency in file I/O operations, string manipulation, and data structure management in Python. It encapsulates how programming can intersect with genetics and forensic science, providing a practical tool for DNA profiling.

#### Example Output
```
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

#### Associated Files (Sequence Files excluded for brevity)
* [dna.py](https://github.com/alex-gillard/CS50_Projects/blob/main/dna.py)
* [large.csv](https://github.com/alex-gillard/CS50_Projects/blob/main/large.csv)
* [small.csv](https://github.com/alex-gillard/CS50_Projects/blob/main/small.csv)

## Week 7: SQL
### Songs

In the Songs project, SQL queries were formulated to extract specific insights from a database containing Spotify's top streamed songs in 2018. The database, songs.db, includes details about songs and artists, such as danceability, energy, tempo, and duration. Participants were tasked with writing SQL queries to perform a range of analyses, from listing all songs in the database to calculating the average energy of tracks by a particular artist like Drake.

Each query required careful consideration of the database schema, which was explored using the .schema command in SQLite. Queries varied in complexity, including sorting songs by tempo, identifying the longest songs, filtering songs with high danceability, energy, and valence, and averaging the energy of all songs or those by specific artists. Additionally, one query focused on songs featuring other artists, indicated by “feat.” in the song title.

This project demonstrated practical applications of SQL for data analysis, requiring a nuanced understanding of SQL syntax and functions to extract meaningful information from a relational database. It highlighted the use of SQL in real-world scenarios, such as generating tailored music recommendations or summarizing streaming trends.

#### Associated Files
* [1.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/1.sql)
* [2.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/2.sql)
* [3.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/3.sql)
* [4.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/4.sql)
* [5.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/5.sql)
* [6.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/6.sql)
* [7.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/7.sql)
* [8.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/8.sql)
* [songs.db](https://github.com/alex-gillard/CS50_Projects/blob/main/songs.db)

### Fiftyville

In the Fiftyville mystery project, participants utilized SQL queries to unravel a fictional crime involving the theft of the CS50 duck in the town of Fiftyville. The premise was that the theft occurred on July 28, 2021, on Humphrey Street, and the thief, along with an accomplice, fled the town shortly after. The challenge was to deduce the thief's identity, the city to which they escaped, and the identity of the accomplice using only the data provided in the fiftyville.db SQLite database.

The database contained various tables with data from around the time of the theft, including crime scene reports, people's personal details, flight records, and more. Participants needed to craft SQL queries to extract and correlate information across these tables strategically. The process involved analyzing crime scene reports to match the date and location of the theft, examining flight records to identify potential suspects leaving town around the time of the crime, and piecing together evidence to pinpoint the thief and their accomplice.

To document their investigative process, participants maintained a log of their SQL queries in log.sql, annotating each query with comments to explain its purpose and the information it sought to uncover. This log served as a record of the analytical steps taken to solve the mystery, highlighting the application of SQL in data-driven problem-solving and investigative scenarios.

The Fiftyville project showcased the power of SQL for data analysis and the importance of logical reasoning in solving complex problems. It provided a practical exercise in applying SQL queries to sift through and make sense of large datasets, embodying the intersection of programming skills and deductive reasoning in forensic analysis.

#### Associated Files
* [fiftyville.db](https://github.com/alex-gillard/CS50_Projects/blob/main/fiftyville.db)
* [log.sql](https://github.com/alex-gillard/CS50_Projects/blob/main/log.sql)
* [answers.txt](https://github.com/alex-gillard/CS50_Projects/blob/main/answers.txt)

## Week 8: HTML, CSS, JavaScript
### Trivia

In the Trivia project, participants were tasked with creating an interactive webpage that allows users to answer trivia questions using HTML, CSS, and JavaScript. The webpage features two types of trivia questions: multiple-choice and text-based free response. Each question is designed with user interaction in mind, providing immediate feedback on the correctness of the user's answer.

For the multiple-choice section, an HTML structure including an h3 heading for the question and buttons for each answer choice was required. JavaScript logic was implemented to change the color of the buttons upon user interaction—turning red for incorrect answers and green for correct ones, with corresponding text feedback displayed below the question.

The text-based free response section similarly used an h3 heading for the question, an input field for user responses, and a confirmation button. JavaScript was used to validate the user's input against the correct answer, altering the input field's color and displaying feedback text accordingly.

Participants had the option to enhance the webpage's aesthetics and user experience by modifying the styles.css file, as well as adding more trivia questions to enrich the quiz content. This project demonstrated a practical application of web development skills, highlighting the dynamic capabilities of JavaScript to create engaging, interactive content on webpages.

#### Associated Files
* [trivia_index.html](https://github.com/alex-gillard/CS50_Projects/blob/main/trivia_index.html)
* [trivia_styles.css](https://github.com/alex-gillard/CS50_Projects/blob/main/trivia_styles.css)

### Homepage

The Homepage project involved developing a simple yet interactive homepage using HTML, CSS, and JavaScript. This project aimed to construct a personal or hobby-related website, which introduces the creator or a subject of interest through the foundational languages of web development. The design specifications required the website to contain at least four different .html pages, including index.html as the main page, ensuring navigability between pages through hyperlinks. The project emphasized the use of at least ten distinct HTML tags beyond the basic structural ones to enrich the webpage's content and layout. Incorporating Bootstrap, a popular CSS framework, was mandated to enhance the website's aesthetics and responsiveness. This involved integrating Bootstrap's CSS and JavaScript libraries, utilizing its ready-made components and grid system for a professional and polished appearance.

Moreover, the creation of a custom stylesheet (styles.css) was specified, where at least five different CSS selectors and properties were to be applied, showcasing the ability to creatively and effectively style web elements. Integration of JavaScript was another crucial aspect of the project, aimed at making the webpage more dynamic and interactive. This could include functionality such as alerts, animations, or interactive forms, depending on the JavaScript coding skills and creative ideas implemented. The project placed a strong emphasis on responsive design, ensuring a seamless user experience across various devices, from mobile phones to desktop computers. This tested the ability to use responsive design principles and Bootstrap's responsive features to adapt the layout and content to different screen sizes.

Overall, the Homepage project provided a comprehensive exercise in web development, challenging the use of HTML, CSS, and JavaScript to create a functional, aesthetically pleasing, and interactive website. It highlighted the importance of combining content, style, and functionality in web design, preparing for more advanced web development tasks.

#### Associated Files
* [images](https://github.com/alex-gillard/CS50_Projects/tree/main/images)
* [hp_index.html](https://github.com/alex-gillard/CS50_Projects/blob/main/hp_index.html)
* [moe.html](https://github.com/alex-gillard/CS50_Projects/blob/main/moe.html)
* [ref.html](https://github.com/alex-gillard/CS50_Projects/blob/main/ref.html)
* [rep.html](https://github.com/alex-gillard/CS50_Projects/blob/main/rep.html)
* [hp_styles.css](https://github.com/alex-gillard/CS50_Projects/blob/main/hp_styles.css)

## Week 9: Flask
### Birthdays

The Birthdays project involved creating a web application for tracking friends' birthdays. This application was built using Flask, a web framework in Python, and utilized a SQLite database to store birthday data. The objective was to develop a platform that allows users to both view a list of birthdays and add new ones through a web interface.

The project's Flask application, outlined in app.py, was set up with a single route (/) that handled both GET and POST requests. For GET requests, the application displayed an index.html page, rendering a table of all people and their birthdays from the birthdays.db database. The implementation required adding logic to the GET request handler in app.py to query the database and pass the birthday data to the index.html template.

The index.html page included a form enabling users to input a new birthday, specifying a name, a month, and a day. This form submitted data to the / route using the POST method. In app.py, the POST request handler was programmed to insert the new birthday data into the birthdays.db database, after which the index page was re-rendered to include the new entry.

Participants had the option to extend the functionality of the web application by adding features to edit or delete birthday entries or any other additional features of their choosing. This project provided a practical experience in developing a full-stack web application, combining backend logic with database interaction and frontend presentation. It showcased the integration of Python with HTML and SQL to create a dynamic, user-interactive web application.

#### Associated Files

* [bd_index.html](https://github.com/alex-gillard/CS50_Projects/blob/main/bd_index.html)
* [bd_styles.css](https://github.com/alex-gillard/CS50_Projects/blob/main/bd_styles.css)
* [bd_app.py](https://github.com/alex-gillard/CS50_Projects/blob/main/bd_app.py)
* [birthdays.db](https://github.com/alex-gillard/CS50_Projects/blob/main/birthdays.db)

### Finance

The Finance project involved creating a web application that simulated stock trading, enabling users to "buy" and "sell" stocks using real-time stock data. The application was developed using Flask, a Python web framework, and integrated with a financial data provider to access real-time stock prices.

The core functionality of the application included:

User Registration: Implementing a registration feature allowing users to create an account. This involved handling user inputs for usernames and passwords, storing user credentials securely in a database, and managing user sessions.

Stock Quotes: Enabling users to look up current stock prices. Users entered stock symbols, and the application used an external API to fetch real-time data.

Buying Stocks: Allowing users to "buy" stocks. This required validating user inputs, ensuring sufficient account balance, and updating the database with the transaction details.

Selling Stocks: Enabling users to "sell" stocks they owned. The application needed to handle stock selection, validate the number of shares, and update the user's portfolio and balance.

Transaction History: Displaying a history of all user transactions, including both buys and sells, with relevant details like stock symbol, price, number of shares, and transaction date.

Portfolio Display: Showing a summary of the user's current holdings, including the stock names, number of shares owned, current market value of each stock, and the total value of the portfolio.

Account Balance: Maintaining and displaying the user's cash balance, updated with each transaction.

The project was designed to give users a realistic experience of stock trading. It required a blend of backend development (handling data, interfacing with the API, server-side logic) and frontend development (creating interactive web pages). Key technologies and concepts used in this project included Flask for the backend, SQLite for database management, HTML/CSS for frontend development, and JavaScript for enhancing user interactivity.

This project provided a comprehensive experience in building a full-fledged web application, covering aspects of database management, user authentication, external API integration, and dynamic content generation based on user interactions.

#### Associated Files
 * [favicon.ico](https://github.com/alex-gillard/CS50_Projects/blob/main/favicon.ico)
 * [styles.css](https://github.com/alex-gillard/CS50_Projects/blob/main/styles.css)
 * [apology.html](https://github.com/alex-gillard/CS50_Projects/blob/main/apology.html)
 * [buy.html](https://github.com/alex-gillard/CS50_Projects/blob/main/buy.html)
 * [history.html](https://github.com/alex-gillard/CS50_Projects/blob/main/history.html)
 * [fin_index.html](https://github.com/alex-gillard/CS50_Projects/blob/main/fin_index.html)
 * [layout.html](https://github.com/alex-gillard/CS50_Projects/blob/main/layout.html)
 * [login.html](https://github.com/alex-gillard/CS50_Projects/blob/main/login.html)
 * [quote.html](https://github.com/alex-gillard/CS50_Projects/blob/main/quote.html)
 * [quoted.html](https://github.com/alex-gillard/CS50_Projects/blob/main/quoted.html)
 * [register.html](https://github.com/alex-gillard/CS50_Projects/blob/main/register.html)
 * [sell.html](https://github.com/alex-gillard/CS50_Projects/blob/main/sell.html)
 * [fin_app.py](https://github.com/alex-gillard/CS50_Projects/blob/main/fin_app.py)
 * [finance.db](https://github.com/alex-gillard/CS50_Projects/blob/main/finance.db)
 * [helpers.py](https://github.com/alex-gillard/CS50_Projects/blob/main/helpers.py)



