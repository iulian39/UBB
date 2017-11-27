package domain.Expressions;

import domain.Heap;
import domain.MyDictionary;

public interface Expression {
    public int eval(MyDictionary<String, Integer> symTable, Heap<Integer> heap);
}