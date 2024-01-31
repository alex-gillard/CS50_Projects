// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Custom Prototypes
bool check_null(FILE *ptr);
int *prime_num(void);

// Global variables

int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO: Ensure that the word is in the dictionary
    // Call the hash function for a given word
    unsigned int total = hash(word);
    // Set up pointer to hash table array
    node *ptr_table = table[total % N];
    // Traverse a specific linked list from the hash table
    while (ptr_table != NULL)
    {
        if (strcasecmp(word, ptr_table->word) == 0)
        {
            // printf("Word is: %s\n", ptr_table->word);
            return true;
        }
        ptr_table = ptr_table->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int total = 0;
    // primeBox contains 25 elements of prime numbers.
    int *primeBox = prime_num();
    // Iterate over each character in a word
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        // Convert a given character to its ASCII value
        int ascii_val = toupper(word[i]) - 'A';
        // Multiplication of the ASCII value with a given prime number
        int pos = ascii_val * primeBox[i % 25];
        // Adding result to a total
        total += pos;
    }
    free(primeBox);
    return total;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Make file pointer
    FILE *dict = fopen(dictionary, "r");
    if (!check_null(dict))
    {
        fclose(dict);
        return false;
    }
    // Setting variables
    char word[LENGTH + 1];
    // Read strings from file one at a time
    while (fscanf(dict, "%s", word) != EOF)
    {
        // Create new node for each word
        node *node_new = malloc(sizeof(node));
        if (node_new == NULL)
        {
            fclose(dict);
            return false;
        }
        // Calling hash function and storing it in index, index will only be positive or zero
        unsigned int index = hash(word);
        strcpy(node_new->word, word);
        // Inserting nodes into hash table
        node_new->next = table[index % N];
        table[index % N] = node_new;
        word_count++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // Return number of words in the dictionary.
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Free all memory that was allocated in the load funciton
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor->next;
            free(cursor);
            cursor = temp;
        }
    }
    return true;
}

bool check_null(FILE *ptr)
{
    if (ptr == NULL)
    {
        return false;
    }
    return true;
}

int *prime_num(void)
{
    int *primeBox = malloc(25 * sizeof(int));
    int pIndex = 0;
    for (int i = 2; i < 100; i++)
    {
        bool isPrime = true;
        for (int j = 2, final = i - 1; j < final; j++)
        {
            if (i % j == 0)
            {
                isPrime = false;
                break;
            }
        }
        if (isPrime == true)
        {
            primeBox[pIndex] = i;
            pIndex++;
        }
    }
    return primeBox;
}