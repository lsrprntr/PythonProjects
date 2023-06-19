#include <stdio.h>

int main(void)
{
    // before compiling what do you think happens?
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14;
    c = &b;
    *c = 25;

    /*
    First line should actually change value of a to 14;
    Then c becomes pointer to b
    b changes to 25
    so a = 14, b = 25, c is pointer to b.
    */
    printf("%i %i %p %p\n",a,b,c,&c);
    return 0;

}