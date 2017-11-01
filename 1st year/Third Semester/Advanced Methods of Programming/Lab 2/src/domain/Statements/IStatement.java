package domain.Statements;

import domain.PrgState;

public interface IStatement {
    public PrgState execute(PrgState p);
}