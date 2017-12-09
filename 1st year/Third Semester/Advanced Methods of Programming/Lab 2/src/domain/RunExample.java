package domain;

import Controller.Controller;
import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;
import exception.NotDeclaredVariable;

import java.io.IOException;


public class RunExample extends Command {
    private Controller ctr;
    public RunExample(String key, String desc,Controller ctr){
        super(key, desc);
        this.ctr=ctr;
    }
    @Override
    public void execute() throws InterruptedException {
        try {
            ctr.allStep();
        }
        catch (NotDeclaredVariable | DivideByZeroException | FileAlreadyOpenedException | FileNotOpenException | IOException e) {
                        System.out.println(e.getMessage());

        }
    }
}
