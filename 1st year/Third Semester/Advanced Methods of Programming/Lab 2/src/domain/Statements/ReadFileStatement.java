package domain.Statements;

import domain.Expressions.Expression;
import domain.FileData;
import domain.PrgState;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;

import java.io.IOException;

public class ReadFileStatement implements IStatement {
    private Expression expression;
    private String var;

    public ReadFileStatement(Expression exp, String var) {
        this.expression = exp;
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenException {
        int fd = this.expression.eval(state.get_symbolTable(), state.getHeap());

        FileData br = state.getFileData(fd);
        if (br == null)
            throw new FileNotOpenException("FileNotOpenedException at: " + this.toString() + "\nNo such file descriptor: " + String.valueOf(fd));

        String line = br.getFileDescriptor().readLine();
        int val = 0;
        if(line != null)
            val = Integer.valueOf(line);
        state.get_symbolTable().put(this.var, val);
        return null;
    }

    @Override
    public String toString() {
        return "ReadFileStatement (" + this.expression.toString() + ", " + this.var + ")";
    }
}