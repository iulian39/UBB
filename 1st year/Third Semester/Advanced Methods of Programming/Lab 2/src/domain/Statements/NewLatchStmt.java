package domain.Statements;

import domain.Expressions.Expression;
import domain.PrgState;

public class NewLatchStmt implements IStatement {
    private static int newfreelocation = 0;

    private String var;
    private Expression exp;

    public NewLatchStmt(String var, Expression exp) {
        this.var = var;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) {
        int number = this.exp.eval(state.get_symbolTable(), state.getHeap());
        
        synchronized (state.getLatchTable()) {

            state.getLatchTable().put(newfreelocation, number);
            state.get_symbolTable().put(this.var, newfreelocation); // put method suits both cases
            ++ newfreelocation;
        }

        return null;
    }

    @Override
    public String toString() {
        return "newLatch(" + this.var + ", " + this.exp.toString() + ")";
    }
}
