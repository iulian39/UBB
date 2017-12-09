package domain.Statements;


import domain.FileData;

import domain.IdGenerator;
import domain.PrgState;
import exception.FileAlreadyOpenedException;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Objects;

public class OpenFileStatement implements IStatement {
    private String id, fileName;

    public OpenFileStatement(String id, String fileName) {
        this.id = id;
        this.fileName = fileName;
    }

    @Override
    public PrgState execute(PrgState p) throws FileNotFoundException, FileAlreadyOpenedException {
        for(FileData file : p.getFileTable().values())
            if(Objects.equals(file.getFileName(), this.fileName))
                throw new FileAlreadyOpenedException("FileAlreadyOpenedException at: " + this.toString() + "\nThe file " + this.fileName + " is already open");

        File f = new File(this.fileName);
        if(!f.exists())
            throw new FileNotFoundException("FileNotFoundException at: " + this.toString() + "\n" + "The file " + this.fileName + " does not exist");

        int actFd = IdGenerator.generateId();
        p.getFileTable().add(actFd, new FileData(this.fileName, new BufferedReader(new FileReader(this.fileName))));
        p.get_symbolTable().put(this.id, actFd);
        return null;
    }
    @Override
    public String toString() {
        return "openRFile (" + this.id + ", " + this.fileName + ")";
    }
}