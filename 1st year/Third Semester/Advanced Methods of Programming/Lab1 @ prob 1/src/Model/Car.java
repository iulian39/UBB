package Model;

public class Car extends Vehicle
{
    protected int year;
    protected String type;

    public Car() {}
    public Car(String color, int year, String type)
    {
        super(color);
        this.year = year;
        this.type = type;
    }

    @Override
    public String toString()
    {
        return "Car " + this.color + " " + this.year + " " + this.type;
    }

    @Override
    public boolean equals(Object O) {
        return O instanceof Car && (this.year == ((Car) O).year) && (this.type.equals(((Car) O).type)) && (this.color.equals(((Car) O).color));
    }
}