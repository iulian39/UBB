//1. Write a program to read a set of integers and print the maximum and minimun value.
#include <stdio.h>

void FindMinMax(int sir[], int *maxim, int *minim);

int main()
{
    int maxim = -0x3f3f3f3f, minim = 0x3f3f3f3f, sir[5];
    int i = 0;
    for ( i = 0; i < 5; ++i)
    {
        scanf("%d", &sir[i]);
        if (sir[i] > maxim)
            maxim = sir[i];
        if (sir[i] < minim)
            minim = sir[i];
    }

    printf("The maxim value is %d\nThe minim value is %d\n", maxim, minim);
    maxim = -0x3f3f3f3f;
    minim = 0x3f3f3f3f;
    int *ptr1 = &maxim, *ptr2 = &minim;
    FindMinMax(sir, ptr1, ptr2);
    printf("The maxim value is %d\nThe minim value is %d\n", maxim, minim);


    return 0;
}

void FindMinMax(int sir[], int *maxim, int *minim)
{
    int i;
    for ( i = 0; i < 5; ++i)
    {
        if (sir[i] > *maxim)
            *maxim = sir[i];
        if (sir[i] < *minim)
            *minim = sir[i];
    }
}
