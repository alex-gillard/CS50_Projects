#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        printf("Error: Two arguments are required (eg. './reverse input.wav output.wav')\n");
        return 1;
    }

    // Open input file for reading
    FILE *file_i = fopen(argv[1], "r");
    if (file_i == NULL)
    {
        printf("Error: Could not open file\n");
        return 1;
    }

    // Read header
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, file_i);

    // Use check_format to ensure WAV format
    if (!check_format(header))
    {
        printf("Error: File is not in WAV format\n");
        fclose(file_i);
        return 1;
    }

    // Open output file for writing
    FILE *file_o = fopen(argv[2], "w");
    if (file_o == NULL)
    {
        printf("Error: Could not open file\n");
        fclose(file_i);
        return 1;
    }

    // Write header to file
    if (fwrite(&header, sizeof(WAVHEADER), 1, file_o) != 1)
    {
        printf("Error: Could not write file\n");
        fclose(file_i);
        fclose(file_o);
        return 1;
    }

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(header);

    // Write reversed audio to file
    fseek(file_i, -block_size, SEEK_END);

    uint8_t *buffer = malloc(block_size);

    while (ftell(file_i) >= sizeof(WAVHEADER)) // Updated this line
    {
        if (fread(buffer, block_size, 1, file_i) != 1)
        {
            printf("Error: Could not read audio data\n");
            free(buffer);
            fclose(file_i);
            fclose(file_o);
            return 1;
        }

        if (fwrite(buffer, block_size, 1, file_o) != 1)
        {
            printf("Error: Could not write audio data\n");
            free(buffer);
            fclose(file_i);
            fclose(file_o);
            return 1;
        }

        fseek(file_i, -2 * block_size, SEEK_CUR);
    }

    free(buffer);
    if (fclose(file_i) != 0)
    {
        printf("Error closing input file\n");
        return 1;
    }

    if (fclose(file_o) != 0)
    {
        printf("Error closing output file\n");
        return 1;
    }
    return 0;
}

int check_format(WAVHEADER header)
{
    if ((strncmp((const char *) header.chunkID, "RIFF", 4) == 0) && (strncmp((const char *) header.format, "WAVE", 4) == 0))
    {
        return 1; // True
    }
    return 0; // False
}

int get_block_size(WAVHEADER header)
{
    // Block size = number of channels * bytes per sample
    int block_size = header.numChannels * (header.bitsPerSample / 8);
    return block_size;
}
