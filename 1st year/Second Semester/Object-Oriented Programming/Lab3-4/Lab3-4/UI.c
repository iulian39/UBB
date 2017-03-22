#define _CRT_SECURE_NO_WARNINGS
#include "UI.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

UI *createUI(Controller* c)
{
	UI *ui = (UI*)malloc(sizeof(UI));
	ui->ctrl = c;
	return ui;
}
void clearScreen()
{
	//for (int i = 1; i <= 40; i++)
		//printf("\n");

}
/*Prints the available menu for the user*/
void printMenu()
{
	printf("\n**********************************************************\n");
	printf("1  - to add a new medicine\n");
	printf("2  - to delete a medicine\n");
	printf("3  - to update a medicine\n");
	printf("4  - list all the available medications\n");
	printf("5  - list all the medications with a given substring\n");
	printf("6  - list all the medications sorted by concentration\n");
	printf("7  - list all the medications that are in short supply\n");
	printf("8  - list all the medications that have a lower price\n");
	printf("9  - undo\n");
	printf("10 - redo\n");
	printf("11 - undo lists\n");
	printf("12 - redo lists\n");
	printf("0  - exit\n");
	printf("**********************************************************\n");

}
/*
Verifies if the given command is valid (is either 1, 2 or 0)
	Input: command - integer
	Output: 1 - if the command is valid
			0 - otherwise
*/
int validCommand(int command)
{
	if (command >= 0 && command <= 12)
		return 1;
	return 0;
}
int readIntegerNumber(const char* message)
{
	char s[16];
	int res = 0;
	int flag = 0;
	int r = 0;

	while (flag == 0)
	{
		printf(message);
		scanf("%s", s);

		r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
		flag = (r == 1);
		if (flag == 0) 
		{
			clearScreen();
			printMenu();
			printf("Error reading number!\n");
		}
	}
	return res;
}

double readDoubleNumber(const char* message)
{
	char s[16];
	int flag = 0;
	int r = 0;
	double d = 0;

	while (flag == 0)
	{
		printf(message);
		scanf("%s", s);

		r = sscanf(s, "%lf", &d);	// reads data from s and stores them as double, if possible; returns 1 if successful
		flag = (r == 1);


		if (flag == 0)
			printf("Error reading number!\n");
	}

	return d;

}

int addMedicationUI(UI *ui)
{
	char name[30];
	double concentration, price;
	int quantity, index = -1;

	printf("Please input the name of the medication: ");
	scanf("%29s", name);
	concentration = readDoubleNumber("Please input the concentration : ");
	while(concentration < 0 || concentration > 100 )
		concentration = readDoubleNumber("Concentration has to be between 0 and 100 !\nPlease input the concentration : ");
	quantity = readIntegerNumber("Please input the quantity : ");
	while ( quantity == 0)
		quantity = readIntegerNumber("Quantity cannot be 0 !\nPlease input the quantity : ");
	index = FindMedicine(ui->ctrl, name, concentration);
	if (index != -1)
		return addQuantity(ui->ctrl, name, concentration, quantity);

	price = readDoubleNumber("Please input the price(in $):  ");
	while (price == 0)
		price = readDoubleNumber("Price cannot be 0 !\nPlease input the price(in $):  ");

	return addMedication(ui->ctrl, name, concentration, quantity, price);

}
int updateMedicationUI(UI *ui)
{
	Pharmacy *med;
	char name1[30],name2[30];
	double concentration1,concentration2, price;
	int quantity;
	printf("Please enter the name of the medication which is going to be updated: ");
	scanf("%29s", name1);
	concentration1 = readDoubleNumber("Please input the concentration : ");
	printf("Please enter the name of the new medication: ");
	scanf("%29s", name2);
	concentration2 = readDoubleNumber("Please input the concentration : ");
	while (concentration2 < 0 || concentration2 > 100)
		concentration2 = readDoubleNumber("Concentration has to be between 0 and 100 !\nPlease input the concentration : ");
	quantity = readIntegerNumber("Please input the quantity : ");
	while (quantity == 0)
		quantity = readIntegerNumber("Quantity cannot be 0 !\nPlease input the quantity : ");
	price = readDoubleNumber("Please input the price(in $):  ");
	while (price == 0)
		price = readDoubleNumber("Price cannot be 0 !\nPlease input the price(in $):  ");
	med = createMedication(name2, concentration2, quantity, price);

	return updateMedication(ui->ctrl, name1, concentration1, med);

}
int deleteMedicationUI(UI *ui)
{
	char name[30];
	double concentration;


	printf("Please enter the name of the medication which is going to be deleted:");
	scanf("%29s", name);
	concentration = readDoubleNumber("Please input the concentration : ");

	return deleteMedicine(ui->ctrl, name, concentration);


}
void listAllMedications(UI* ui)
{
	MedRepo* repo = getRepo(ui->ctrl);
	int length = getLength(repo);

	if (length == 0)
	{
		printf("There are no stored medications \n");
	}
	int i = 0;
	for (i = 0; i < getLength(repo); i++)
	{
		char str[200];
		toString(getMedicationPosition(repo, i), str);
		printf("%s\n", str);
	}
}

void listAllMedicationsInShortSupply(UI* ui)
{
	char choice[30];
	int quantity;
	quantity = readIntegerNumber("Please enter the quantity: ");
	printf("Please enter your choice ascending/descending: ");
	scanf("%29s", choice);
	MedRepo *result = filterStringsQuantity(ui->ctrl, quantity, choice);
	if (getLength(result) == 0)
		printf("There are no medications with quantity less than %d", quantity);
	else
	{
		int i = 0;
		for (i = 0; i < getLength(result); i++)
		{
			char str[200];
			toString(getMedicationPosition(result, i), str);
			printf("%s\n", str);
		}
	}

	
}

