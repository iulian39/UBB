package domain;

import java.util.Collection;
import java.util.Map;

public interface iLatchTable {
    Integer put(Integer key, Integer value);
    Integer get(Integer key);
    Collection<Integer> values();
    Collection<Integer> keys();
    Integer remove(Integer fd);
    Map<Integer, Integer> toMap();


}
