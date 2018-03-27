import java.util.ArrayList;
import java.util.HashMap;

public class BoardGame {

    private ArrayList<int[]> coordinates;
    private HashMap<Character, int []> coordinateMap;

    BoardGame(){
        coordinates = new ArrayList<>();
        coordinateMap = new HashMap<>();
    }

    public ArrayList<int[]> getCoordinates() {
        return coordinates;
    }

    public void plot(char character, int x, int y) {
        int [] cord = {x, y};
        coordinates.add(cord);
        coordinateMap.put(character, cord);
    }

    public void plot(){
        for (int [] cord : coordinateMap.get('x'));
    }
}
