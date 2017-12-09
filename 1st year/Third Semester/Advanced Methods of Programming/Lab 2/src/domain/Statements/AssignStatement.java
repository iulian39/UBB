package domain.Statements;

import domain.Expressions.Expression;
import domain.MyDictionary;
import domain.PrgState;

public class AssignStatement implements IStatement {
    private String varName;
    private Expression expr;

    public AssignStatement(String v, Expression e) {
        varName = v;
        expr = e;
    }

    @Override
    public PrgState execute(PrgState state) {
        MyDictionary<String, Integer> symTable = state.get_symbolTable();
        symTable.put(this.varName, this.expr.eval(symTable, state.getHeap()));
        return null;
    }

    @Override
    public String toString()
    {
        return this.varName + '=' + this.expr;
    }

}