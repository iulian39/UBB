package Repository;

import domain.PrgState;

import java.io.IOException;
import java.util.List;

public interface IRepo {
    public PrgState getCurrentPrgState();
    public void logPrgStateExec() throws IOException;
}
