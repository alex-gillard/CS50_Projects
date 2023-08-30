#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // initialize blocks and gaps for pyramid
    string block = "#";
    string gap = " ";
    // prompt user for numbers between 1 and 8 inclusive, continue loop until user follows prompt
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (!(n >= 1 && n <= 8));
    // create loop for printing blocks and gaps
    for (int i = 0; i < n; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            printf("%s", gap);
        }
        for (int k = i + 1; k > 0; k--)
        {
            printf("%s", block);
        }
        printf("\n");
    }
}