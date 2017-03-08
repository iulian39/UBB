#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*1)
a. Generate all the prime numbers smaller than a given natural number n.
b. Given a vector of numbers, find the longest increasing contiguous subsequence.
c. Generate the first n prime numbers (n is a given natural number)
*/


int* GeneratePrimeNumbers(int n);
int* GenerateNPrimeNumbers(int n);
void Menu();
bool IsPrime(int nr);
int* FindLongestSubsequence();
int* ReadArray();
int ReadNumber();

int main()
{
	char command;
	int n, i;
	while (1)
	{
		Menu();
		printf("Please enter the command : ");
		scanf("\n%c", &command);

		if (command == '1')
		{
			n = ReadNumber();
			int *sir = malloc(sizeof(int) * n);
			sir = GeneratePrimeNumbers(n);
			for (i = 0; i < n; i++)
			{
				if (sir[i] == 0)
					break;
				printf("%d ", sir[i]);
			}
			free(sir);
			printf("\n");
		}

		else
			if (command == '2')
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
				if (command == '3')
				{
					int n = ReadNumber(), i;
					int *sir = malloc(sizeof(int) * n);
					sir = GenerateNPrimeNumbers(n);
					for (i = 0; i < n; i++)
					{
						printf("%d ", sir[i]);
					}
					free(sir);
					printf("\n");
				}
				else
					if (command == '0')
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
	printf("3 - Generate the first n prime numbers (n is a given natural number)\n");
	printf("0 - Exit\n");
}

//The function used to generate all the prime numbers below a given number
int* GeneratePrimeNumbers(int n)
{
	int i, cnt = 0;
	int *sir = malloc(sizeof(int) * n);
	for (i = 2; i < n; ++i)
		if (IsPrime(i) == true)
			sir[cnt++] = i;
	sir[cnt] = 0;
	return sir;

}

//Checks if a number is prime or not
bool IsPrime(int nr)
{
	if (nr < 2)
		return false;
	if (nr == 2)
		return true;
	int i;
	for (i = 2; i <= nr / 2; i++)
		if (nr % i == 0)
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
		if (sir1[i] == 0)
			break;
		len_sir = i + 1;
	}
	for (i = 0; i < len_sir - 1; ++i)
		if (sir1[i] < sir1[i + 1])
		{
			cnt = 2;
			for (j = i + 1; j < len_sir - 1; ++j)
				if (sir1[j] < sir1[j + 1])
				{
					cnt++;
					if (j + 1 == len_sir - 1)
					{
						cnt++;
						if (cnt > maxLen)
						{
							maxLen = cnt;
							poz1 = i;
							poz2 = j + 1;
						}

					}
				}					
				else
				{
					if (cnt > maxLen)
					{
						maxLen = cnt;
						poz1 = i;
						poz2 = j;
					}
					i = j - 1;
					break;
				}

		}
	if (poz2 == 0)
		poz2 = len_sir - 1;

	j = -1;
	int *sir2 = malloc(sizeof(int) * 200);
	for (i = poz1; i <= poz2; ++i)
		sir2[++j] = sir1[i];
	sir2[++j] = 0;
	free(sir1);

	return sir2;

}

// reads a number from the keyboard
int ReadNumber()
{
	int n;
	scanf("%d", &n);
	return n;
}

//Generate the first n prime numbers (n is a given natural number)
int* GenerateNPrimeNumbers(int n)
{
	int *sir = malloc(sizeof(int) * n);
	int i = 2, cnt = 0;
	while (n)
	{
		if (IsPrime(i))
		{
			sir[cnt++] = i;
			i++;
			n--;
		}
		else
			i++;

	}

	return sir;
}
