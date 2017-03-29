#pragma once
#include "controller.h"
#include "movies.h"


class UI {
	Controller ctrl;
public:
	UI(Controller(& ctrl));
	void run();
private:
	void _run_admin();
	void _admin_sort();
	void _run_user();
	void printMovies(DynamicVector<Movies> u);
	void _show_user_menu();
	void _show_admin_menu();
	void _user_show_watchList();
	void _admin_show_all();
	bool readNumber(int &nr);
	void InitialMenu();

	void _admin_add_movie();

	void _admin_remove_movie();

	void _user_remove_movie();

	void _admin_update_movie();

};