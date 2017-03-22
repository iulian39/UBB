#pragma once

typedef struct 
{
	char *name;
	double concentration;
	int quantity;
	double price;

}Pharmacy;

Pharmacy* createMedication(char *name, double concentration, int quantity, double price);
void deleteMedication(Pharmacy *med);
Pharmacy* copyMedication(Pharmacy* p);

char *getName(Pharmacy *med);
double getConcentration(Pharmacy *med);
int getPrice(Pharmacy *med);
int getQuantity(Pharmacy *med);

void toString(Pharmacy *med, char str[]);
void setQuantity(Pharmacy *med, double newConcentration);
