package domain.Statements;

import domain.Expressions.Expression;
import domain.PrgState;

public class IfStatement implements IStatement {
    private Expression exp;
    private IStatement thenS;
    private IStatement elseS;

    public IfStatement(Expression exp, IStatement thenS, IStatement elseS) {
        this.exp = exp;
        this.thenS = thenS;
        this.elseS = elseS;
    }

    @Override
    public String toString() {
        return "If " + exp.toString() + " then " + thenS.toString() + " else " + elseS.toString();
    }

    @Override
    public PrgState execute(PrgState state) {
        if(exp.eval(state.get_symbolTable()) == 0)
            state.get_exeStack().push(elseS);
        else
            state.get_exeStack().push(thenS);
        return state;
    }
}