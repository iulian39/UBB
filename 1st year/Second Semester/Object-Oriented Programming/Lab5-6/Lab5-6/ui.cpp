#include "ui.h"
#include "controller.h"
#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <conio.h>
using namespace std;

UI::UI(Controller(& ctrl)) : ctrl {ctrl} {}

bool UI :: readNumber(int &nr)
{
	string s;
	getline(cin, s);
	istringstream iss(s);


	if ((iss >> nr).fail())
	{
		cout << "ERROR READING NUMBER\n";
		return false;
	}
	else
		return true;
}

void UI::InitialMenu()
{
	cout << "\nChoose mode:\n";
	cout << "   1. Administrator\n";
	cout << "   2. User\n";
	cout << "   0. Exit\n";
}

void UI::run()
{

	while (true) 
	{
		this->InitialMenu();
		int op;
		cout << "Please input the command : ";
		while (readNumber(op) == false)
			readNumber(op);
		if (op == 1)
			this->_run_admin();
		else if (op == 2)
			this->_run_user();
		else if (op == 0)
			break;
		else {
			cout << "Not an option!\n";
			run();
		}
	}
}

void UI::_run_admin() 
{
	int op;
	while (true) 
	{
		this->_show_admin_menu();
		cout << "Please input the command : ";
		while (readNumber(op) == false)
			if (readNumber(op))
				break;
		switch (op) 
		{
			case 1:
			{
				this->_admin_add_movie();
				break;
			}
			case 2:
			{
				this->_admin_show_all();
				this->_admin_remove_movie();
				break;
			}
			case 3:
			{
			this->_admin_show_all();
				this->_admin_update_movie();
				break;
			}
			case 4:
			{
				this->_admin_show_all();
				break;
			}
			case 5:
			{
				this->_admin_sort();
				break;
			}
			case 0:
			{
				this->ctrl.saveToFile("movies.csv");	
				cout << "\nSuccessfully saved!\n";
				return;
			}
			default:
				cout << "Invalid operation!\n";
		}
	}
}

void UI::_admin_sort()
{
	DynamicVector <Movies> a = this->ctrl.getArray();
	if (a.size() == 0)
	{
		cout << "\nThere are no movies in the database !\n";
		return;
	}
	
	Movies aux;
	for (int i = 0; i < a.size() - 1; ++i)
		for (int j = i + 1; j < a.size(); ++j)
			if (a[i].getLikes() > a[j].getLikes())
			{
				aux = a[i];
				a[i] = a[j];
				a[j] = aux;
			}
		


	for(int i = 0; i < a.size(); ++i)
		{
			Movies it = a[i];
			cout << "Title : " << it.getTitle() << "|";
			cout << "Genre : " << it.getGenre() << "|";
			cout << "Year : " << it.getYear() << "|";
			cout << "Trailer : " << it.getTrailer() << "|";
			cout << "Likes : " << it.getLikes() << "\n";
		}
}

void UI::_run_user() 
{
	int op;
	while (true) 
	{
		_show_user_menu();
		cout << "Please input the command : ";
		while (readNumber(op) == false)
			if (readNumber(op))
				break;
		
		string genre;
		DynamicVector <Movies> u;
		Repository u1;
		switch (op) 
		{
			case 1:	
				cout << "Please input the genre : ";
				getline(cin, genre);
				u = this->ctrl.findGenre(genre);
				if (u.size() == 0)
					cout << "There are no movies with the genre : " << genre << '\n';
				else
				{
					for (int i = 0; i < u.size(); ++i)
						u1.addMovie(u[i]);
					this->printMovies(u);
				}
				break;
				
			case 2:
				this->_user_show_watchList();
				this->_user_remove_movie();
				break;
			case 3:
				this->_user_show_watchList();
				break;
			case 0:
				this->ctrl.saveToFileWL("watchList.csv");
				cout << "\nSuccessfully saved!\n";
				return;
			default:
				cout << "Not an option!\n";
		}
	}
}

void UI::printMovies(DynamicVector<Movies> u)
{
	bool ok = true;
	int i = 1;
	while (true)
	{
		system("cls");
		cout << "To exit press ESC\n";	
		cout << "Movie : " << i << " out of " << u.size();
		Movies it = u[i - 1];
		cout << "\tTitle : " << it.getTitle() << "|";
		cout << "\tGenre : " << it.getGenre() << "|";
		cout << "\tYear : " << it.getYear() << "|";
		cout << "\tTrailer : " << it.getTrailer() << "|";
		cout << "\tLikes : " << it.getLikes() << "\n";
		cout << "Use < and > to move between movies \n";

		if (this->ctrl.findWatchList(it.getTitle(), it.getYear()) == -1)
			cout << "Press SPACE to add the movie to your WATCH LIST\n";

		if(ok == true)
			it.playTrailer();
		ok = true;

		unsigned char a;
		a = _getch();

		if (a == 27)
			break;
		if (a == 32 && this->ctrl.findWatchList(it.getTitle(), it.getYear()) == -1)
		{
			this->ctrl.addMovieWatchList(it);
			ok = false;
			continue;
		}
		if (a == 75)
		{
			if (i > 1)
				i--;
			continue;
		}
		else if (a == 77)
		{
			if (i < u.size())
				i++;
			else
				i = 1;
			continue;
		}

		
	}
}

