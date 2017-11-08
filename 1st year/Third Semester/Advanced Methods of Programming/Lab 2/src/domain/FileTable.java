package domain;

import java.util.Collection;
import java.util.HashMap;

public class FileTable<K,V> implements IFileTable<K,V>
{
    private HashMap<K,V> fileTable = new HashMap<>();

    public FileTable(){}

    public FileTable(K t1, V t2) {
        fileTable.put(t1, t2);
    }

    public FileTable(HashMap<K,V> fileTable) {
        this.fileTable = fileTable;
    }


    @Override
    public V get(K key)
    {
        return fileTable.get(key);
    }

    public boolean contains(K key){
        return fileTable.containsKey(key);
    }

    @Override
    public V remove(K key)
    {
        return fileTable.remove(key);
    }

    @Override
    public Iterable<K> getAll()
    {
        return fileTable.keySet();
    }

    @Override
    public void add (K key, V value)
    {
        fileTable.put(key,value);
    }

    @Override
    public Collection<V> values() {
        return this.fileTable.values();
    }
}