package exception;

public class InvalidOperationException extends RuntimeException {
    public InvalidOperationException(String s) {
        super(s);
    }
}