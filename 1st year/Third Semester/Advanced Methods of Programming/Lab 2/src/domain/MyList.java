package domain;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> {
    private List<T> l;

    public MyList()
    {
        l = new ArrayList<>();
    }

    public void add(T x)
    {
        l.add(x);
    }

    @Override
    public String toString() {
        StringBuffer buff = new StringBuffer();
        for ( T i : l)
        {
            buff.append(i);
            buff.append(" ");
        }
        return buff.toString();
    }
}
