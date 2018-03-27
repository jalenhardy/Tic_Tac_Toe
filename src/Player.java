import java.util.ArrayList;
import java.util.Scanner;

public class Player {
    private char character;
    private BoardGame game;
    private ArrayList<int []> coordinates;

    Player(char character, BoardGame game){
        this.character = character;
        this.game = game;
        coordinates = new ArrayList<>();
    }

    public void retrieveCordinates(){
        Scanner scanner = new Scanner(System.in);
        int x, y;
        // If the user inputted coordinates are the same as coordinates already plotted
        do{
            System.out.println("X Value: ");
            x = scanner.nextInt();
            System.out.println("Y Value: ");
            y = scanner.nextInt();

        }while(!checkCoordinates(x, y, game.getCoordinates()));

        // If coordinates are authentic
        game.plot(character, x, y);
    }

    private boolean checkCoordinates(int x, int y, ArrayList<int []> coordinates){
        boolean isSame = false;
        for (int i = 0; i < coordinates.size(); i++){
            int [] cord = coordinates.get(i);
            if (cord[0] == x || cord[1] == y){
                isSame = true;
            }
        }
        return isSame;
    }


}
