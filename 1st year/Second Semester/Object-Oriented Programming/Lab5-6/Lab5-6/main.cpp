#include <iostream>
#include "repository.h"
#include "controller.h"
#include "ui.h"
#include "Tests.h"


using namespace std;

int main() 
{
	Tester a;


	Repository x("movies.csv");
	Repository z("watchList.csv");
	Controller y(x, z);
	UI u(y);
	u.run();


	return 0;
}