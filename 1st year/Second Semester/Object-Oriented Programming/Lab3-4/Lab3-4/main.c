#include "MedRepo.h"
#include "UI.h"
#include <crtdbg.h>

int main()
{
	TestMedRepo();

	MedRepo *repo = createRepo();
	OperationsStack* UndoStack = createStack();
	OperationsStack* RedoStack = createStack();
	CopyLists* undo = createStackB();
	CopyLists* redo = createStackB();
	Controller *ctrl = createController(repo, UndoStack, RedoStack, undo, redo);

	addMedication(ctrl, "Stugeron", 2.2, 20, 12);
	addMedication(ctrl, "Paracetanol Sinus", 3.2, 130, 9);
	addMedication(ctrl, "Paracetanol", 3.9, 15, 12);
	addMedication(ctrl, "Panadol", 1.5, 20, 15);
	addMedication(ctrl, "Panadol", 0.8, 12, 12);
	addMedication(ctrl, "Panadol", 5, 12, 12);
	addMedication(ctrl, "Panadol", 4.75, 12, 12);
	addMedication(ctrl, "Algocalmin", 4.5, 22, 10);
	addMedication(ctrl, "Algocalmin", 7.47, 22, 10);

	UI *ui = createUI(ctrl);

	startUI(ui);
	destroyUI(ui);
	

	_CrtDumpMemoryLeaks();

	return 0;


}