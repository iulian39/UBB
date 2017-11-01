package domain.Expressions;

import domain.MyDictionary;
import exception.DivideByZeroException;
import exception.InvalidOperationException;

public class ArithmeticExpression implements Expression {
    private char operator;
    private Expression left, right;
    public ArithmeticExpression (char op, Expression left, Expression right){
        this.operator = op;
        this.left = left;
        this.right = right;
    }

    @Override
    public int eval(MyDictionary<String, Integer> symbolTable) {
        int left = this.left.eval(symbolTable);
        int right = this.right.eval(symbolTable);
        switch(operator){
            case '+':
                return left+right;
            case '-':
                return left-right;
            case '*':
                return left*right;
            case '/':
                if (right == 0)
                    throw new DivideByZeroException("Divide by zero : " + this.toString());
                return left/right;
            default :
                throw new InvalidOperationException("Invalid operation : " + this.toString());
        }
    }

    @Override
    public String toString() {
        return left.toString() + " " +operator + " " + right.toString();
    }
}
