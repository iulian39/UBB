package domain.Statements;

import domain.PrgState;
import exception.NotDeclaredVariable;

public class CountDownStmt implements IStatement {
    private String var;

    public CountDownStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) {

        if(state.get_symbolTable().get(this.var) == null)
            throw new NotDeclaredVariable("CountDownStmt : No variable " + this.var);

        int index = state.get_symbolTable().get(this.var);

        synchronized (state.getLatchTable()) {
            if (state.getLatchTable().get(index) == null)
                return null;

            int count = state.getLatchTable().get(index);
            if (count > 0) {
                state.getLatchTable().put(index, count - 1);
                state.get_messages().add(state.getId()); // writing the id
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "countDown(" + this.var + ")";
    }
}