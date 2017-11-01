package Model;

public class Motorcycle extends Vehicle
{
    protected int year;
    protected String type;

    public Motorcycle() {}
    public Motorcycle(String color, int year, String type)
    {
        super(color);
        this.year = year;
        this.type = type;
    }

    @Override
    public String toString()
    {
        return "Motorcycle " + this.color + " " + this.year + " " + this.type;
    }

    @Override
    public boolean equals(Object O) {
        return O instanceof Motorcycle && (this.year == ((Motorcycle) O).year) && (this.type.equals(((Motorcycle) O).type)) && (this.color.equals(((Motorcycle) O).color));
    }
}