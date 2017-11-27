package domain.Statements;

import domain.Expressions.Expression;
import domain.MyStack;
import domain.PrgState;

public class WhileStatement implements IStatement {
    private Expression exp;
    private IStatement stmt;

    public WhileStatement(Expression exp, IStatement stmt) {
        this.exp = exp;
        this.stmt = stmt;
    }

    @Override
    public PrgState execute(PrgState state) {
        MyStack<IStatement> exeStack = state.get_exeStack();
        if(exp.eval(state.get_symbolTable(), state.getHeap()) != 0) {
            exeStack.push(this);
            exeStack.push(stmt);
        }
        return null;
    }

    @Override
    public String toString() {
        return "while(" + this.exp.toString() + ") do " + this.stmt.toString() + " end";
    }
}
