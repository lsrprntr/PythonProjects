#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *ptr;
}
node;

int main(void)
{
    node *n = malloc(sizeof(node));
    node *p = malloc(sizeof(node));
    node *q = malloc(sizeof(node));


    n->number = 1;
    n->ptr = p;

    // OR

    (*n).number = 2;
    (*n).ptr = q;


    return 0;
}