#define _CRT_SECURE_NO_WARNINGS
#include "Medication.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

Pharmacy * createMedication(char * name, double concentration, int quantity, double price)
{
	Pharmacy* med = (Pharmacy*)malloc(sizeof(Pharmacy));
	med->name = (char*)malloc(strlen(name) + 1);
	strcpy(med->name, name);
	med->concentration = concentration;
	med->quantity = quantity;
	med->price = price;


	return med;


}

void deleteMedication(Pharmacy *med)
{
	
	free(med->name);
	
	free(med);
}

char* getName(Pharmacy* med)
{
	return med->name;
}

double getConcentration(Pharmacy *med)
{
	return med->concentration;
}

int getQuantity(Pharmacy *med)
{
	return med->quantity;
}

int getPrice(Pharmacy *med)
{
	return med->price;
}

void toString(Pharmacy *med,char str[])
{
	sprintf(str, "The %s has the concentration %.2f , the quantity is %d and it's price is %.2f ", med->name, med->concentration, med->quantity, med->price);
}

void setQuantity(Pharmacy *med, double newConcentration)
{
	med->concentration = newConcentration;
}


Pharmacy* copyMedication(Pharmacy* p)
{
	if (p == NULL)
		return NULL;

	Pharmacy* newMedication = createMedication(getName(p), getConcentration(p), getQuantity(p), getPrice(p));
	return newMedication;
	

}