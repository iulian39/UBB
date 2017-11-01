package Repository;

import domain.PrgState;

import java.util.ArrayList;
import java.util.List;

public class Repo implements IRepo {
    private List<PrgState> _prgStateList;

    public Repo(PrgState state)
    {
        this._prgStateList = new ArrayList<>();
        this._prgStateList.add(state);
    }

    @Override
    public PrgState getCurrentPrgState()
    {
        return _prgStateList.get(0);
    }

    @Override
    public void addPrgState(PrgState p)
    {
        this._prgStateList.add(p);
    }
}
