package domain.Statements;

import domain.Expressions.Expression;
import domain.Expressions.NotExp;
import domain.PrgState;

public class RepeatStmt implements IStatement {
    private IStatement stmt;
    private Expression exp;

    public RepeatStmt(IStatement stmt, Expression exp) {
        this.stmt = stmt;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) {
        IStatement s = new CompoundStatement(stmt, new WhileStatement(new NotExp(this.exp), stmt));
        state.get_exeStack().push(s);
        return null;
    }

    @Override
    public String toString() {
        return "repeat " + this.stmt.toString() + " until " + this.exp.toString();
    }
}
