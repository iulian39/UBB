#define _CRT_SECURE_NO_WARNINGS
#include "UndoBonus.h"
#include <string.h>
#include <stdlib.h>
#include <assert.h>


CopyLists* createStackB()
{
	CopyLists* s = (CopyLists*)malloc(sizeof(CopyLists));
	s->length = 0;

	return s;
}


void destroyStackB(CopyLists* s)
{
	if (s == NULL )
		return;

	// first deallocate memory of operations (this is allocated when a new operation is pushed onto the stack)
	for (int i = 0; i < s->length; i++)
		destroyRepo(s->lists[i]);

	// then free the stack
	free(s);
}


void pushB(CopyLists* s, MedRepo* o)
{
	if (isFull(s))
		return;

	s->lists[s->length++] = copyRepositoy(o);	// copies of operations are added, such that the stask manages its own operations
}

MedRepo* popB(CopyLists* s)
{
	if (isEmpty(s))
		return NULL;
	s->length--;
	return s->lists[s->length];
}

int isEmptyB(CopyLists* s)
{
	return (s->length == 0);
}

int isFullB(CopyLists* s)
{
	return s->length == 100;
}
