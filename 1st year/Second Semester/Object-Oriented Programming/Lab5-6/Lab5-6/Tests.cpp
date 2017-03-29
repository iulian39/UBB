#include "Tests.h"
#include "DynamicVector.h"
#include "movies.h"
#include "controller.h"
#include "repository.h"
#include <cassert>

Tester::Tester()
{
	testDynamicVector();
}

void Tester::testDynamicVector()
{
	DynamicVector <Movies> v;
	assert(v.size() == 0);
	v.push_back(Movies("12 Angry Men", "Drama", 1957, "https://www.youtube.com/watch?v=A7CBKT0PWFA",551515));
	assert(v.size() == 1);
	v.erase(0);
	assert(v.size() == 0);
	DynamicVector <Movies> v1;
	assert(v.size() == v1.size());
	v.push_back(Movies("12 Angry Men", "Drama", 1957, "https://www.youtube.com/watch?v=A7CBKT0PWFA", 551515));
	assert(v.size() > v1.size());
}

void Tester::testRepo()
{
	Repository x;
	assert(x.getLenght() == 0);
	assert(x.addMovie(Movies("12 Angry Men", "Drama", 1957, "https://www.youtube.com/watch?v=A7CBKT0PWFA", 551515)) == true);
	assert(x.getLenght() == 1);
	assert(x.addMovie(Movies("12 Angry Men", "Drama", 1957, "https://www.youtube.com/watch?v=A7CBKT0PWFA", 551515)) == false);
	assert(x.getLenght() == 1);
	assert(x.removeMovie("12 Angry Men", 1754) == false);
	assert(x.getLenght() == 1);
	assert(x.removeMovie("12 Angry Men", 1957) == true);
	assert(x.getLenght() == 0);
}
