package domain.Expressions;

import domain.Heap;
import domain.MyDictionary;

public class NotExp implements Expression {
    private Expression exp;
    public NotExp(Expression exp) {
        this.exp = exp;
    }

    @Override
    public int eval(MyDictionary<String, Integer> symTable, Heap<Integer> heap)  {
        int x = this.exp.eval(symTable, heap);
        return x == 0 ? 1 : 0;
    }

    @Override
    public String toString() {
        return "!" + this.exp.toString();
    }
}
