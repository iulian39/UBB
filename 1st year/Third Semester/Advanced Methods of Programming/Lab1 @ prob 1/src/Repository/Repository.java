package Repository;

import Model.Vehicle;

public class Repository implements InterfaceRepository
{
    private Vehicle[] vehicles;
    private int size;

    public Repository()
    {
        size = 0;
        vehicles = new Vehicle[20];
    }

    @Override
    public void add(Vehicle NewVehicle) throws AddItemException
    {
        if ( size == vehicles.length )
        {
            resize();
        }
        if (NewVehicle.getColor().isEmpty())
            throw new AddItemException("The color can't be null");

        vehicles[size++] = NewVehicle;

    }

    @Override
    public void remove(Vehicle V)
    {
        for ( int i = 0; i < size; i++)
        {
            if (vehicles[i] == V)
            {
                for ( int j = i; j < size - 1; ++j)
                {
                    vehicles[j] = vehicles[j + 1];
                }
                size--;
                break;
            }
        }
    }

    private void resize()
    {
        Vehicle[] newArray = new Vehicle[size*2];

        for(int i = 0; i < size; i++)
            newArray[i] = vehicles[i];

        vehicles = newArray;

    }

    @Override
    public void update(Vehicle V, Vehicle NewV)
    {
        for ( int i = 0; i < size; i++)
        {
            if (vehicles[i] == V)
            {
                vehicles[i] = NewV;
                break;
            }
        }
    }

    @Override
    public Vehicle[] getAll()
    {
        Vehicle[] newArray = new Vehicle[size];
        for (int i = 0; i < size; ++i)
            newArray[i] = vehicles[i];
        return newArray;
    }

}