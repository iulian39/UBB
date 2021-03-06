import domain.Expressions.*;
import domain.Statements.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class main {

    public static void main(String[] args) throws Exception {
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



        System.out.printf("Input the file where the log will be registered: ");
        Scanner terminalInput = new Scanner(System.in);
        String File = terminalInput.nextLine();

        System.out.printf("Input the file where the variable will be read from: ");
        String ReadFile = terminalInput.nextLine();

        /*
        *   openRFile (var_f, "test.in");
        *   readFile (var_f, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        */
        IStatement lab4ex1 = new CompoundStatement(
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

       /*
        *   Lab4Ex2
        *   openRFile (var_f, "test.in");
        *   readFile (var_f + 5, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        * */
        IStatement lab4ex2 = new CompoundStatement(
                new OpenFileStatement("var_f", "c.txt"),
                new CompoundStatement(
                        new ReadFileStatement(new ArithmeticExpression('+', new VarExpression("var_f"), new ConstExpression(5)), "var_c"),
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

//        Example: v=10;new(v,20);new(a,22);wH(a,30);print(a);print(rH(a));a=0
//        At the end of execution: Heap={1->20}, SymTable={v->1, a->0} and Out={2,30}
        IStatement lab5ex1 =
                new CompoundStatement(
                        new AssignStatement("v", new ConstExpression(10)),
                        new CompoundStatement(
                                new newH("v", new ConstExpression(20)),
                                new CompoundStatement(
                                        new newH("a", new ConstExpression(22)),
                                        new CompoundStatement(
                                                new writeH("a", new ConstExpression(30)),
                                                new CompoundStatement(
                                                        new PrintStatement(new VarExpression("a")),
                                                        new CompoundStatement(
                                                                new PrintStatement(new readH("a")),
                                                                new AssignStatement("a", new ConstExpression(0)))))
                                )
                        )
                );
        //Example:  v=0,
        // while(v <= 10)
        // { Print (v),
        //  v=v + 1 )
        // end }
        IStatement lab7 = new CompoundStatement(
                new AssignStatement("v", new ConstExpression(0)),
                new WhileStatement(new BolleanExpression("<=", new VarExpression("v"), new ConstExpression(10)),
                        new CompoundStatement(
                                new PrintStatement(new VarExpression("v")),
                                new AssignStatement("v", new ArithmeticExpression('+', new VarExpression("v"), new ConstExpression(1)))
                        ))
        );

        /*v=10;new(a,22);
        fork(wH(a,30);v=32;print(v);print(rH(a)));
        print(v);print(rH(a))*/

        IStatement lab8ex1 = new CompoundStatement(
                new CompoundStatement(
                        new AssignStatement("v", new ConstExpression(10)),
                        new newH("a", new ConstExpression(22))
                ),
                new CompoundStatement(
                        new forkStmt(
                                new CompoundStatement(
                                        new writeH("a", new ConstExpression(30)),
                                        new CompoundStatement(
                                                new AssignStatement("v", new ConstExpression(32)),
                                                new forkStmt(
                                                        new CompoundStatement(
                                                                new PrintStatement(new VarExpression("v")),
                                                                new PrintStatement(new readH("a"))
                                                        )
                                                )
                                        )
                                )
                        ),
                        new CompoundStatement(
                                new PrintStatement(new VarExpression("v")),
                                new PrintStatement(new readH("a"))
                        )
                )
        );

        List<String> menu = new ArrayList<>();
        menu.add(ex1.toString());
        menu.add(ex2.toString());
        menu.add(ex3.toString());







    }



}
