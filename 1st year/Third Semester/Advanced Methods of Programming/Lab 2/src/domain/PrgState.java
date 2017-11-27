package domain;

import domain.Statements.IStatement;


public class PrgState {
    private MyDictionary<String, Integer> _symbolTable;
    private MyStack<IStatement> _exeStack;
    private MyList<Integer> _messages;
    private IStatement _stmt;
    private FileTable<Integer,  FileData> fileTable;
    private Heap<Integer> heap;

    public PrgState(MyStack<IStatement> exeStack, MyDictionary<String, Integer> symTable, MyList<Integer> list, IStatement stmt, FileTable<Integer,  FileData> fileTable, Heap<Integer> heap) {
        this._exeStack = exeStack;
        this._symbolTable = symTable;
        this._messages = list;
        this._stmt = stmt;
        this.fileTable = fileTable;
        this.heap = heap;
    }

    public PrgState(IStatement prg) {
        this._exeStack = new MyStack<>();
        this._symbolTable = new MyDictionary<>();
        this._messages = new MyList<>();
        this.fileTable = new FileTable<>();
        this.heap = new Heap<>();
        this._exeStack.push(prg);
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

    public FileTable<Integer, FileData> getFileTable() {
        return fileTable;
    }

    public FileData getFileData(int nr) {
        return fileTable.get(nr);
    }

    public void setFileTable(FileTable<Integer, FileData> fileTable) {
        this.fileTable = fileTable;
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

    public Heap<Integer> getHeap() {
        return heap;
    }

    public void setHeap(Heap<Integer> heap) {
        this.heap = heap;
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
        buff.append("\nHeap\n");
        buff.append(heap.toString());
        buff.append("\n---------------\n");

        return buff.toString();
    }

}
