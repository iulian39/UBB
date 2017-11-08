import Controller.Controller;
import Repository.Repo;
import UI.TextMenu;
import domain.*;
import domain.Expressions.ArithmeticExpression;
import domain.Expressions.ConstExpression;
import domain.Expressions.VarExpression;
import domain.Statements.*;

import java.util.Scanner;

public class main {
    public main(){}

    public static void main(String args[])
    {

        MyStack<IStatement> exeStack = new MyStack<>();
        MyDictionary<String, Integer> symTable = new MyDictionary<>();
        MyList<Integer> out = new MyList<Integer>();
        FileTable<Integer,  FileData> fileT = new FileTable<>();

        // a=2+3*5;b=a+1;
        // Print(b)
        IStatement ex1 = new CompoundStatement(new AssignStatement("a", new ArithmeticExpression('+',new ConstExpression(2),new
                ArithmeticExpression('*',new ConstExpression(3), new ConstExpression(5)))),
                new CompoundStatement(new AssignStatement("b",new ArithmeticExpression('+',new VarExpression("a"), new
                        ConstExpression(1))), new PrintStatement(new VarExpression("b"))));

        IStatement ex2 = new CompoundStatement(new AssignStatement("v",new ConstExpression(2)), new PrintStatement(new
                VarExpression("v")));

        IStatement ex3 = new CompoundStatement(new AssignStatement("a", new ArithmeticExpression('-',new ConstExpression(2), new
                ConstExpression(2))),
                new CompoundStatement(new IfStatement(new VarExpression("a"),new AssignStatement("v",new ConstExpression(2)), new
                        AssignStatement("v", new ConstExpression(3))), new PrintStatement(new VarExpression("v"))));

        exeStack.push(ex1);


        System.out.printf("Input the file where the log will be registered: ");
        Scanner terminalInput = new Scanner(System.in);
        String File = terminalInput.nextLine();

        System.out.printf("Input the file where the variable will be read from: ");
        String ReadFile = terminalInput.nextLine();

        /*
        *   Lab5Ex1
        *   openRFile (var_f, "test.in");
        *   readFile (var_f, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        *
        * */
        IStatement lab5ex1 = new CompoundStatement(
                new OpenFileStatement("var_f", ReadFile),
                new CompoundStatement(
                        new ReadFileStatement(new VarExpression("var_f"), "var_c"),
                        new CompoundStatement(
                                new PrintStatement(new VarExpression("var_c")),
                                new CompoundStatement(
                                        new IfStatement(
                                                new VarExpression("var_c"),
                                                new CompoundStatement(
                                                        new ReadFileStatement(new VarExpression("var_f"), "var_c"),
                                                        new PrintStatement(new VarExpression("var_c"))
                                                ),
                                                new PrintStatement(new ConstExpression(0))
                                        ),
                                        new CloseFileStatement(new VarExpression("var_f"))
                                )
                        )
                )
        );

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "Exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), new Controller(ex1, File)));
        menu.addCommand(new RunExample("2", ex2.toString(), new Controller(ex2, File)));
        menu.addCommand(new RunExample("3", ex3.toString(), new Controller(ex3, File)));
        menu.addCommand(new RunExample("4", lab5ex1.toString(), new Controller(lab5ex1, File)));
        menu.show();


    }

}