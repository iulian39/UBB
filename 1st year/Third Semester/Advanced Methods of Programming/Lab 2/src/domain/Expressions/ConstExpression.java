package domain.Expressions;


import domain.MyDictionary;

public class ConstExpression implements Expression {
    private int constant;
    public ConstExpression(int value) {
        constant = value;
    }
    @Override
    public int eval(MyDictionary<String, Integer> symbolTable) {
        return constant;
    }
    @Override
    public String toString() {
        return "" + constant;
    }
}