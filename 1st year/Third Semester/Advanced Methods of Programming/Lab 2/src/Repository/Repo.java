package Repository;

import domain.PrgState;
import domain.Statements.IStatement;

import java.io.*;
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

    @Override
    public void serialize() {

        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("serialize.txt"))){

            out.write(this._prgStateList.size());
            for(PrgState t : this._prgStateList)
                out.writeObject(t);
        } catch (IOException e) {
            System.out.println("IOError\nError: " + e.toString());
        }
    }

    @Override
    public void deserialize() {

        PrgState state = null;
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("serialize.txt")) ){

            int size = in.read();
            this._prgStateList.clear();
            for(int i = 0; i < size; ++ i)
                this._prgStateList.add((PrgState) in.readObject());
        } catch(IOException e) {
            System.out.println("IOError\nError: " + e.toString());
        } catch(ClassNotFoundException e) {
            System.out.println("ClassNotFoundException\nError: " + e.toString());
        }
    }

}
