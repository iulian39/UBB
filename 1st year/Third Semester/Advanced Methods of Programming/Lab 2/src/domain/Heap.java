package domain;

import java.util.HashMap;
import java.util.Map;

public class Heap<T> {

    int memory;
    Map<Integer, T> vals;

    public Heap()
    {
        memory = 1;
        vals = new HashMap<>();
    }

    public Heap(Map<Integer, T> vals) {
        memory = 1;
        this.vals = vals;
    }

    public int allocate(T value) {
        this.memory++;
        this.vals.put(this.memory, value);
        return memory;
    }

    public T get(int addr) {
        return this.vals.get(addr);
    }

    public void remove(int addr)
    {
        this.vals.remove(addr);
    }

    public boolean contains(int addr)
    {
        if (this.vals.containsKey(addr)) return true;
        else {
            return false;
        }
    }

    public void update(int addr, T value)
    {
        this.vals.put(addr, value);
    }

    public void add(int addr, T value) {
        this.vals.put(addr, value);
    }


    public T deallocate(int addr) {
        return this.vals.remove(addr);
    }


    public String toString() {
        String ret = "";
        boolean ok = false;
        for(HashMap.Entry<Integer, T> entry : this.vals.entrySet()) {
            if(ok)
                ret = ret + "\n";
            ret += entry.getKey().toString() + " -> " + entry.getValue().toString();
            ok = true;
        }
        return ret;
    }


    public void setMap(Map<Integer, T> map) {
        this.vals = map;
    }

    public Map<Integer, T> toMap() {
        return this.vals;
    }

    public Integer size()
    {
        return this.vals.size();
    }
}