package Repository;

import domain.PrgState;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public interface IRepo {
    public void setPrgList(List<PrgState> _prgStateList);
    public List<PrgState> getPrgList();
    public void logPrgStateExec(PrgState p) throws IOException;
}
