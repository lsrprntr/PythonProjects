#include <stdio.h>

int factor(int x);

int main(void)
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Factorial is: %i\n",factor(n));
}

int factor(int x)
{
    if (x == 1)
    {
        return 1;
    }
    return x * factor(x-1);
}