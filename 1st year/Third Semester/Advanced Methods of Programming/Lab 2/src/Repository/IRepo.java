package Repository;

import domain.PrgState;

import java.util.List;

public interface IRepo {
    public void addPrgState(PrgState p);
    public PrgState getCurrentPrgState();
}
