package exception;

public class NotDeclaredVariable extends RuntimeException {
    public NotDeclaredVariable() { super(); }
    public NotDeclaredVariable(String s) { super(s); }
}