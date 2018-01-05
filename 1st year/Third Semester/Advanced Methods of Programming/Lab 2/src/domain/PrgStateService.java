package domain;


import Repository.Repo;

import java.util.*;


public class PrgStateService implements Observable<PrgState> {
    private List<Observer<PrgState>> observers = new ArrayList<Observer<PrgState>>();
    private Repo repo;

    public PrgStateService(Repo repo) {
        this.repo = repo;
    }

    public Repo getRepo() {
        return this.repo;
    }

    public List<PrgState> getAll() {
        List<PrgState> mList = new ArrayList<>();
        mList.addAll(this.repo.getPrgList());
        return mList;
    }

    public List<String> getOutList() {
        List<String> mList = new ArrayList<>();
        for(int i = 0; i < this.repo.getPrgList().get(0).get_messages().size(); ++ i)
            mList.add(String.valueOf(this.repo.getPrgList().get(0).get_messages().get(i)));
        return mList;
    }

    public List<MyDictionary<Integer, String>> getFileList() {
        List<MyDictionary<Integer, String>> mList = new ArrayList<>();
        for(Integer x : this.repo.getPrgList().get(0).getFileTable().keys())
            mList.add(new MyDictionary(x, this.repo.getPrgList().get(0).getFileTable().get(x).getFileName()));
        return mList;
    }

    public MyDictionary<Integer, String> getHeapList() {
        MyDictionary<Integer, String> hList = new MyDictionary<>();
        for(int i = 0; i < this.repo.getPrgList().get(0).getHeap().size(); ++ i)
            hList.put(i, this.repo.getPrgList().get(0).getHeap().get(i).toString());
        return hList;
    }

    @Override
    public void addObserver(Observer<PrgState> o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer<PrgState> o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for(Observer o : observers)
            o.update(this);
    }


}
