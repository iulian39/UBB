package Repository;

import domain.PrgState;
import domain.Statements.IStatement;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repo implements IRepo {

    private List<PrgState> _prgStateList;
    private String logFile;

    public Repo(PrgState state, String logFile)
    {
        this._prgStateList = new ArrayList<>();
        this._prgStateList.add(state);
        this.logFile = logFile;
    }

    public Repo(PrgState state)
    {
        this._prgStateList = new ArrayList<>();
        this._prgStateList.add(state);
    }

    public void setPrgList(List<PrgState> _prgStateList) {
        this._prgStateList = _prgStateList;
    }

    public List<PrgState> getPrgList() {
        return _prgStateList;
    }

    @Override
    public void logPrgStateExec(PrgState p) throws IOException {
        PrintWriter printWriter = new PrintWriter(new FileWriter(this.logFile, true));

        printWriter.println("Id:");
        printWriter.println(p.getId());
        printWriter.println("ExeStack:");
        printWriter.println(p.get_exeStack().toString());
        printWriter.println("SymTable:");
        printWriter.println(p.get_symbolTable().toString());
        printWriter.println("Message:");
        printWriter.println(p.get_messages().toString());
        printWriter.println("Heap:");
        printWriter.println(p.getHeap().toString());
        printWriter.println("FileTable:");
        printWriter.println(p.getFileTable().toString());
        printWriter.println();

        printWriter.close();
    }
}
