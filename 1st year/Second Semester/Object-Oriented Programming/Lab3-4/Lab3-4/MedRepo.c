#include "MedRepo.h"
#include "Operations.h"
#include <stddef.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

MedRepo * createRepo()
{
	MedRepo *m = (MedRepo*)malloc(sizeof(MedRepo));
	m->medications = createDynamicArray(CAPACITY);

	return m;
}	

void destroyRepo(MedRepo * v)
{
	if (v == NULL)
		return;

	// first free the memory allocated for the medications
	for (int i = 0; i < getLengthArray(v->medications); i++)
	{
		Pharmacy* p = get(v->medications, i);
		deleteMedication(p);
	}
	destroy(v->medications);
	free(v);
}


int delete(MedRepo *m, char *name, double concentration)
{
	int i,j;
	for (i = 0; i < getLengthArray(m->medications); i++)
	{
		if (strcmp(m->medications->elems[i]->name, name) == 0 && m->medications->elems[i]->concentration == concentration)
		{
			for (j = i; j < getLengthArray(m->medications); j++)
			{
				m->medications->elems[j] = m->medications->elems[j + 1];
			}
			m->medications->length--;	

			return 1;
		}
	}
	return 0;
}
Pharmacy* find(MedRepo * m, char * name, double concentration)
{
	int i = 0;
	for (i = 0; i < m->medications->length; i++)
	{
		if (strcmp(m->medications->elems[i]->name, name) == 0)
		{
			if (m->medications->elems[i]->concentration == concentration)
			{
				return m->medications->elems[i];
			}
		}
	}
	return NULL;
}

int quantityUP(MedRepo* m, int quantity, int poz)
{
	if (getMedicationPosition(m, poz) == NULL)
		return 0;
	m->medications->elems[poz]->quantity += quantity;
	return 2;
}

int add(MedRepo * m, Pharmacy * med)
{
	/*Adds a medication to the stock , and if it already exists , the concentration of the new medication is updated*/
	if (find(m, med->name, med->concentration) != NULL)
		return 0;

	m->medications->elems[m->medications->length] = med;
	m->medications->length++;
	return 1;
}


int update(MedRepo * m, char * name, double concentration, Pharmacy *med)
{
	int i;
	if (find(m, name, concentration) != NULL)
	{
		for (i = 0; i < m->medications->length; i++)
		{
			if (strcmp(m->medications->elems[i]->name, name) == 0)
			{
				if (m->medications->elems[i]->concentration == concentration)
				{
					m->medications->elems[i] = med;
					return 1;
				}
			}
		}
	}
	return 0;
}

MedRepo* copyRepositoy(MedRepo* a)
{
	int i;
	MedRepo* c = createRepo();
	for (i = 0; i < a->medications->length; ++i)
	{
		Pharmacy* d = copyMedication(a->medications->elems[i]);
		add(c, d);
	}
	return c;
}

int getLength(MedRepo * m)
{
	return m->medications->length;
}

Pharmacy * getMedicationPosition(MedRepo * m, int pos)
{
	if (pos<0 || pos > m->medications->length)
	{
		return NULL;
	}
	return m->medications->elems[pos];

}

void initMedRepoForTests(MedRepo * m)
{
	Pharmacy *med = createMedication("Paramol", 3.20, 50, 8);
	add(m, med);
}

void testAdd()
{
	MedRepo *m = createRepo();
	initMedRepoForTests(m);

	Pharmacy *med = createMedication("Nurofen", 2.2, 20, 15);
	assert(add(m, med) == 1);

	Pharmacy *med2 = createMedication("Nurofen", 2.4, 20, 15);
	assert(add(m, med2) == 1);

	destroyRepo(m);
}

void testDelet()
{
	MedRepo *m = createRepo();
	initMedRepoForTests(m);
	assert(delete(m, "ye", 5) == 0);


	assert(delete(m, "Paramol", 3.2) == 1);

}

void testUpdate()
{
	MedRepo *m = createRepo();
	initMedRepoForTests(m);
	Pharmacy *med2 = createMedication("Nurofen", 2.4, 20, 15);
	assert(update(m, "dada", 78, med2) == 0);
}

void TestMedRepo()
{
	testAdd();
	testDelet();
	testUpdate();
}

