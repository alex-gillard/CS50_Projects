#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string msg = get_string("Message: ");
    int n = strlen(msg);
    int j = 8;
    int bits[n][j];
    for (int i = 0; i < n; i++)
    {
        for (int bit = 7; bit >= 0; bit--)
        {
            int bit_val = (msg[i] >> bit) & 1;
            bits[i][bit] = bit_val;
            print_bulb(bit_val);
        }
        printf("\n");
    }
    printf("\n");
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
