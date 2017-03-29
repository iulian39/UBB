#pragma once
#include <string>

using namespace std;

class Movies {
	string title, genre, trailer;
	int year, likes;
public:
	// Default c-tor
	Movies();
	Movies(string title, string genre, int year, string trailer, int likes = 0);
	// getters
	string getTitle();
	string getGenre();
	string getTrailer();
	int getYear();
	int getLikes();
	// setters
	void setTitle(string title);
	void setGenre(string genre);
	void setTrailer(string trailer);
	void setYear(int year);
	void setLikes(int likes);

	//Function to play the trailer into chrome.exe 
	void playTrailer();
	
};