void listAllMedicationsLowerThanXPrice(UI *ui)
{
	double price;
	price = readDoubleNumber("Please enter the price: ");
	MedRepo *result = filterStringsPrice(ui->ctrl, price);
	if (getLength(result) == 0)
		printf("There are no medications with price less than %.2f", price);
	else
	{
		int i = 0;
		for (i = 0; i < getLength(result); i++)
		{
			char str[200];
			toString(getMedicationPosition(result, i), str);
			printf("%s\n", str);
		}
	}


}


void listAllMedicationsSortedByConcentration(UI *ui)
{
	char string[30];
	printf("Please enter the name of the medicine: ");
	scanf("%29s", string);

	char string1[30];
	printf("Please enter the sorting method(ascending/descending): ");
	scanf("%29s", string1);

	MedRepo *result = filterStringsConcentrations(ui->ctrl, string);
	Pharmacy* aux;
	int length = getLength(result);
	if (length == 0)
	{
		printf("There are no medications with the given string.\n");
		return;
	}
	else
	{
		int i, j;
		if (strcmp(string1, "ascending"))
		{
			for (i = 0; i < length - 1; ++i)
				for (j = i + 1; j < length; ++j)
					if (result->medications->elems[i]->concentration < result->medications->elems[j]->concentration)
					{
						aux = result->medications->elems[i];
						result->medications->elems[i] = result->medications->elems[j];
						result->medications->elems[j] = aux;
					}
		}
		else if (strcmp(string1, "descending"))
		{
			for (i = 0; i < length - 1; ++i)
				for (j = i + 1; j < length; ++j)
					if (result->medications->elems[i]->concentration > result->medications->elems[j]->concentration)
					{
						aux = result->medications->elems[i];
						result->medications->elems[i] = result->medications->elems[j];
						result->medications->elems[j] = aux;
					}
		}
		
		for (i = 0; i < length; i++)
		{
			char str[200];
			toString(getMedicationPosition(result, i), str);
			printf("%s\n", str);
		}
	}

}

void listAllMedicationsWithAGivenSubstring(UI *ui)
{
	char substring[30];
	printf("Please input your substring. If the string is empty, all the medications are taken: ");
	scanf("%29s", substring);

	MedRepo *result = filterStrings(ui->ctrl, substring);
	int length = getLength(result);
	if (length == 0)
	{
		printf("There are no medications with the given substring.\n");
		return;
	}
	else
	{
		int i,j;
		Pharmacy * aux;
		
		for (i = 0; i < length - 1; i++)  
			for (j = i + 1; j < length; j++)
				if (strcmp(result->medications->elems[i]->name, result->medications->elems[j]->name) > 0)
				{
					aux = result->medications->elems[i];
					result->medications->elems[i] = result->medications->elems[j];
					result->medications->elems[j] = aux;
				}
		for (i = 0; i < length; i++)
		{
			char str[200];
			toString(getMedicationPosition(result, i), str);
			printf("%s\n", str);
		}
	}

}
void destroyUI(UI * ui)
{
	// first destroy the controller
	destroyController(ui->ctrl);
	// free the UI memory
	free(ui);
}

int undoUI(UI * ui)
{
	int res = undo(ui->ctrl);
	return res;
}

int redoUI(UI * ui)
{
	int res = redo(ui->ctrl);
	return res;
}

int undoUIB(UI * ui)
{
	int res = undoB(ui->ctrl);
	return res;
}

int redoUIB(UI * ui)
{
	int res = redoB(ui->ctrl);
	return res;
}

void startUI(UI * ui)
{
	while (1)
	{
		clearScreen();
		printMenu();
		int command = readIntegerNumber("Input command: ");
		while (validCommand(command) == 0)
		{
			printf("Please input a valid command!\n");
			command = readIntegerNumber("Input command: ");
		}
		if (command == 0)
			break;
		switch (command)
		{
			case 1:
			{
				int res = addMedicationUI(ui);
				if (res == 1)
					printf("The medication was succesfully added");
				if (res == 2)
					printf("The quantity of the medicine was succesfully updated");
				break;
			}
			case 2:
			{
				int res = deleteMedicationUI(ui);
				if (res == 1)
					printf("The medication was succesfully deleted");
				else
					printf("There is no medication with this name or concentration!");
				break;
			}
			case 3:
			{
				int res = updateMedicationUI(ui);
				if (res == 1)
					printf("The medication was succesfully updated");
				else
				{
					printf("The medication with ths name or concetration does not exist!");
				}
				break;
			}
			case 4:
			{
				listAllMedications(ui);
				break;
			}
			case 5:
			{
				listAllMedicationsWithAGivenSubstring(ui);
				break;
			}
			case 6:
			{
				listAllMedicationsSortedByConcentration(ui);
				break;
			}
			case 7:
			{
				listAllMedicationsInShortSupply(ui);
				break;
			}
			case 8:
			{
				listAllMedicationsLowerThanXPrice(ui);
				break;
			}
			case 9:
			{
				int res = undoUI(ui);
				if (res == 1)
					printf("You have just undo the last operation\n");
				else
					printf("Nothing to undo :(\n");
				break;
			}
			case 10:
			{
				int res = redoUI(ui);
				if (res == 1)
					printf("You have just redo the last operation\n");
				else
					printf("Nothing to redo :(\n");
				break;
			}
			case 11:
			{
				int res = undoUIB(ui);
				if (res == 1)
					printf("You have just undo the last operation\n");
				else
					printf("Nothing to undo :(\n");
				break;
			}
			case 12:
			{
				int res = redoUIB(ui);
				if (res == 1)
					printf("You have just redo the last operation\n");
				else
					printf("Nothing to redo :(\n");
				break;
			}
		}
	}
}
