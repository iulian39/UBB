#include "controller.h"

Controller::Controller(Repository & repo, Repository & watchList) :repo { repo }, watchList{ watchList } {}

Repository Controller::getRepo()
{
	return repo;
}

bool Controller::addMovieController(Movies m)
{
	bool ok = this->repo.addMovie(m);
	return ok;
}

bool Controller::addMovieWatchList(Movies m)
{
	bool ok = this->watchList.addMovie(m);
	return ok;
}

bool Controller::removeMovieWatchList(string title, int year)
{
	bool result = this->watchList.removeMovie(title, year);
	return result;
}

bool Controller::removeMovieController(string title, int year)
{
	bool result = this->repo.removeMovie(title, year);
	return result;
}

bool Controller::updateMovieController(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes)
{
	bool result = this->repo.updateMovie(title, yearOLD, newTitle, genre, year, trailer, likes);
	return result;
}

bool Controller::updateMovieWatchList(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes)
{
	bool result = this->repo.updateMovie(title, yearOLD, newTitle, genre, year, trailer, likes);
	return result;
}

DynamicVector <Movies> & Controller::getArray()
{
	return this->repo.getAll();
}

DynamicVector <Movies> & Controller::getArrayWL()
{
	return this->watchList.getAll();
}

int Controller::findCTRL(string title, int year)
{
	return this->repo.find(title, year);
}

int Controller::findWatchList(string title, int year)
{
	return this->watchList.find(title, year);
}

DynamicVector<Movies> Controller::findGenre(string genre)
{
	DynamicVector<Movies> u, u2;
	u2 = this->repo.getAll();
	if (genre.compare("") == 0)
		return u2;
	for (int i = 0; i < u2.size(); ++i)
		if (genre.compare(u2[i].getGenre()) == 0)
			u.push_back(u2[i]);

	return u;
}

int Controller::getLen()
{
	return this->repo.getLenght();
}

int Controller::getLenWL()
{
	return this->watchList.getLenght();
}

void Controller::saveToFile(string filename)
{
	this->repo.saveToFile(filename);
}

void Controller::saveToFileWL(string filename)
{
	this->watchList.saveToFile(filename);
}