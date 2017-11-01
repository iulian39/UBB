
import Controller.Controller;
import Model.Vehicle;
import Model.Bike;
import Model.Car;
import Model.Motorcycle;
import Repository.Repository;

public class Main {
    public Main(){}

    public static void main(String args[])
    {
        Repository repo = new Repository();
        Bike a = new Bike("Yellow",15.7,"Mountain bike");
        Car c = new Car("Red",2015,"Audi A4");
        Bike d = new Bike("Red",20,"Mountain bike");
        Motorcycle b = new Motorcycle("Blue",2004,"Cruiser");

        Controller controller = new Controller(repo);

        controller.add(a);
        controller.add(b);
        controller.add(c);
        controller.add(d);


        for(Vehicle element:controller.getAll()){
            if(element.getColor().equals("Red"))
                System.out.println(element.toString());
        }
    }

}