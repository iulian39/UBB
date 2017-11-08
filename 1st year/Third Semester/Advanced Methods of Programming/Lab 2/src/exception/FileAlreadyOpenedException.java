package exception;

public class FileAlreadyOpenedException extends RuntimeException {
    public FileAlreadyOpenedException()
    {
        super();
    }

    public FileAlreadyOpenedException(String s)
    {
        super(s);
    }
}