package domain.Expressions;


import domain.Heap;
import domain.MyDictionary;
import exception.UnknownComparisonExpression;

public class BolleanExpression implements Expression {

    private String type;
    private Expression e1, e2;

    public BolleanExpression(String type, Expression e1, Expression e2) {
        this.type = type;
        this.e1 = e1;
        this.e2 = e2;
    }

    @Override
    public int eval(MyDictionary<String, Integer> symTable, Heap<Integer> heap)  {
        int val1 = this.e1.eval(symTable, heap);
        int val2 = this.e2.eval(symTable, heap);
        switch (this.type) {
            case "<":
                return val1 < val2 ? 1 : 0;
            case "<=":
                return val1 <= val2 ? 1 : 0;
            case "==":
                return val1 == val2 ? 1 : 0;
            case "!=":
                return val1 != val2 ? 1 : 0;
            case ">":
                return val1 > val2 ? 1 : 0;
            case ">=":
                return val1 >= val2 ? 1 : 0;
            default:
                throw new UnknownComparisonExpression("Unknown comparison exception: " + this.type + "\n" + "At: " + this.toString());
        }
    }

    @Override
    public String toString() {
        return this.e1.toString() + " " +  this.type + " " + this.e2.toString();
    }
}