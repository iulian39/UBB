package GUI;

import Controller.Controller;
import domain.*;
import domain.Statements.IStatement;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.util.Callback;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class ControllerMain implements Observer<PrgState> {

    private Controller c;
    private PrgStateService prgStateService;
    private ObservableList<PrgState> prgStateModel;
    private ObservableList<String> outListModel;
    private ObservableList<MyDictionary<Integer, String>> heapTableModel;
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
    private TextField PrgStatesTF;

    @FXML
    private TableView<MyDictionary<Integer, String>> HeapTable;

    @FXML
    private Button btnRun;

    void setController(Controller c)
    {
        this.c = c;
    }

    public void setService(PrgStateService service) {

        this.prgStateService = service;

        this.c.setRepo(this.prgStateService.getRepo());
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
        this.HeapTable.setItems(this.heapTableModel);

        this.fileTableModel = FXCollections.observableArrayList();
        this.FileTableTV.setItems(this.fileTableModel);

        this.symTableModel = FXCollections.observableArrayList();
        this.SymbolTV.setItems(this.symTableModel);

        this.outListModel = FXCollections.observableArrayList();

        this.PrgStatesIdentifiersLV.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<PrgState>() {
            @Override
            public void changed(ObservableValue<? extends PrgState> observable, PrgState oldValue, PrgState newValue) {
                programId = newValue.getId();
                List<PrgState> prgStates = prgStateService.getAll();
                PrgState current = prgStates.stream().filter(e->e.getId() == programId).findFirst().get();

                List<IStatement> list = new ArrayList<>();
                for(IStatement stm: current.get_exeStack().getAll())
                    list.add(stm);
                Collections.reverse(list);
                exeStackModel.setAll(list);
                symTableModel.setAll((MyDictionary<String, Integer>) current.get_symbolTable().clone().getAll().entrySet().stream().map(e->new MyDictionary(e.getKey(), e.getValue())).collect(Collectors.toList()));
            }
        });

        // exeStack
        this.exeStackModel = FXCollections.observableArrayList();
        this.ExeStackLV.setItems(this.exeStackModel);

        this.update(this.prgStateService);
    }

    @Override
    public void update(Observable<PrgState> observable) {
        List<PrgState> prgStates = this.prgStateService.getAll();
        this.PrgStatesTF.setText(String.valueOf(prgStates.size()));
        this.prgStateModel.setAll(prgStates);
        this.outListModel.setAll(this.prgStateService.getOutList());
        this.heapTableModel.setAll(this.prgStateService.getHeapList());

        this.fileTableModel.setAll( prgStates.get(0).getFileTable().keys()
                .stream()
                .map(k -> new MyDictionary<Integer, String>(k, prgStates.get(0).getFileTable().get(k).getFileName()))
                .collect(Collectors.toList())
        );

        PrgState current = prgStates.stream().filter(e->e.getId() == programId).findFirst().get();

        List<IStatement> list = current.get_exeStack().toStack().stream().collect(Collectors.toList());
        Collections.reverse(list);
        this.exeStackModel.setAll(list);
        this.symTableModel.setAll(current.get_symbolTable().clone().getAll().entrySet().stream().map(e->new MyDictionary<String, Integer>(e.getKey(), e.getValue())).collect(Collectors.toList()));
    }
}
