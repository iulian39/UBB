package domain.Statements;

import domain.PrgState;
import exception.NotDeclaredVariable;

public class AwaitStmt implements IStatement {

    private String var;

    public AwaitStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) {
        if(state.get_symbolTable().get(var) == null)
            throw new NotDeclaredVariable("AwaitStmt : No variable: " + this.var);

        int index = state.get_symbolTable().get(var);

        synchronized (state.getLatchTable()) {
            if (state.getLatchTable().get(index) == null)
                throw new NotDeclaredVariable("AwaitStmt : No latch index: " + index );

            if(state.getLatchTable().get(index) > 0)
                state.get_exeStack().push(this);
        }
        return null;
    }
    @Override
    public String toString() {
        return "await(" + this.var + ")";
    }
}