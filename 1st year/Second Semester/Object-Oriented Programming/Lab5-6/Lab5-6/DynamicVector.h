#pragma once
#define DEFLENGTH 100

template <typename  TElement>
class DynamicVector
{
	TElement *elems;
	int capacity, lenght;
public:
	/* Default constructor */
	DynamicVector();
	/* Resize the vector */
	void resize();
	/* Puts an element into the list */
	void push_back(TElement elem);
	/* Erases an element from the list */
	void erase(int pos);
	/* Returns the size of the list*/
	int size();
	/* Checks if the position is valide */
	void validatePosition(int position);
	/* Assignment operator for a DynamicVector */
	DynamicVector<TElement>& operator =(const DynamicVector<TElement>& v);
	/* Position operator */
	TElement & operator[](int pos);
	TElement * getArray();
	int find(TElement elem);
private:
	/* Returns the capacity of the list*/
	int getCapacity();
	void setLenght(int len);
	//void setCapacity(int capacity);
};

template<typename TElement>
inline DynamicVector<TElement>::DynamicVector()
{
	this->lenght = 0;
	this->capacity = DEFLENGTH;
	this->elems = new TElement[DEFLENGTH];
}


template<typename TElement>
inline void DynamicVector<TElement>::resize()
{
	this->capacity *= 2;

	TElement *newElems = new TElement[this->capacity];
	for (int i = 0; i < this->lenght; i++)
		newElems[i] = this->elems[i];

	delete[] this->elems;
	this->elems = newElems;
}

template<typename TElement>
inline void DynamicVector<TElement>::push_back(TElement elem)
{
	if (this->lenght == this->capacity)
		resize();

	this->elems[this->lenght] = elem;

	this->lenght++;
}

template<typename TElement>
inline void DynamicVector<TElement>::erase(int pos)
{
	this->validatePosition(pos);
	for (int i = pos; i < this->lenght; i++)
		this->elems[i] = this->elems[i + 1];

	this->lenght--;
}

template<typename TElement>
inline int DynamicVector<TElement>::size()
{
	return this->lenght;
}


template<typename TElement>
inline int DynamicVector<TElement>::getCapacity()
{
	return this->capacity;
}

template<typename TElement>
inline void DynamicVector<TElement>::setLenght(int len)
{
	if (len > this->capacity)
		this->capacity += len;
	this->lenght = len;
}



template<typename TElement>
inline void DynamicVector<TElement>::validatePosition(int position)
{
	if (position < 0 || position >= this->lenght)
		throw("Invalid position");
}




template<typename TElement>
inline DynamicVector<TElement>& DynamicVector<TElement>::operator=(const DynamicVector<TElement>& v)
{
	if (this == &v)
		return *this;

	this->lenght = v.lenght;
	this->capacity = v.capacity;

	delete[] this->elems;
	this->elems = new TElement[this->lenght];
	for (int i = 0; i < this->lenght; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

template<typename TElement>
inline TElement & DynamicVector<TElement>::operator[](int pos)
{
	this->validatePosition(pos);	
	return this->elems[pos];
}

template<typename TElement>
inline TElement * DynamicVector<TElement>::getArray()
{
	return this->elems;
}

template<typename TElement>
inline int DynamicVector<TElement>::find(TElement elem)
{
	for (int i = 0; i < this->lenght; i++)
		if (this->elems[i] == elem)
			return i;
	return -1;
}

