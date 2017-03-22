#pragma once
#include "Medication.h"
#include "DynamicArray.h"
#include <string.h>

typedef struct
{
	Pharmacy* medication;
	char* operationType;
} Operation;

Operation* createOperation(Pharmacy* p, char* operationType);
void destroyOperation(Operation* o);
Operation* copyOperation(Operation* o);
char* getOperationType(Operation* o);
Pharmacy* getMedication(Operation* o);

// ---------------------------------------------------------------
typedef struct
{
	Operation* operations[100];
	int length;
} OperationsStack;

OperationsStack* createStack();
void destroyStack(OperationsStack* s);
void push(OperationsStack* s, Operation* o);
Operation* pop(OperationsStack* s);
int isEmpty(OperationsStack* s);
int isFull(OperationsStack* s);

void testsStack();