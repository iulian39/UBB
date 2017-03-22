#pragma once
#include "Medication.h"
#include "DynamicArray.h"

typedef struct
{
	DynamicArray *medications;

}MedRepo;

MedRepo *createRepo();

void destroyRepo(MedRepo* m);

Pharmacy *find(MedRepo *m, char *name, double concentration);

/*
	Adds a medication to the repository of medications.
	Input:	- m - pointer to the MedRepo
			- med - medication
	Output: 1 - if the medication was sucessfully added.
	2 - if the medication already exists , the concetration is modified .
*/

int add(MedRepo *m, Pharmacy *med);

/*
Deletes a medication to the repository of medications.
	Input:	- m - pointer to the MedRepo
	- name -the name of the medication
	Output: 1 - if the medication was sucessfully deleted.
	0 - if the medication could not be deleted .
*/
int delete(MedRepo *m, char *name, double concentration);
/*Updates the medication if the name and concentration exist

Returns: -1 if was succesfully updated
		-0 if couldn't be updated */
int update(MedRepo *m, char *name, double concentration, Pharmacy *med);

//Returns the length of a specific repository
int getLength(MedRepo *m);

/*
Returns the medication on the given position in the medications vector.
Input:	m - the medication repository;
pos - integer, the position;
Output: the medication on the given potision, or an "empty" medication.
*/
Pharmacy* getMedicationPosition(MedRepo* m, int pos);
MedRepo* copyRepositoy(MedRepo* a);
int quantityUP(MedRepo* m, int quantity, int poz);

void initMedRepoForTests(MedRepo *m);

void TestMedRepo();





