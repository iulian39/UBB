package domain;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class MyStack<T> {
    private Deque<T> _stack;

    public MyStack(){
        this._stack = new ArrayDeque<>();
    }

    public MyStack(Deque<T> s)
    {
        this._stack = s;
    }

    public void push(T el) {
        this._stack.push(el);
    }

    public T pop() {
        return this._stack.pop();
    }

    public boolean isEmpty() {
        return this._stack.isEmpty();
    }

    @Override
    public String toString() {
        StringBuffer buff = new StringBuffer();
        for ( T i : _stack)
        {
            buff.append(i);
            buff.append(" ");
        }
        return buff.toString();
    }
}
