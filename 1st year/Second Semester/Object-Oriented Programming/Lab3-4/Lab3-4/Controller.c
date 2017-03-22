#define _CRT_SECURE_NO_WARNINGS
#include "Controller.h"
#include <string.h>
#include <stdlib.h>

Controller *createController(MedRepo *repo, OperationsStack* UndoS, OperationsStack* redoS, CopyLists* undo, CopyLists* redo)
{
	Controller *c = (Controller*)malloc(sizeof(Controller));
	
	c->repo = repo;
	c->undoStack = UndoS;
	c->redoStack = redoS;
	c->undo = undo;
	c->redo = redo;

	return c;
}

void destroyController(Controller *c)
{

	destroyRepo(c->repo);

	destroyStack(c->undoStack);

	destroyStack(c->redoStack);

	destroyStackB(c->undo);

	destroyStackB(c->redo);

	free(c);
}

int FindMedicine(Controller* c, char* name, double concentration)
{
	int i;
	for (i = 0; i < c->repo->medications->length; ++i)
		if (strcmp(c->repo->medications->elems[i]->name , name) == 0 && c->repo->medications->elems[i]->concentration == concentration)
			return i;
	return -1;
}

int addQuantity(Controller * c, char * name, double concentration, int quantity)
{
	int i, result = 0;
	for (i = 0; i < c->repo->medications->length; ++i)
		if (strcmp(c->repo->medications->elems[i]->name, name) == 0 && c->repo->medications->elems[i]->concentration == concentration)
		{
			result = quantityUP(c->repo, quantity, i);
		}
	return result;
}

int addMedication(Controller * c, char * name, double concentration, int quantity, double price)
{
	if (quantity == 0 || price == 0)
		return 0;
	Pharmacy *p = createMedication(name, concentration, quantity, price);
	pushB(c->undo, c->repo);
	int result = add(c->repo, p);

	if (result == 1) // if the medication was successfully added - register the operation
	{
		Operation* o = createOperation(p, "add");
		push(c->undoStack, o);

	}
	else
		popB(c->undo);

	return result;
}

int deleteMedicine(Controller * c, char * name, double concentration)
{
	int i;
	for (i = 0; i < getLengthArray(c->repo->medications); i++)
	{
		if (strcmp(c->repo->medications->elems[i]->name, name) == 0 && c->repo->medications->elems[i]->concentration == concentration)
		{
			Pharmacy * p = createMedication(c->repo->medications->elems[i]->name, c->repo->medications->elems[i]->concentration, c->repo->medications->elems[i]->quantity, c->repo->medications->elems[i]->price);
			Operation* o = createOperation(p, "remove");
			push(c->undoStack, o);
			pushB(c->undo, c->repo);

			break;
		}
	}

	int result = delete(c->repo, name, concentration);
	
	return result;
}

int updateMedication(Controller * c, char * name, double concentration, Pharmacy * med)
{
	int i;
	for (i = 0; i < getLengthArray(c->repo->medications); i++)
	{
		if (strcmp(c->repo->medications->elems[i]->name, name) == 0 && c->repo->medications->elems[i]->concentration == concentration)
		{
			Pharmacy * p = createMedication(c->repo->medications->elems[i]->name, c->repo->medications->elems[i]->concentration, c->repo->medications->elems[i]->quantity, c->repo->medications->elems[i]->price);
			Operation* o = createOperation(p, "update");
			push(c->undoStack, o);

			break;
		}
	}
	pushB(c->undo, c->repo);
	int result = update(c->repo, name, concentration, med);
	Operation* o1 = createOperation(med, "update");
	push(c->undoStack, o1);
	if (result == 0)
		popB(c->undo);
	return result;
}

MedRepo * getRepo(Controller * c)
{
	return c->repo;
}


int filter_price(int a, int b)
{
	return a < b;
}

// FUNCTION POINTER BELOW

MedRepo * filterStringsPrice(Controller * c, double pricelessThan)
{
	int i;
	int(*functionPtr)(int, int);
	functionPtr = &filter_price;
	MedRepo *result = createRepo();
	for (i = 0; i < getLength(c->repo); i++)
		if ((*functionPtr)(c->repo->medications->elems[i]->price, pricelessThan))
			add(result, c->repo->medications->elems[i]);
	return result;
}

MedRepo * filterStringsQuantity(Controller * c, int quantitylessThan, char *choice)
{
	int i, j;
	MedRepo *result = createRepo();
	Pharmacy *aux;

	for (i = 0; i < getLength(c->repo); i++)
	{
		if (c->repo->medications->elems[i]->quantity < quantitylessThan)
		{
			Pharmacy *newMed = getMedicationPosition(c->repo, i);
			add(result, newMed);
		}
	}
	if (strcmp(choice, "ascending") == 0)
	{
		for (i = 0; i < getLength(result); i++)
		{
			for (j = 0; j < getLength(result) - i - 1; j++)
			{
				if (result->medications->elems[j]->quantity > result->medications->elems[j + 1]->quantity)
				{
					aux = result->medications->elems[j];
					result->medications->elems[j] = result->medications->elems[j + 1];
					result->medications->elems[j + 1] = aux;

				}
			}
		}

	}
	else
	{
		for (i = 0; i < getLength(result); i++)
		{
			for (j = 0; j < getLength(result) - i - 1; j++)
			{
				if (result->medications->elems[j]->quantity < result->medications->elems[j + 1]->quantity)
				{
					aux = result->medications->elems[j];
					result->medications->elems[j] = result->medications->elems[j + 1];
					result->medications->elems[j + 1] = aux;

				}
			}
		}
	}

	return result;
}



