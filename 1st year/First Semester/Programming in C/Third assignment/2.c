//2. Write a program that reads a 2D array and prints transpose of the array.
#include <stdio.h>

void PrintMatrix(int sir[][100], int n, int m);
void PrintMatrixP(int sir[][100], int *n, int *m);

int main()
{
    int n, m, i, j, sir[100][100];
    printf("Insert the values : \n");
    scanf("%d%d", &n, &m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &sir[i][j]);
    PrintMatrix(sir, n, m);
    int *ptr1 = &n, *ptr2 = &m;
    printf("\n");
    PrintMatrixP(sir, ptr1, ptr2);


    return 0;
}

void PrintMatrix(int sir[][100], int n, int m)
{
    int i, j;
    for ( j = 0; j < m; ++j)
    {
        for ( i = 0; i < n; ++i)
            printf(" %d", sir[i][j]);
        printf("\n");
    }
}

void PrintMatrixP(int sir[][100], int *n, int *m)
{
    int i, j;
    for ( j = 0; j < *m; ++j)
    {
        for ( i = 0; i < *n; ++i)
            printf(" %d", sir[i][j]);
        printf("\n");
    }
}
