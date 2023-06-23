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

    node *root = malloc(sizeof(node));
    node *child = malloc(sizeof(node));



    root->number = 1;
    root->ptr = child;
    child->number = 3;
    child->ptr = NULL;

    node *cursor = malloc(sizeof(node));


    cursor->number = 2;
    cursor = root->ptr;

    // Should point to child number
    printf("%i\n",cursor->number);




    free(root);
    free(child);
    //free(cursor);
    free(n);
    free(q);
    free(p);
    return 0;
}