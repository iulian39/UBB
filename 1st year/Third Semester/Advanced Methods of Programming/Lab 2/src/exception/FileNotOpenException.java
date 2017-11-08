package exception;

public class FileNotOpenException extends RuntimeException {
    public FileNotOpenException() { super(); }
    public FileNotOpenException(String s) { super(s); }
}