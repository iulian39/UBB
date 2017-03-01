#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*1)
a. Generate all the prime numbers smaller than a given natural number n.
b. Given a vector of numbers, find the longest increasing contiguous subsequence.
*/


void GeneratePrimeNumbers();
void Menu();
bool IsPrime(int nr);
int* FindLongestSubsequence();
int* ReadArray();

int main()
{
    char command;
    while ( 1 )
    {
        Menu();
        printf("Please enter the command : ");
        scanf("\n%c", &command);

        if ( command == '1' )
            GeneratePrimeNumbers();
        else
            if ( command == '2' )
            {
                int *sir1 = malloc(sizeof(int) * 200);
                sir1 = FindLongestSubsequence();
                int i;
                for (i = 0; i < 200; i++)
                {
                    if (sir1[i] == 0)
                        break;
                    printf("%d ", sir1[i]);
                }
                free(sir1);
                printf("\n");
            }
            else
                if ( command == '0' )
                    break;
    }
    return 0;
}
//The menu of the program
void Menu()
{
    printf("Available Commands:\n");
    printf("1 - Generate all the prime numbers smaller than a given natural number n\n");
    printf("2 - Given a vector of numbers, find the longest increasing contiguous subsequence\n");
    printf("0 - Exit\n");
}

//The function used to generate all the prime numbers below a given number
void GeneratePrimeNumbers()
{
    int n, i;
    printf("\nPlease enter the number :");
    scanf("%d", &n);
    for (i = 2; i < n; ++i)
        if(IsPrime(i) == true)
            printf("%d ", i);
    printf("\n");

}

//Checks if a number is prime or not
bool IsPrime(int nr)
{
    if ( nr < 2 )
        return false;
    if ( nr == 2)
        return true;
    int i;
    for (i = 2; i <= nr/2 ; i++)
        if(nr % i == 0)
            return false;
    return true;
}

//Reads the array
int* ReadArray()
{
    int x, i = 0;
    int *sir1 = malloc(sizeof(int) * 200);
    while (1)
    {
        scanf("%d", &x);
        if (x == 0)
            break;
        else
            sir1[i++] = x;
    }

    sir1[i] = 0;
    return sir1;
}

//Given a vector of numbers, find the longest increasing contiguous subsequence
int* FindLongestSubsequence()
{
    int x, i = 0, maxLen = -1, j, poz1 = 0, poz2 = 0, cnt = 0;
    int *sir1 = ReadArray();
    int len_sir = 0;
    for (i = 0; i < 200; i++) {
        if (sir1[i] == 0) break;
        len_sir = i + 1;
    }
    for (i = 0; i < len_sir - 1; ++i)
        if (sir1[i] < sir1[i + 1])
        {
            cnt = 2;
            for ( j = i + 1; j < len_sir - 1; ++j )
                if(sir1[j] < sir1[j + 1])
                    cnt++;
                else
                {
                    if (cnt > maxLen)
                    {
                        maxLen = cnt;
                        poz1 = i;
                        poz2 = j;
                    }
                    i += j - 1;
                    break;
                }

        }
    if ( poz2 == 0)
        poz2 = len_sir - 1;

    j = -1;
    int *sir2 = malloc(sizeof(int) * 200);
    for ( i = poz1; i <= poz2; ++i)
        sir2[++j] = sir1[i];
    sir2[++j] = 0;
    free(sir1);

    return sir2;

}

