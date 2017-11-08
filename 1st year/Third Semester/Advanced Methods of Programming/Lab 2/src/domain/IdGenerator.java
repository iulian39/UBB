package domain;

public class IdGenerator
{
    static int id = 0;
    static public int generateId()
    {
        return id++;
    }
}