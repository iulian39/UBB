#include "repository.h"
#include <algorithm>
#include <fstream>
#include <cassert>
#include <sstream>
#include <string>
using namespace std;



Repository::Repository(string fileName) 
{
	ifstream fin(fileName.c_str());
	string line;
	while (getline(fin, line) && line != "")
	{
		istringstream iss(line);
		string token;
		DynamicVector<string> s;
		while (std::getline(iss, token, ','))
		{
			s.push_back(token);
		}
		Movies x(s[0], s[1], stoi(s[2]), s[3], stoi(s[4]));
		this->addMovie(x);
	}
	fin.close();
}

void Repository::saveToFile(string fileName)
{
	ofstream fout(fileName.c_str());
	for (int i = 0; i < this->list.size(); ++i)
	{
		Movies it = this->list[i];
		fout << it.getTitle() << "," <<
			it.getGenre() << "," <<
			to_string(it.getYear()) << "," <<
			it.getTrailer() << "," <<
			to_string(it.getLikes()) << '\n';
	}

}

bool Repository::addMovie(Movies & m) 
{
	if (find(m.getTitle(), m.getYear()) == -1)
	{
		this->list.push_back(m);
		return true;
	}
	return false;
	
}

bool Repository::removeMovie(string title, int year) 
{
	for (int i = 0; i < this->list.size(); ++i)
	{
		if (title.compare(this->list[i].getTitle()) == 0 && this->list[i].getYear() == year)
		{
			this->list.erase(i);
			return true;
		}
	}
	return false;
}

bool Repository::updateMovie(string title, int yearOLD, string newTitle, string genre, int year, string trailer, int likes ) 
{
	if (this->list.size() == 0)
		return false;
	for (int i = 0; i < this->list.size(); ++i)
		if (this->list[i].getTitle().compare(title) == 0 && this->list[i].getYear() == yearOLD)
		{
			this->list[i].setGenre(genre);
			this->list[i].setLikes(likes);
			this->list[i].setTitle(newTitle);
			this->list[i].setTrailer(trailer);
			this->list[i].setYear(year);
			return true;
		}
	return false;
}

DynamicVector<Movies> Repository::getAll()
{
	return this->list;
}

int Repository::find(string name, int year)
{
	for (int i = 0; i < list.size(); i++)
		if (name.compare(this->list[i].getTitle()) == 0 && year == this->list[i].getYear())
			return i;
	return -1;
}

int Repository::getLenght()
{
	return this->list.size();
}

