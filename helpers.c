#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, h_max = height; i < h_max; i++)
    {
        for (int j = 0, w_max = width; j < w_max; j++)
        {
            // Access blue, green, and red pixel colours
            int B = image[i][j].rgbtBlue;
            int G = image[i][j].rgbtGreen;
            int R = image[i][j].rgbtRed;
            // Calculate average of each colour
            int gray = round((float) (B + G + R) / 3);
            // Update each colour value to the average
            image[i][j].rgbtBlue = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtRed = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, h_max = height; i < h_max; i++)
    {
        for (int j = 0, w_max = width; j < w_max; j++)
        {
            // Access blue, green, and red pixel colours
            int B = image[i][j].rgbtBlue;
            int G = image[i][j].rgbtGreen;
            int R = image[i][j].rgbtRed;
            // Calculating sepia colour values
            float sepiaRed = 0.393 * R + 0.769 * G + 0.189 * B;
            float sepiaGreen = 0.349 * R + 0.686 * G + 0.168 * B;
            float sepiaBlue = 0.272 * R + 0.534 * G + 0.131 * B;
            // Calling the rounding function for each sepiaColour
            int SR = (int) round(sepiaRed);
            int SG = (int) round(sepiaGreen);
            int SB = (int) round(sepiaBlue);
            // Ensuring sepiaColour is within range
            int colour_max = 255;
            if (SR > colour_max)
            {
                SR = colour_max;
            }
            if (SG > colour_max)
            {
                SG = colour_max;
            }
            if (SB > colour_max)
            {
                SB = colour_max;
            }
            // Updating each pixel to the sepiaColour
            image[i][j].rgbtBlue = SB;
            image[i][j].rgbtGreen = SG;
            image[i][j].rgbtRed = SR;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, h_max = height; i < h_max; i++)
    {
        for (int j = 0, w_max = width; j < w_max / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][w_max - j - 1];
            image[i][w_max - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    // Create a copy of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Loop through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int count = 0;

            // Check surrounding pixels including itself
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // Check boundaries
                    if ((i + k) >= 0 && (i + k) < height && (j + l) >= 0 && (j + l) < width)
                    {
                        sumRed += copy[i + k][j + l].rgbtRed;
                        sumGreen += copy[i + k][j + l].rgbtGreen;
                        sumBlue += copy[i + k][j + l].rgbtBlue;
                        count++;
                    }
                }
            }

            // Average the sum and assign to the original image pixel
            image[i][j].rgbtRed = round((float) sumRed / count);
            image[i][j].rgbtGreen = round((float) sumGreen / count);
            image[i][j].rgbtBlue = round((float) sumBlue / count);
        }
    }

    return;
}