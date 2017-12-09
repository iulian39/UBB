package domain.Statements;

import domain.Expressions.Expression;
import domain.FileData;
import domain.FileTable;
import domain.PrgState;
import exception.FileNotOpenException;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseFileStatement implements IStatement{
    private Expression expression;

    public CloseFileStatement(Expression expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "CloseFileStatement (" + this.expression.toString() + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws FileNotOpenException, IOException {
        int fd = this.expression.eval(state.get_symbolTable(), state.getHeap());
        FileData file = state.getFileData(fd);
        state.getFileTable().remove(fd);
        if(file == null)
        {
            throw new FileNotOpenException("FileNotOpened Exception at: " + this.toString() + "\nThere is no opened file with file descriptor = " + fd);
        }
        file.getFileDescriptor().close();
        return null;

    }
}