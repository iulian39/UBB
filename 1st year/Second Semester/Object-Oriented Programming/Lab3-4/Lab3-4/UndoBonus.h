#pragma once
#include "MedRepo.h"
#include "DynamicArray.h"
#include <string.h>

typedef struct
{
	MedRepo* lists[100];
	int length;
} CopyLists;


CopyLists* createStackB();
void destroyStackB(CopyLists* s);
void pushB(CopyLists* s, MedRepo* o);
MedRepo* popB(CopyLists* s);
int isEmptyB(CopyLists* s);
int isFullB(CopyLists* s);
MedRepo* copyListOfMedications(MedRepo* o);
