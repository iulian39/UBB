package Controller;

import Repository.Repo;
import domain.MyStack;
import domain.PrgState;
import domain.Statements.IStatement;

public class Controller {
    private Repo repo;

    public Controller(Repo r) {
        this.repo = r;
    }

    public void executeOne() {
        PrgState current = repo.getCurrentPrgState();
        if (!current.get_exeStack().isEmpty()) {
            IStatement s = current.get_exeStack().pop();
            s.execute(current);
            System.out.println(current);
        }

    }

    public void executeAll() {
        PrgState current = repo.getCurrentPrgState();
        while (!current.get_exeStack().isEmpty())
            executeOne();
    }
}