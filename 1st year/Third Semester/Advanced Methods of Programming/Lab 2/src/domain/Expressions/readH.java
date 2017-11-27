package domain.Expressions;

import domain.Heap;
import domain.MyDictionary;
import exception.InterpreterException;

public class readH implements Expression {
    String id;

    public readH(String id) {
        this.id = id;
    }

    @Override
    public int eval(MyDictionary<String, Integer> symTable, Heap<Integer> heap){
        if (! symTable.containsKey(id))
            throw new InterpreterException("The variable doesn't exist");
        int v = symTable.get(id);
        if(!heap.contains(v))
            throw new InterpreterException("The variable doesn't exist in the symbolTable");

        return heap.get(v);
    }

    @Override
    public String toString() {
        return "readH(" + id + ")";
    }
}