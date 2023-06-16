
void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    swap(&x,&y);

    printf("%i %i\n", x, y);

    return;

}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
    return;
}
