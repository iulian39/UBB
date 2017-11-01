package exception;

public class DivideByZeroException extends RuntimeException {
    public DivideByZeroException(String s) {
        super(s);
    }
}