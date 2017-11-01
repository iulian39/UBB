package Model;

public class Bike extends Vehicle
{
    protected double weight;
    protected String type;

    public Bike() {}
    public Bike(String Color, double Weight, String Type)
    {
        super(Color);
        this.weight = Weight;
        this.type = Type;
    }

    @Override
    public String toString()
    {
        return "Bike " + this.color + " " + this.weight + " " + this.type;
    }

    @Override
    public boolean equals(Object O) {
        return O instanceof Bike && (this.weight == ((Bike) O).weight) && (this.type.equals(((Bike) O).type)) && (this.color.equals(((Bike) O).color));
    }
}
