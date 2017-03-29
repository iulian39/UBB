#pragma once
#include "repository.h"


class Controller {
	Repository repo;
	Repository watchList;
public:
	/* constructor */
	Controller(Repository & repo, Repository & watchList);
	/* Method to return the Repository*/
	Repository getRepo(); 
	/* Method to add a movie to the Repository*/
	bool addMovieController(Movies m);
	/* Method to add a movie to the Watch List*/
	bool addMovieWatchList(Movies m);
	/* Method to remove a movie to the Watch List*/
	bool removeMovieWatchList(string title, int year);
	/* Method to remove a movie to the Repository*/
	bool removeMovieController(string title, int year);
	/* Method to update a movie to the Repository*/
	bool updateMovieController(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes);
	/* Method to update a movie to the Watch List*/
	bool updateMovieWatchList(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes);
	DynamicVector <Movies> &  getArray();
	DynamicVector<Movies>& getArrayWL();
	int findCTRL(string title, int year);
	int findWatchList(string title, int year);
	DynamicVector <Movies> findGenre(string genre);
	int getLen();
	int getLenWL();
	void saveToFile(string filename);

	void saveToFileWL(string filename);
	
};

