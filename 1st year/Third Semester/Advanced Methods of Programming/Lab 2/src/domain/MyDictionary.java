package domain;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class MyDictionary<Key, Value>
{
    private Map<Key, Value> _dictinary;

    public MyDictionary(){
        this._dictinary = new HashMap<>();
    }

    public MyDictionary(HashMap<Key, Value> dictionary)
    {
        this._dictinary = new HashMap<>();
        this._dictinary = dictionary;
    }

    public void put(Key key, Value value)
    {
        _dictinary.put(key, value);
    }

    public Value get(Key k)
    {
        return _dictinary.get(k);
    }

    public boolean containsKey(Key k)
    {
        return _dictinary.containsKey(k);
    }

    public void update(Key K, Value V)
    {
        _dictinary.put(K, V);
    }

    public Value remove(Key k)
    {
        return this._dictinary.remove(k);
    }

    public  String toString()
    {
        StringBuffer buff = new StringBuffer();

        for (Map.Entry<Key,Value> d: _dictinary.entrySet() )
        {
            buff.append(d.getKey());
            buff.append(d.getValue());

        }
        return buff.toString();
    }

    public Collection<Value> values() {
        return this._dictinary.values();
    }

    public Map<Key, Value> getAll()
    {
        return this._dictinary;
    }

}
