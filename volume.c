// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // Header is always 44 bytes, use fread to read 44 bytes from input, fwrite to write 44 new bytes to output file

    uint8_t header_input[HEADER_SIZE];
    fread(header_input, HEADER_SIZE, 1, input);
    fwrite(header_input, HEADER_SIZE, 1, output);
    // TODO: Read samples from input file and write updated data to output file

    // for each 2 byte sample, update volume, write updated volume to output

    int16_t buffer;
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        buffer = (factor * buffer);
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }
        fclose(input);
        fclose(output);
}
