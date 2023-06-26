#include <stdio.h>
#include <string.h>

typedef struct node
{
    char word[46];
    struct node *next;
}
node;

node *table[27];

int main(void)
{
    for (int i = 0; i < 26; i++)
    {
        //strcpy(table[i]->word, "\0");
        table[i]->next = NULL;
        printf("Yes\n");
    }
}
