package domain.Statements;

import domain.Expressions.Expression;
import domain.Heap;
import domain.IdGenerator;
import domain.MyDictionary;
import domain.PrgState;



public class newH implements IStatement{
    private String nrx;
    private Expression exp;

    public newH(String s, Expression e)
    {
        nrx = s;
        exp = e;
    }

    @Override
    public PrgState execute(PrgState p) {
        Heap<Integer> h = p.getHeap();
        MyDictionary<String, Integer> sym = p.get_symbolTable();

        int expRes = exp.eval(sym, h);
        int addr = IdGenerator.generateId();

        h.add(addr, expRes);

        if (sym.containsKey(nrx)) {
            sym.update(nrx, addr);
        }
        else
        {
            sym.put(nrx, addr);
        }

        return p;
    }

    @Override
    public String toString() {
        return "newH(" + this.nrx + ", " + this.exp.toString() + ")";
    }
}
