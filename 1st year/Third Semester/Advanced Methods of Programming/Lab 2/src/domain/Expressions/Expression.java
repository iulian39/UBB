package domain.Expressions;

import domain.MyDictionary;

public interface Expression {
    public int eval(MyDictionary< String, Integer > symbolTable);
}