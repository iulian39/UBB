package domain.Statements;

import domain.Expressions.Expression;
import domain.PrgState;
import domain.Statements.IStatement;

import java.util.List;

public class PrintStatement implements IStatement {
    private Expression exp;

    public PrintStatement(Expression exp) {
        this.exp = exp;
    }

    @Override
    public String toString() {
        return "Print (" + exp + ")";
    }

    @Override
    public PrgState execute(PrgState prg) {

        int r = exp.eval(prg.get_symbolTable(), prg.getHeap());
        prg.get_messages().add(r);
        return prg;

//        MyDictionary<String, Integer> dict = prg.get_symbolTable();
//        List<Integer> list = prg.get_messages();
//
//        int res = exp.eval(dict);
//        list.add(res);
//        return prg;
    }
}
