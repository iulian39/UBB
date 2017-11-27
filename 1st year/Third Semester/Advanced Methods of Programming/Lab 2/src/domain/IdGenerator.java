package domain;

public class IdGenerator
{
    static int id = 1;
    static public int generateId()
    {
        return id++;
    }
}