MedRepo * filterStringsConcentrations(Controller * c, char string[])
{
	int i;
	MedRepo *result = createRepo();
	MedRepo *result2 = createRepo();

	for (i = 0; i < getLength(c->repo); i++)
	{
	
		if (strstr(getName(c->repo->medications->elems[i]), string) != 0)
		{
			
			Pharmacy *newMed = getMedicationPosition(c->repo, i);
			add(result, newMed);
		}
	}
	
	if (result->medications->length == 1)
		return result;

	for (i = 0; i < getLength(result) - 1; i++)
	{
		Pharmacy *med1 = getMedicationPosition(result, i);
		Pharmacy *med2 = getMedicationPosition(result, i + 1);
		if (getConcentration(med1) > getConcentration(med2))
		{
			add(result2, med2);
			add(result2, med1);

		}
		else
		{
			add(result2, med1);
			add(result2, med2);
		}
	}
	return result2;

}

MedRepo* filterStrings(Controller * c, char substring[])
{
	int i;
	MedRepo *result = createRepo();
	MedRepo *result2 = createRepo();
	

	if (strcmp(substring,"")==0)
	{
		for (i = 0; i < getLength(c->repo); i++)
		{
			Pharmacy *newMed = getMedicationPosition(c->repo, i);
			add(result, newMed);
		}
		return result;
	}
	else
	{
		
		for (i = 0; i < getLength(c->repo); i++)
		{
			Pharmacy *med = getMedicationPosition(c->repo, i);
			if (strstr(getName(med), substring) != NULL)
			{
				Pharmacy *newMedication = createMedication(med->name, med->concentration, med->quantity, med->price);
				add(result, newMedication);
			}
		}

	}

	i = 0;
	for (i = 0; i < getLength(result)-1; i++)
	{
		Pharmacy *med1 = getMedicationPosition(result, i);
		Pharmacy *med2 = getMedicationPosition(result, i+1);
		if (strcmp(getName(med1), getName(med2)) > 0)
		{
			add(result2, med2);
			add(result2, med1);

		}
		else
		{
			add(result2, med1);
			add(result2, med2);
		}
	}
	 
	return result2;

}


int undo(Controller* c)
{
	if (isEmpty(c->undoStack))
		return 0;
	

	Operation* operation = pop(c->undoStack);

	Pharmacy* medication = getMedication(operation);

	if (strcmp(getOperationType(operation), "add") == 0)
	{
		
		char name[29];
		double concentration;
		strcpy(name, getName(medication));
		concentration = medication->concentration;
		delete(c->repo, name, concentration);
		Operation* o = createOperation(medication, "remove");
		push(c->redoStack, o);
	}
	else 
		if (strcmp(getOperationType(operation), "remove") == 0)
		{
			add(c->repo, medication);
			Operation* o = createOperation(medication, "add");
			push(c->redoStack, o);
		}
			
	else 
		if (strcmp(getOperationType(operation), "update") == 0)
		{ 
			char name[29];
			double concentration;
			strcpy(name, getName(medication));
			concentration = medication->concentration;
			delete(c->repo, name, concentration);
			Operation* operation1 = pop(c->undoStack);

			Pharmacy* medication1 = getMedication(operation1);

			add(c->repo, medication1);

			push(c->redoStack, operation);
			push(c->redoStack, operation1);
		}


	return 1;

}

int redo(Controller* c)
{
	if (isEmpty(c->redoStack))
	{
		return 0;
	}


	Operation* operation = pop(c->redoStack);
	Pharmacy* medication = getMedication(operation);

	if (strcmp(getOperationType(operation), "add") == 0)
	{

		char name[29];
		double concentration;
		strcpy(name, getName(medication));
		concentration = medication->concentration;
		delete(c->repo, name, concentration);
		Operation* o1 = createOperation(medication, "remove");
		push(c->undoStack, o1);
	}
	else
		if (strcmp(getOperationType(operation), "remove") == 0)
		{
			add(c->repo, medication);
			Operation* o1 = createOperation(medication, "add");
			push(c->undoStack, o1);
		}

		else if (strcmp(getOperationType(operation), "update") == 0)
		{
			char name[29];
			double concentration;
			strcpy(name, getName(medication));
			concentration = medication->concentration;
			delete(c->repo, name, concentration);
			Operation* operation1 = pop(c->redoStack);

			Pharmacy* medication1 = getMedication(operation1);

			add(c->repo, medication1);

			push(c->undoStack, operation);
			push(c->undoStack, operation1);
		}

	return 1;

}

int undoB(Controller* c)
{
	if (isEmpty(c->undo))
		return 0;

	pushB(c->redo, c->repo);
	MedRepo* a = createRepo();
	a = popB(c->undo);

	c->repo->medications->length = 0;
	for (int i = 0; i < a->medications->length; i++)
	{
		add(c->repo, a->medications->elems[i]);
	}

	
	return 1;

}

int redoB(Controller* c)
{
	if (isEmpty(c->redo))
		return 0;

	pushB(c->undo, c->repo);
	MedRepo* a = createRepo();
	a = popB(c->redo);

	c->repo->medications->length = 0;
	for (int i = 0; i < a->medications->length; i++)
	{
		add(c->repo, a->medications->elems[i]);
	}

	
	return 1;

}
