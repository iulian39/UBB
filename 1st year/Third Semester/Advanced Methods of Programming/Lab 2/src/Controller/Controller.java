package Controller;

import Repository.Repo;
import domain.PrgState;
import domain.Statements.IStatement;
import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;
import exception.NotDeclaredVariable;

import java.io.IOException;

public class Controller {
    private Repo repo;

    public Controller(Repo r) {
        this.repo = r;
    }

    public Controller(IStatement initialStatement, String File) {
        this.repo = new Repo(new PrgState(initialStatement), File);
    }

    public void executeOne() throws IOException {
        PrgState current = repo.getCurrentPrgState();
        if (!current.get_exeStack().isEmpty()) {
            IStatement s = current.get_exeStack().pop();
            s.execute(current);
            System.out.println(current);
        }

    }

    public PrgState step(PrgState state) throws NotDeclaredVariable, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenException, IOException
    {
        IStatement cur = state.get_exeStack().pop();
        return cur.execute(state);
    }

    public void executeAll()  throws NotDeclaredVariable, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenException, IOException
    {
        PrgState current = repo.getCurrentPrgState();
        while(!current.get_exeStack().isEmpty()) {
            step(current);
            try {
                repo.logPrgStateExec();
            } catch (Exception e) {
                System.out.println("Logging error");
                return ;
            }
        }
    }
}