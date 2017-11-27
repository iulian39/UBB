package domain.Expressions;

import domain.Heap;
import domain.MyDictionary;
import exception.DivideByZeroException;
import exception.InvalidOperationException;
import exception.NotDeclaredVariable;

public class ArithmeticExpression implements Expression {
    private char operator;
    private Expression left, right;
    public ArithmeticExpression (char op, Expression left, Expression right){
        this.operator = op;
        this.left = left;
        this.right = right;
    }

    @Override

    public int eval(MyDictionary<String, Integer> symbolTable, Heap<Integer> heap)
    {
        int left = this.left.eval(symbolTable, heap);
        int right = this.right.eval(symbolTable, heap);
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
