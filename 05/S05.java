import java.io.BufferedReader;
import java.io.FileReader;
import java.util.LinkedList;

public class S05 {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new FileReader("05.in"));
    String line;
    LinkedList<Character>[] stacks = new LinkedList[9];
    LinkedList<Character>[] stacks2 = new LinkedList[9];
    LinkedList<Character> tmp = new LinkedList<>();
    for (int i = 0; i < stacks.length; i++) {
      stacks[i] = new LinkedList<>();
      stacks2[i] = new LinkedList<>();
    }
    line = reader.readLine();
    do {
      for (int i = 0; i < stacks.length; i++) {

        if (line.length() >= 1 + i * 4 && line.charAt(1 + i * 4) != ' ') {
          stacks[i].addLast(line.charAt(1 + i * 4));
          stacks2[i].addLast(line.charAt(1 + i * 4));
        }
      }

    } while ((line = reader.readLine()) != null && line.charAt(1) != '1');
    reader.readLine();
    line = reader.readLine();

    do {
      //move 3 from 2 to 9
      var lines= line.split(" ");
      int num = Integer.parseInt( lines[1]);
      int from = Integer.parseInt( lines[3])-1;
      int to = Integer.parseInt( lines[5])-1;
      for (int i = 0; i < num; i++) {
        stacks[to].push(stacks[from].pop());
        tmp.push(stacks2[from].pop());
      }
      while (!tmp.isEmpty()){
        stacks2[to].push(tmp.pop());
      }

    } while ((line = reader.readLine()) != null);
    for (int i = 0; i < stacks.length; i++) {
      System.out.print(stacks[i].peek());
    }
    System.out.println();
    for (int i = 0; i < stacks2.length; i++) {
      System.out.print(stacks2[i].peek());
    }
    System.out.println();
  }
}
