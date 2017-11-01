package Repository;
import Model.Vehicle;

public interface InterfaceRepository
{
    public void add(Vehicle NewVehicle) throws AddItemException;
    public void remove(Vehicle V);
    public void update(Vehicle V, Vehicle NewV);
    public Vehicle[] getAll();

}