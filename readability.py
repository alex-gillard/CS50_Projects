# TODO
from cs50 import get_string


def main():
    # Get text from user
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sents(text)
    calc_CLI(letters, words, sentences)


# Function which counts letters from given text
def count_letters(text):
    letters = 0
    txt_len = len(text)
    for i in range(txt_len):
        if text[i] >= "A" and text[i] <= "Z":
            letters += 1
        if text[i] >= "a" and text[i] <= "z":
            letters += 1
    return letters


# Function which counts words from given text
def count_words(text):
    words = 1
    txt_len = len(text)
    for i in range(txt_len):
        if text[i] == " ":
            words += 1
    return words


# Function which counts sentences from given text
def count_sents(text):
    sents = 0
    txt_len = len(text)
    for i in range(txt_len):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            sents += 1
    return sents


def calc_CLI(letters, words, sentences):
    # Define variables L and S for the Coleman-Liau index
    L = float(letters / words) * 100
    S = float(sentences / words) * 100
    # Coleman-Liau index formula
    CLI = round(0.0588 * L - 0.296 * S - 15.8)
    # Evaluating reading comprehension level based on the CLI value
    if CLI >= 16:
        print("Grade 16+")
        print()
    elif CLI >= 1:
        print(f"Grade {CLI}")
        print()
    else:
        print("Before Grade 1")
        print()


main()
