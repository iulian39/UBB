package Model;

public abstract class Vehicle
{
    protected String color;

    public Vehicle() {}

    public Vehicle(String color)
    {
        this.color = color;
    }

    public String getColor()
    {
        return this.color;
    }

    public void setColor( String color )
    {
        this.color = color;
    }

}