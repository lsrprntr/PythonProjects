#include <stdio.h>

typedef struct
{
    char *name;
    char *number;
}
person;

int main(void)
{
    person contact[2];
    contact[0].name = "David";
    contact[0].number = "+61422684635";

    person list[1];
    // You can copy struct to struct
    list[0] = contact[0];

    printf("%s %s\n",list[0].name,list[0].number);

}