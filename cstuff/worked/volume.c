// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

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
    // Create variable header of 44 8-bit chunks
    // 'u' is for unsigned which can be only positive ints, doesnt matter for header
    uint8_t header[HEADER_SIZE];

    // Read from input into header
    // fread reads from input FILE and puts it into memory at location &header
    // reads HEADER_SIZE byte one time
    fread(&header, HEADER_SIZE, 1, input);
    fwrite(&header, HEADER_SIZE, 1, output);

    // fread for next loop should remember where last INPUT FILE ended

    // TODO: Read samples from input file and write updated data to output file
    // size of 16 bits for sample size
    // no 'u' means it is a signed int, can be negative or positive ints.
    int16_t buffer;

    // while loop reads repeatedly until end of file, starting from &header location
    while (fread(&buffer, sizeof(int16_t), 1,input))
    {
        // Update volume
        buffer *= factor;
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }



    // Close files
    fclose(input);
    fclose(output);
}
