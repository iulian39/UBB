package domain.Expressions;

import domain.Heap;
import domain.MyDictionary;
import exception.NotExistingException;

public class VarExpression implements Expression {
    private String varName;
    public VarExpression(String VarName) {
        this.varName = VarName;
    }

    @Override
    public int eval(MyDictionary< String, Integer > symbolTable, Heap<Integer> heap){
        if(symbolTable.containsKey(varName))
            return symbolTable.get(varName);
        throw new NotExistingException("Not Found");
    }

    @Override
    public String toString() {
        return varName;
    }
}