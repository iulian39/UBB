package GUI;

import Repository.Repo;
import domain.*;
import domain.Expressions.*;
import Controller.Controller;
import domain.Statements.*;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListView;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ControllerStart {

    private List<IStatement> menu;
    private String File;

    @FXML
    private ListView<String> listV;

    public static Repo getNewRepository(IStatement prg) {
        /// Create the data structures for the program execution
        MyDictionary<String, Integer> _symbolTable = new MyDictionary<>();
        MyStack<IStatement> _exeStack = new MyStack<>();
        MyList<Integer> _messages =new MyList<>();
        FileTable<Integer,  FileData> fileTable= new FileTable<>();
        Heap<Integer> heap = new Heap<>();
        LatchTable latch = new LatchTable();
        int id = IdGenerator.generateId();
        _exeStack.push(prg);


        PrgState prgState = new PrgState(_exeStack, _symbolTable,_messages,prg,fileTable,heap,id, latch);
        Repo repo = new Repo(prgState, "log.txt");
        return repo;
    }

    @FXML
    void initialize() {
        menu = new ArrayList<>();
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


        /*
        *   openRFile (var_f, "test.in");
        *   readFile (var_f, var_c); print (var_c);
        *   If var_c then readFile (var_f, var_c); print (var_c) else print (0);
        *   closeRFile (var_f)
        */
        IStatement lab4ex1 = new CompoundStatement(
                new OpenFileStatement("var_f", "a.txt"),
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

        /*
        v=0;
        (repeat (fork(print(v);v=v-1);v=v+1) until v==3);
        x=1;y=2;z=3;w=4;
        print(v*10)
         */
        IStatement Ex1 = new CompoundStatement(
                new AssignStatement("v", new ConstExpression(0)),
                new CompoundStatement(
                        new RepeatStmt(
                                new CompoundStatement(
                                        new forkStmt(
                                                new CompoundStatement(
                                                        new PrintStatement(new VarExpression("v")),
                                                        new AssignStatement("v", new ArithmeticExpression('-', new VarExpression("v"), new ConstExpression(1)))
                                                )),
                                        new AssignStatement("v", new ArithmeticExpression('+', new VarExpression("v"), new ConstExpression(1)))
                                ),
                                new BolleanExpression("==", new VarExpression("v"), new ConstExpression(3))
                        ),
                        new CompoundStatement(
                                new AssignStatement("x", new ConstExpression(1)),
                                new CompoundStatement(
                                        new AssignStatement("y", new ConstExpression(2)),
                                        new CompoundStatement(
                                                new AssignStatement("z", new ConstExpression(3)),
                                                new CompoundStatement(
                                                        new AssignStatement("w", new ConstExpression(4)),
                                                        new PrintStatement(new ArithmeticExpression('*', new VarExpression("v"), new ConstExpression(10)))
                                                )
                                        )

                                )
                        )
                )
        );

        /*new(v1,2);new(v2,3);new(v3,4);newLatch(cnt,rH(v2));
        fork(wh(v1,rh(v1)*10));print(rh(v1));countDown(cnt);
        fork(wh(v2,rh(v2)*10));print(rh(v2));countDown(cnt);
        fork(wh(v3,rh(v3)*10));print(rh(v3));countDown(cnt))));
        await(cnt);
        print(100);
        countDown(cnt);
        print(100)
        The final Out should be {20,id-first-child,30,id-second-child,40, id-third-child,
        100,100} where id-first-child, id-second-child and id-third-child are the unique
        identifiers of those three new threads created by fork.*/
        IStatement examEx2 = new CompoundStatement(
                new newH("v1", new ConstExpression(2)),
                new CompoundStatement(
                        new newH("v2", new ConstExpression(3)),
                        new CompoundStatement(
                                new newH("v3", new ConstExpression(4)),
                                new CompoundStatement(
                                        new NewLatchStmt("cnt", new readH("v2")),
                                        new CompoundStatement(
                                                new forkStmt(
                                                        new CompoundStatement(
                                                                new writeH("v1", new ArithmeticExpression('*', new readH("v1"), new ConstExpression(10))),
                                                                new CompoundStatement(
                                                                        new PrintStatement(new readH("v1")),
                                                                        new CountDownStmt("cnt")
                                                                )
                                                        )
                                                ),
                                                new CompoundStatement(
                                                        new forkStmt(
                                                                new CompoundStatement(
                                                                        new writeH("v2", new ArithmeticExpression('*', new readH("v2"), new ConstExpression(10))),
                                                                        new CompoundStatement(
                                                                                new PrintStatement(new readH("v2")),
                                                                                new CountDownStmt("cnt")
                                                                        )
                                                                )
                                                        ),
                                                        new CompoundStatement(
                                                                new forkStmt(
                                                                        new CompoundStatement(
                                                                                new writeH("v3", new ArithmeticExpression('*', new readH("v3"), new ConstExpression(10))),
                                                                                new CompoundStatement(
                                                                                        new PrintStatement(new readH("v3")),
                                                                                        new CountDownStmt("cnt")
                                                                                )
                                                                        )
                                                                ),
                                                                new CompoundStatement(
                                                                        new AwaitStmt("cnt"),
                                                                        new CompoundStatement(
                                                                                new PrintStatement(new ConstExpression(100)),
                                                                                new CompoundStatement(
                                                                                        new CountDownStmt("cnt"),
                                                                                        new PrintStatement(new ConstExpression(100))
                                                                                )
                                                                        )
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );

        ObservableList<String> listItems = FXCollections.observableArrayList();

        menu.add(ex1);
        menu.add(ex2);
        menu.add(ex3);
        menu.add(lab4ex1);
        menu.add(lab4ex2);
        menu.add(lab5ex1);
        menu.add(lab7);
        menu.add(lab8ex1);
        menu.add(Ex1);
        menu.add(examEx2);

        for(IStatement stmt : menu)
        {
            listItems.add(stmt.toString());
        }

        listV.setItems(listItems);
    }

    public void loadMainWindow() throws IOException {
        try {
            FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("gui.fxml"));
            Parent root1 = fxmlLoader.load();

            PrgStateService prgStateService = new PrgStateService(getNewRepository(menu.get(listV.getSelectionModel().getSelectedIndex())));
            Controller ctrl = fxmlLoader.getController();
            ctrl.setService(prgStateService);
            prgStateService.addObserver(ctrl);


            Stage stage = new Stage();
            stage.initModality(Modality.APPLICATION_MODAL);
            stage.setScene(new Scene(root1));
            stage.show();
        }catch ( Exception e){
            System.out.println("Invalid index");
        }

    }

}
