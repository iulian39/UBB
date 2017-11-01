import Controller.Controller;
import Repository.IRepo;
import Repository.Repo;
import domain.*;
import domain.Expressions.ArithmeticExpression;
import domain.Expressions.ConstExpression;
import domain.Expressions.VarExpression;
import domain.Statements.AssignStatement;
import domain.Statements.CompoundStatement;
import domain.Statements.IStatement;
import domain.Statements.IfStatement;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

public class main {
    public main(){}

    public static void main(String args[])
    {

        MyStack<IStatement> exeStack = new MyStack<>();
        MyDictionary<String, Integer> symTable = new MyDictionary<>();
        MyList<Integer> out = new MyList<Integer>();

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

        PrgState prgState = new PrgState(exeStack, symTable, out, ex1);
        Repo repo = new Repo(prgState);
        Controller ctrl = new Controller(repo);
        ctrl.executeAll();
    }

}