#include <stdio.h>
#include <stdint.h>

// Alias
typedef int8_t DATATYPE;

int main(void)
{
    // File I/O commands

    // FILE type | pointer | targetfile | read-mode
    FILE *input = fopen("hello.txt", "r");
    if (input == NULL)
    {
        return 1;
    }
    /* 
    fopen essentially finds the address of the file;
    it is assigned to pointer input;
    */
    
    DATATYPE buffer[3];
    // store location | size of chunk | how many chunks | read location
    fread(buffer,1,3,input);
    // input pointer "remembers" last read location

    fclose(input);

    // Test print
    for (int i = 0; i < 3; i++)
    {
        printf("%i ", buffer[i]);
    }

    return 0;
}