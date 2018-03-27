import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class BoardGame {
    char [][] board = new char [3][3];

    public void retrieveChords(char player){
        Scanner scanner = new Scanner(System.in);
        int x, y;
        do{
            System.out.printf("\nPlayer %c Row: ", player);
            x = scanner.nextInt();
        }while(x == 0);

        do{
            System.out.printf("\nPlayer %c Column: ", player);
            y = scanner.nextInt();
        }while(y == 0);

        board[x-1][y-1] = player;
    }

    public void printBoard(){
        for (char [] arr : board){
            for (char num : arr){
                if (num != 0) {
                    System.out.print(Character.toString(num) + "|");
                }
                else{
                    System.out.print(" |");
                }
            }
            System.out.println("\n_________");
        }
    }

    public static void main(String[] args) {
        BoardGame game = new BoardGame();

        game.printBoard();
        while (true){
            game.retrieveChords('x');
            game.retrieveChords('o');
            game.printBoard();
        }
    }

}
