//Multiply 2 matrices of integers.
#include <stdio.h>

int main()
{
  int m, n, p, q, c, d, k, sum = 0, i;
  int first[10][10], second[10][10], multiply[10][10];

  printf("Enter the number of rows and columns of first matrix\n");
  scanf("%d%d", &n, &m);
  int **mat1 = (int **)malloc(n * sizeof(int*));
  for( i = 0; i < n; i++)
    mat1[i] = (int *)malloc(m * sizeof(int));
  printf("Enter the elements of first matrix\n");
  for (c = 0; c < n; c++)
    for (d = 0; d < m; d++)
      scanf("%d", &mat1[c][d]);

  printf("Enter the number of rows and columns of second matrix\n");
  scanf("%d%d", &p, &q);
  if (n != p)
    printf("Matrices with entered orders can't be multiplied with each other.\n");
  else
  {
      int **mat2 = (int **)malloc(p * sizeof(int*));
      for( i = 0; i < p; i++)
        mat2[i] = (int *)malloc(q * sizeof(int));
      printf("Enter the elements of second matrix\n");
      for (c = 0; c < p; c++)
          for (d = 0; d < q; d++)
            scanf("%d", &mat2[c][d]);


  int **mat3 = (int **)malloc(n * sizeof(int*));
  for( i = 0; i < n; i++)
    mat3[i] = (int *)malloc(q * sizeof(int));

    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++) {
        for (k = 0; k < p; k++) {
          sum = sum + mat1[c][k]*mat2[k][d];
        }

        mat3[c][d] = sum;
        sum = 0;
      }
    }

    printf("Product of entered matrices:-\n");

    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%d\t", mat3[c][d]);

      printf("\n");
    }
  }

  return 0;
}
