#pragma once
#include "movies.h"
#include "DynamicVector.h"

class Repository {
	DynamicVector <Movies> list;
public:
	// c-tor for reading from a specific file, can be empty
	Repository(string fileName = "");
	// add a movie
	bool addMovie(Movies & m);
	// remove a movie
	bool removeMovie(string title, int year);
	// updates a movie
	bool updateMovie(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes);
	DynamicVector <Movies> getAll();
	int find(string name, int year);
	int getLenght();
	// saves the list of movies into a file
	void saveToFile(string fileName = "");
	
};
