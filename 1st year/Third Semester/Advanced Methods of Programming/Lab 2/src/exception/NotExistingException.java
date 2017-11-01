package exception;

public class NotExistingException extends RuntimeException {
    public NotExistingException(String s) {
        super(s);
    }
}