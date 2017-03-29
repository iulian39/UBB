#include "movies.h"
#include <Windows.h>
#include <shellapi.h>

Movies::Movies() : title{ "" }, genre{ "" }, trailer{ "" }, year{ 0 }, likes{ 0 } {}


Movies::Movies(string title, string genre, int year, string trailer, int likes) : title{ title }, genre{ genre }, year{ year }, trailer{ trailer }, likes{ likes } {}

string Movies::getTitle() 
{
	return this->title;
}

string Movies::getGenre()
{
	return this->genre;
}

string Movies::getTrailer()
{
	return this->trailer;
}

int Movies::getYear()
{
	return this->year;
}

int Movies::getLikes()
{
	return this->likes;
}

void Movies::setTitle(string title)
{
	this->title = title;
}

void Movies::setGenre(string genre)
{
	this->genre = genre;
}

void Movies::setTrailer(string trailer)
{
	this->trailer = trailer;
}

void Movies::setYear(int year)
{
	this->year = year;
}

void Movies::setLikes(int likes)
{
	this->likes = likes;
}

void Movies::playTrailer()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
}






