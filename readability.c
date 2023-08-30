#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string txt);
int count_words(string txt);
int count_sents(string txt);

int main(void)
{
    // Prompt user for text string
    string text = get_string("Text: ");

    // Functions which count letters, words, and sentences
    int lets = count_letters(text);
    int wds = count_words(text);
    int sts = count_sents(text);

    // Defining L and S for Coleman-Liau index
    float L = ((float) lets / wds) * 100;
    float S = ((float) sts / wds) * 100;

    // Defining Coleman-Liau index formula for reading comprehension level
    float CLI = 0.0588 * L - 0.296 * S - 15.8;
    // Testing the reading comprehension level against the CLI formula
    if (CLI >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (CLI >= 1)
    {
        printf("Grade %i\n", (int) (CLI + 0.5));
    }
    else
    {
        printf("Before Grade 1\n");
    }
}
// Implementing count letters function
int count_letters(string txt)
{
    int letters = 0;
    for (int i = 0, n = strlen(txt); i < n; i++)
    {
        if (txt[i] >= 'A' && txt[i] <= 'Z')
        {
            letters++;
        }
        else if (txt[i] >= 'a' && txt[i] <= 'z')
        {
            letters++;
        }
    }
    return letters;
}
// Implementing count words function
int count_words(string txt)
{
    int words = 1;
    for (int i = 0, n = strlen(txt); i < n; i++)
    {
        if (txt[i] == ' ')
        {
            words++;
        }
    }
    return words;
}
// Implementing count sentences function
int count_sents(string txt)
{
    int sents = 0;
    for (int i = 0, n = strlen(txt); i < n; i++)
    {
        if (txt[i] == '.' || txt[i] == '!' || txt[i] == '?')
        {
            sents++;
        }
    }
    return sents;
}