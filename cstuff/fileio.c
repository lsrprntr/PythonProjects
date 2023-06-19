#include <stdio.h>

// Alias
typedef int8_t DATATYPE;

int main(void)
{
    // File I/O commands

    // FILE type | pointer | targetfile | read-mode
    FILE *input = fopen("hello.txt", "r");
    /* 
    fopen essentially finds the address of the file;
    it is assigned to pointer input;
    */
    
    DATATYPE buffer;
    // store location | size of chunk | how many chunks | read location
    fread(buffer,1,3,input);

    // input pointer "remembers" last read location
}