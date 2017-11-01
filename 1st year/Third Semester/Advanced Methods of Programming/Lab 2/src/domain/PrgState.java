package domain;

import domain.Statements.IStatement;

import java.util.List;

public class PrgState {
    private MyDictionary<String, Integer> _symbolTable;
    private MyStack<IStatement> _exeStack;
    private MyList<Integer> _messages;
    private IStatement _stmt;

    public PrgState(MyStack<IStatement> exeStack, MyDictionary<String, Integer> symTable, MyList<Integer> list, IStatement stmt) {
        this._exeStack = exeStack;
        this._symbolTable = symTable;
        this._messages = list;
        this._stmt = stmt;
    }


    public boolean isStackEmpty()
    {
        return this._exeStack.isEmpty();
    }

    public MyDictionary<String, Integer> get_symbolTable() {
        return _symbolTable;
    }

    public MyStack<IStatement> get_exeStack() {
        return _exeStack;
    }

    public MyList<Integer> get_messages() {
        return _messages;
    }

    public IStatement get_stmt() {
        return _stmt;
    }

    public void set_symbolTable(MyDictionary<String, Integer> _symbolTable) {
        this._symbolTable = _symbolTable;
    }

    public void set_exeStack(MyStack<IStatement> _exeStack) {
        this._exeStack = _exeStack;
    }

    public void set_messages(MyList<Integer> _messages) {
        this._messages = _messages;
    }

    public void set_stmt(IStatement _stmt) {
        this._stmt = _stmt;
    }

    @Override
    public String toString() {
        StringBuffer buff = new StringBuffer();

        buff.append("Exe stack\n");
        buff.append(_exeStack);
        buff.append("\nSymbol Table\n");
        buff.append(_symbolTable);
        buff.append("\nMessages\n");
        buff.append(_messages);
        buff.append("\nStatement\n");
        buff.append(_stmt);
        buff.append("\n---------------\n");

        return buff.toString();
    }

}
