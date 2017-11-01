package Controller;

import Repository.Repository;
import Model.Vehicle;

public class Controller
{
    private Repository repo;

    public Controller(Repository repo)
    {
        this.repo = repo;
    }

    public void add(Vehicle NewVehicle)
    {
        try{
            repo.add(NewVehicle);
        }
        catch (Exception e) {
            System.err.println("Caught Exception: " + e.getMessage());
        }

    }

    public void remove(Vehicle V)
    {
        repo.remove(V);
    }

    public void update(Vehicle V, Vehicle NewV)
    {
        repo.update(V, NewV);
    }

    public Vehicle[] getAll()
    {
        return repo.getAll();
    }

}