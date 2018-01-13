package Controller;

import Repository.Repo;
import domain.*;
import domain.Expressions.Expression;
import domain.Observable;
import domain.Observer;
import domain.Statements.CloseFileStatement;
import domain.Statements.IStatement;
import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;
import exception.NotDeclaredVariable;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.util.Callback;

import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller implements Observer<PrgState> {
    private Repo repo;
    private String File;
    private ExecutorService executor;
    private PrgStateService prgStateService;
    private ObservableList<PrgState> prgStateModel;
    private ObservableList<String> outListModel;
    private ObservableList<Map.Entry<Integer, Integer>> heapTableModel;
    private ObservableList<MyDictionary<Integer, String>> fileTableModel;
    private ObservableList<IStatement> exeStackModel;
    private ObservableList<MyDictionary<String, Integer>> symTableModel;
    private int programId;

    @FXML
    private TableView<MyDictionary<Integer, String>> FileTableTV;

    @FXML
    private ListView<IStatement> ExeStackLV;

    @FXML
    private TableView<MyDictionary<String, Integer>> SymbolTV;

    @FXML
    private ListView<PrgState> PrgStatesIdentifiersLV;

    @FXML
    private ListView<String> OutLV;
    @FXML
    private Button btnRun;
    @FXML
    private TextField PrgStatesTF;

    @FXML
    private TableView<Map.Entry<Integer, Integer>> HeapTable;


    public Controller(Repo r) {
        this.repo = r;
    }

    public Controller(IStatement initialStatement, String File) {
        this.repo = new Repo(new PrgState(initialStatement), File);
        this.File = File;
    }

    public Controller(IStatement initialStatement) {
        this.repo = new Repo(new PrgState(initialStatement));
    }
    public Controller() {
    }

    @FXML
    private void initialize() {
    }

    public void setService(PrgStateService service) {

        this.prgStateService = service;

        System.out.println(service.getRepo().getPrgList().get(0).get_stmt());

        this.programId = this.prgStateService.getAll().get(0).getId();

        this.repo = this.prgStateService.getRepo();
        //prg state model;
        this.prgStateModel = FXCollections.observableArrayList();
        this.PrgStatesIdentifiersLV.setItems(this.prgStateModel);
        this.PrgStatesIdentifiersLV.setCellFactory(new Callback<ListView<PrgState>, ListCell<PrgState>>() {
            @Override
            public ListCell<PrgState> call(ListView<PrgState> param) {
                ListCell<PrgState> listCell = new ListCell<PrgState>() {
                    @Override
                    protected void updateItem(PrgState e, boolean empty) {
                        super.updateItem(e, empty);
                        if (e == null || empty)
                            setText("");
                        else
                            setText(String.valueOf(e.getId()));
                    }
                };
                return listCell;
            }
        });

        this.heapTableModel = FXCollections.observableArrayList();
        TableColumn<Map.Entry<Integer, Integer>, String> first = new TableColumn<>("Address");
        TableColumn<Map.Entry<Integer, Integer>, String> second = new TableColumn<>("Value");
        first.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getKey()));
            }
        });
        second.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Map.Entry<Integer, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getValue()));
            }
        });
        this.HeapTable.getColumns().setAll(first, second);
        this.HeapTable.setItems(this.heapTableModel);

        this.fileTableModel = FXCollections.observableArrayList();
        TableColumn<MyDictionary<Integer, String>, String> fd = new TableColumn<>("File descriptor");
        TableColumn<MyDictionary<Integer, String>, String> fn = new TableColumn<>("File name");
        fd.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<MyDictionary<Integer, String>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<MyDictionary<Integer, String>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getAll().keySet()));
            }
        });
        fn.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<MyDictionary<Integer, String>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<MyDictionary<Integer, String>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getAll().values()));
            }
        });

        this.FileTableTV.getColumns().setAll(fd, fn);
        this.FileTableTV.setItems(this.fileTableModel);

        this.symTableModel = FXCollections.observableArrayList();
        TableColumn<MyDictionary<String, Integer>, String> symNameColumn = new TableColumn<>("Symbol name");
        TableColumn<MyDictionary<String, Integer>, String> symValueColumn = new TableColumn<>("Value");
        symNameColumn.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<MyDictionary<String, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<MyDictionary<String, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getAll().keySet()));
            }
        });
        symValueColumn.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<MyDictionary<String, Integer>, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<MyDictionary<String, Integer>, String> param) {
                return new SimpleStringProperty(String.valueOf(param.getValue().getAll().values()));
            }
        });
        this.SymbolTV.getColumns().setAll(symNameColumn, symValueColumn);
        this.SymbolTV.setItems(this.symTableModel);

        this.outListModel = FXCollections.observableArrayList();
        this.OutLV.setItems(this.outListModel);

        this.exeStackModel = FXCollections.observableArrayList();
        this.ExeStackLV.setItems(this.exeStackModel);


        this.PrgStatesIdentifiersLV.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<PrgState>() {
            @Override
            public void changed(ObservableValue<? extends PrgState> observable, PrgState oldValue, PrgState newValue) {
               try {
                   programId = newValue.getId();
                   List<PrgState> prgStates = prgStateService.getAll();
                   PrgState current = prgStates.stream().filter(e -> e.getId() == programId).findFirst().get();

                   List<IStatement> list = new ArrayList<>();
                   for (IStatement stm : current.get_exeStack().getAll())
                       list.add(stm);
                   exeStackModel.setAll(list);
                   symTableModel.setAll(current.get_symbolTable().clone().getAll().entrySet().stream().map(e -> new MyDictionary<>(e.getKey(), e.getValue())).collect((Collectors.toList())));
               }catch(Exception e){}
            }
        });



        this.update(this.prgStateService);
    }

    public void setRepo(Repo r)
    {
        this.repo = r;
    }



    public Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet()
                .stream()
                .filter(e -> symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }




    List<PrgState> removeCompletedPrg(List<PrgState> inPrgList)
    {
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    void oneStepForAllPrg(List<PrgState> prgList) throws IOException, InterruptedException {


        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        //start the execution of the callables
        //it returns the list of new created PrgStates (namely threads)
        List<PrgState> newPrgList = executor.invokeAll(callList)
                .stream()
                .map(future->{
                    try {
                        return future.get();
                    }
                    catch(Exception e) {
                        System.out.println("Erorr oneStepForAll");
                        return null;
                    }
                }).filter(p -> p!=null).collect(Collectors.toList());

        //add the new created threads to the list of existing threads
        prgList.addAll(newPrgList);
        for (PrgState prg : prgList) {
            repo.logPrgStateExec(prg);
        }
        //Save the current programs in the repository
        repo.setPrgList(prgList);
        this.prgStateService.notifyObservers();
    }

    public void allStep() throws IOException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        //remove the completed programs
        List<PrgState> prgList=removeCompletedPrg(repo.getPrgList());
        while(prgList.size() > 0){
            prgList.get(prgList.size() - 1).getHeap().setMap(conservativeGarbageCollector(
                    prgList.get(prgList.size() - 1).get_symbolTable().values(),
                    prgList.get(prgList.size() - 1).getHeap().toMap()));
            oneStepForAllPrg(prgList);
            prgList=removeCompletedPrg(repo.getPrgList());
            //remove the completed programs
        }
        executor.shutdownNow();
        repo.setPrgList(prgList);
    }

    @FXML
    public void allStepsGUI() throws IOException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        while(true) {
            this.prgStateService.notifyObservers();
            List<PrgState> prgList = removeCompletedPrg(this.prgStateService.getAll());
            if(prgList.size() == 0) {
                System.out.println("FINISHED");
                break;
            }
            oneStepForAllPrg(prgList);
            System.out.println("ONE STEP");
            break;
        }
        executor.shutdownNow();
    }

    @Override
    public void update(Observable<PrgState> observable) {
        List<PrgState> prgStates = this.prgStateService.getAll();
        this.PrgStatesTF.setText(String.valueOf(prgStates.size()));
        this.prgStateModel.setAll(prgStates);
        this.outListModel.setAll(this.prgStateService.getOutList());
        this.heapTableModel.setAll(this.prgStateService.getHeapList());
        this.fileTableModel.setAll(this.prgStateService.getFileList());



        try {
            PrgState current = prgStates.stream().filter(e -> e.getId() == programId).findFirst().get();
            List<IStatement> list = current.get_exeStack().toStack().stream().collect(Collectors.toList());
            Collections.reverse(list);
            this.exeStackModel.setAll(list);
            this.symTableModel.setAll(current.get_symbolTable().clone().getAll().entrySet().stream().map(e->new MyDictionary<String, Integer>(e.getKey(), e.getValue())).collect(Collectors.toList()));
        }catch ( Exception e )
        {
            System.out.println(e.getMessage());
        }


    }




//    public void executeAll()  throws NotDeclaredVariable, DivideByZeroException, FileAlreadyOpenedException, FileNotOpenException, IOException
//    {
//        try {
//            PrgState current = repo.getCurrentPrgState();
//            while (!current.get_exeStack().isEmpty()) {
//                step(current);
//                current.getHeap().setMap(conservativeGarbageCollector(
//                        current.get_symbolTable().values(),
//                        current.getHeap().toMap()));
//
//                repo.logPrgStateExec();
//
//            }
//        }
//        catch (Exception e) {
//            System.out.println("Logging error");
//            return;
//        }
//        finally
//        {
//            try {
//                for(int e: repo.getCurrentPrgState().getFileTable().getAll())
//                {
//                    repo.getCurrentPrgState().getFileTable().get(e).getFileDescriptor().close();
//                    repo.getCurrentPrgState().getFileTable().remove(e);
//                }
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
//    }

}
