package domain;

import java.io.BufferedReader;
import java.util.Collection;

public interface IFileTable<K,V>
{
    V get(K key);
    V remove(K key);
    void add(K key, V value);
    Iterable<K> getAll();
    public Collection<V> values();
}