void UI::_show_user_menu() 
{
	cout << "--- User mode ---\n";
	cout << "   1. Search movies having a given genre\n";
	cout << "   2. Delete movies from Watch List\n";
	cout << "   3. Print Watch List\n";
	cout << "   0. Exit\n";
}

void UI::_show_admin_menu() 
{
	cout << "Administrator mode\n";
	cout << "   1. Add a new movie\n";
	cout << "   2. Delete a movie\n";
	cout << "   3. Update a movie\n";
	cout << "   4. Show all movies\n";
	cout << "   5. Show all movies ascending by likes\n";
	cout << "   0. Exit\n";
	cout << "\n";
}

void UI::_user_show_watchList()
{
	DynamicVector <Movies> a = this->ctrl.getArrayWL();
	if (a.size() == 0)
	{
		cout << "\nThere are no movies in the watch list !\n";
		return;
	}

	for (int i = 0; i < a.size(); ++i)
	{
		Movies it = a[i];
		cout << "Title : " << it.getTitle() << "|";
		cout << "Genre : " << it.getGenre() << "|";
		cout << "Year : " << it.getYear() << "|";
		cout << "Trailer : " << it.getTrailer() << "|";
		cout << "Likes : " << it.getLikes() << "\n";
	}
}

void UI::_admin_show_all() 
{
	DynamicVector <Movies> a = this->ctrl.getArray();
	if (a.size() == 0)
	{
		cout << "\nThere are no movies in the database !\n";
		return;
	}
	
	for (int i = 0; i < a.size() ; ++i)
	{
		Movies it = a[i];
		cout << "Title : " << it.getTitle() << "|";
		cout << "Genre : " << it.getGenre() << "|";
		cout << "Year : " << it.getYear() << "|";
		cout << "Trailer : " << it.getTrailer() << "|";
		cout << "Likes : " << it.getLikes() << "\n";
	}
}

void UI::_admin_add_movie() 
{
	string title, genre, link;
	int year, likes;
	cout << "Please input the title : ";
	getline(cin, title);
	cout << "Please input the year : ";
	while (readNumber(year) == false)
		if (readNumber(year))
			break;
	cout << "Please input the genre : ";
	getline(cin, genre);
	cout << "Please input the link : ";
	getline(cin, link);
	cout << "Please input the likes : ";
	while (readNumber(likes) == false)
		if (readNumber(likes))
			break;
	Movies x = Movies(title, genre, year, link, likes);
	bool ok = this->ctrl.addMovieController(x);
	if (ok == true)
		cout << "Movie added successfully !\n";
	else
		cout << "Movie already exists !\n";
}

void UI::_admin_remove_movie() 
{
	if (this->ctrl.getLen() == 0)
	{
		cout << "There are no movies in the list\n";
		return;
	}
	string title;
	int year;
	cout << "Please input the title : ";
	getline(cin, title);
	cout << "Please input the year : ";
	while (readNumber(year) == false)
		if (readNumber(year))
			break;
	if (this->ctrl.removeMovieController(title, year) == true)
		this->ctrl.removeMovieWatchList(title, year);
}

void UI::_user_remove_movie()
{
	if (this->ctrl.getLenWL() == 0)
	{
		cout << "There are no movies in the list\n";
		return;
	}
	string title;
	int year;
	cout << "Please input the title : ";
	getline(cin, title);
	cout << "Please input the year : ";
	while (readNumber(year) == false)
		if (readNumber(year))
			break;
	this->ctrl.removeMovieWatchList(title, year);
}

void UI::_admin_update_movie() 
{
	string title;
	int year;
	cout << "Please input the title : ";
	getline(cin, title);
	cout << "Please input the year : ";
	while (readNumber(year) == false)
		if (readNumber(year))
			break;
	if (this->ctrl.findCTRL(title, year) == -1)
	{
		cout << "The movie doesn't exist !\n";
		return;
	}
	string newTitle, genre, link;
	int yearN, likes;
	cout << "Please input the title : ";
	getline(cin, newTitle);
	cout << "Please input the year : ";
	while (readNumber(yearN) == false)
		if (readNumber(yearN))
			break;
	cout << "Please input the genre : ";
	getline(cin, genre);
	cout << "Please input the link : ";
	getline(cin, link);
	cout << "Please input the likes : ";
	while (readNumber(likes) == false)
		if (readNumber(likes))
			break;

	this->ctrl.updateMovieController(title, year, newTitle, genre, yearN, link, likes);
	this->ctrl.updateMovieWatchList(title, year, newTitle, genre, yearN, link, likes);
	cout << "Movie updated !\n";
}