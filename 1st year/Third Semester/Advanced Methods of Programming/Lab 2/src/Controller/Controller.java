package Controller;

import Repository.Repo;
import domain.*;
import domain.Expressions.Expression;
import domain.Statements.CloseFileStatement;
import domain.Statements.IStatement;
import exception.DivideByZeroException;
import exception.FileAlreadyOpenedException;
import exception.FileNotOpenException;
import exception.NotDeclaredVariable;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    private Repo repo;
    private String File;
    private ExecutorService executor;

    public Controller(Repo r) {
        this.repo = r;
    }

    public Controller(IStatement initialStatement, String File) {
        this.repo = new Repo(new PrgState(initialStatement), File);
        this.File = File;
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
//        //before the execution, print the PrgState List into the log file
//        for (PrgState prg : prgList) {
//            repo.logPrgStateExec(prg);
//        }

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
        //HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        //setPrgList of repository in order to change the repository
//        for(PrgState x: repo.getPrgList()) {
//            for (int y : x.getFileTable().getAll()) {
//                try {
//                    x.getFileTable().get(y).getFileDescriptor().close();
//                } catch ( IOException e1 ) {
//                    e1.printStackTrace();
//                }
//                x.getFileTable().remove(y);
//            }
//        }
//        // update the repository state

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
