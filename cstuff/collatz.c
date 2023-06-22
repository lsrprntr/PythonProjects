#include <stdio.h>

int collatz(int n);

int main(void)
{
    
    printf("Enter a positive integer: ");
    int n;
    if (scanf("%d", &n) != 1)
    {
        printf("Error: Only input integers.\n");
        return 1;
    }
    if (n <= 0)
    {
        printf("Error: Only positive integers greater than 0.\n");
        return 1;
    }

    collatz(n);
    return 0;
}

int collatz(int n)
{
    if (n == 1)
    {
        printf("1\n");
        return 1;
    }
    if (n%2 == 0)
    {
        printf("%i->",n);
        return collatz(n/2);
    }
    else
    {
        printf("%i->",n);
        return collatz(3*n+1);
    }
}