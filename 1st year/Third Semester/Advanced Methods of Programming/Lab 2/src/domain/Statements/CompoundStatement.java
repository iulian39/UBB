package domain.Statements;

import domain.MyStack;
import domain.PrgState;

public class CompoundStatement implements IStatement {
    private IStatement first, second;

    public CompoundStatement(IStatement first, IStatement second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public String toString() {
        return "( " + first.toString() + ", " + second.toString() + " )";
    }

    @Override
    public PrgState execute(PrgState state) {
        MyStack<IStatement> stack = state.get_exeStack();
        stack.push(second);
        stack.push(first);
        return state;
    }
}
