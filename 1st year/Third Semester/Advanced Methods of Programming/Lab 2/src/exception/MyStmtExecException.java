package exception;

public class MyStmtExecException extends RuntimeException {
    public MyStmtExecException() {
        super();
    }

    public MyStmtExecException(String s) {
        super(s);
    }
}