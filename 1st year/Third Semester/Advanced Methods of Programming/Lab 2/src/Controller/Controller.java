package Controller;

import Repository.Repo;
import domain.*;
import domain.Expressions.Expression;
import domain.Statements.CloseFileStatement;
import domain.Statements.IStatement;
import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;
import exception.NotDeclaredVariable;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller {
    private Repo repo;
    private String File;

    public Controller(Repo r) {
        this.repo = r;
    }

    public Controller(IStatement initialStatement, String File) {
        this.repo = new Repo(new PrgState(initialStatement), File);
        this.File = File;
    }

    public void executeOne() throws IOException {
        PrgState current = repo.getCurrentPrgState();
        if (!current.get_exeStack().isEmpty()) {
            IStatement s = current.get_exeStack().pop();
            s.execute(current);
            System.out.println(current);
        }

    }

    public Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet()
                .stream()
                .filter(e -> symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }


    public PrgState step(PrgState state) throws NotDeclaredVariable, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenException, IOException
    {
        IStatement cur = state.get_exeStack().pop();
        return cur.execute(state);
    }

    public void executeAll()  throws NotDeclaredVariable, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenException, IOException
    {
        try {
            PrgState current = repo.getCurrentPrgState();
            while (!current.get_exeStack().isEmpty()) {
                step(current);
                current.getHeap().setMap(conservativeGarbageCollector(
                        current.get_symbolTable().values(),
                        current.getHeap().toMap()));

                repo.logPrgStateExec();

            }
        }
        catch (Exception e) {
            System.out.println("Logging error");
            return;
        }
        finally
        {
            try {
                for(int e: repo.getCurrentPrgState().getFileTable().getAll())
                {
                    repo.getCurrentPrgState().getFileTable().get(e).getFileDescriptor().close();
                    repo.getCurrentPrgState().getFileTable().remove(e);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}
