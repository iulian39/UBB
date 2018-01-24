package GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class guiStart extends Application{

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        try {
            AnchorPane root = FXMLLoader.load(getClass().getResource("start.fxml"));
            Scene scene = new Scene(root);


            primaryStage.setTitle("Start Window");
            primaryStage.setScene(scene);
            primaryStage.show();
        } catch(Exception e) { e.printStackTrace();}
    }
}
