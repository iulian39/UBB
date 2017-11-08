package domain.Statements;

import domain.PrgState;

import java.io.IOException;

public interface IStatement {
    public PrgState execute(PrgState p) throws IOException;
}