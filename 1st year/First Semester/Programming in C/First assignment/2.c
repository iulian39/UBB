//2.Read two integers and compute their sum, average and sum of the squares of the numbers.
#include <stdio.h>

int main()
{
    int a, b, sum, squares;
    float average;
    scanf("%d%d", &a, &b);
    sum = a + b;
    printf("The sum is %d\n", sum);
    average = (a + b)/2.0;
    printf("The average is %.2f\n", average);
    squares = a*a + b*b;
    printf("The sum of squares is %d\n", squares);

    return 0;
}
