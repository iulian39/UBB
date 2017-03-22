#pragma once
#include "MedRepo.h"
#include "Operations.h"
#include "UndoBonus.h"


typedef struct
{
	MedRepo *repo;
	OperationsStack * undoStack;
	OperationsStack * redoStack;
	CopyLists* undo;
	CopyLists* redo;
}Controller;

Controller *createController(MedRepo *repo, OperationsStack* UndoS, OperationsStack* redoS, CopyLists* undo, CopyLists* redo);

void destroyController(Controller*c);
/*Adds a medication to the list , if possible*/
int addMedication(Controller *c, char *name, double concentration, int quantity, double price);

/*Delete a medication from the list if it exist*/
int deleteMedicine(Controller *c, char *name, double concentration);

/*Update a medication from the list, if possible*/
int updateMedication(Controller *c, char* name, double concentration, Pharmacy *med);

MedRepo *getRepo(Controller *c);
/*Returns a repository which contains all the medications with the given substring*/
MedRepo*filterStringsConcentrations(Controller *c, char string[]);

/*Returns a string which is sorted alphabetically*/
MedRepo *filterStrings(Controller *c, char substring[]);

MedRepo * filterStringsQuantity(Controller * c, int quantitylessThan, char *choice);

int FindMedicine(Controller* c, char* name, double concentration);

MedRepo * filterStringsPrice(Controller * c, double price);

int filter_price(int, int);

int addQuantity(Controller * c, char * name, double concentration, int quantity);

int undo(Controller* c);

int redo(Controller* c);