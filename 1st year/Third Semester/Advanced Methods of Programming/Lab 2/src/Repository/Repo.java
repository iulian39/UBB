package Repository;

import domain.PrgState;
import domain.Statements.IStatement;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repo implements IRepo {
    private PrgState _prgStateList;
    private String logFile;

    public Repo(PrgState state, String logFile)
    {
        this._prgStateList = state;
        this.logFile = logFile;
    }

    @Override
    public PrgState getCurrentPrgState()
    {
        return _prgStateList;
    }


    @Override
    public void logPrgStateExec() throws IOException {
        PrintWriter printWriter = new PrintWriter(new FileWriter(this.logFile, true));

        printWriter.println("ExeStack:");
        printWriter.println(this._prgStateList.get_exeStack().toString());
        printWriter.println("SymTable:");
        printWriter.println(this._prgStateList.get_symbolTable().toString());
        printWriter.println("Message:");
        printWriter.println(this._prgStateList.get_messages().toString());
        printWriter.println("Heap:");
        printWriter.println(this._prgStateList.getHeap().toString());
        printWriter.println("FileTable:");
        printWriter.println(this._prgStateList.getFileTable().toString());
        printWriter.println();

        printWriter.close();
    }
}
