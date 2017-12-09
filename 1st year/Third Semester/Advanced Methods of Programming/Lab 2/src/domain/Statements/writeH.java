package domain.Statements;

import domain.Expressions.Expression;
import domain.Heap;
import domain.MyDictionary;
import domain.PrgState;
import exception.InterpreterException;

public class writeH implements IStatement {
    String id;
    Expression expr;

    public writeH(String id, Expression expr) {
        this.id = id;
        this.expr = expr;
    }

    @Override
    public PrgState execute(PrgState p) {
        Heap<Integer> heap = p.getHeap();
        MyDictionary<String, Integer> symbolTable = p.get_symbolTable();

        int expRes = expr.eval(symbolTable, heap);
        if (! symbolTable.containsKey(id))
            throw new InterpreterException("The variable doesn't exist");
        int v = symbolTable.get(id);
        if(!heap.contains(v))
            throw new InterpreterException("The variable doesn't exist in the symbolTable");

        heap.update(v, expRes);
        return null;
    }

    @Override
    public String toString() {
        return "writeH(" + this.id + ", " + this.expr.toString() + ")";
    }
}
