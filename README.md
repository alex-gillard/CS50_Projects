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



