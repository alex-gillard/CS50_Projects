import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv seq.txt")

    # TODO: Read database file into a variable
    # Open the file listed in the first command line argument in read mode.
    # File will automatically close after nested code is executed.
    with open(sys.argv[1], "r") as data:
        # Create a DictReader object which returns each row as an OrderedDict from provided file
        reader = csv.DictReader(data)
        # fieldnames is a list that contains the names of the fields from the first row (header row) of the .csv file
        fieldnames = reader.fieldnames
        # List comprehension - Goes through each row in reader and adds it to a new list, "data_contents"
        data_contents = [row for row in reader]

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as seq:
        seq_contents = seq.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR_counts = {}
    for STR in fieldnames[1:]:
        STR_counts[STR] = longest_match(seq_contents, STR)

    # TODO: Check database for matching profiles
    for row in data_contents:
        match = True
        for STR in fieldnames[1:]:
            count = int(row[STR])
            if count != STR_counts[STR]:
                match = False
                break
        if match:
            print(row["name"])
            return
    print("No match")
    print()


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
