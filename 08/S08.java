import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
record Pos(int x, int y){}
public class S08 {
  public static void main(String[] args) throws Exception{

    var br = new BufferedReader(new FileReader("08.in"));
    ArrayList<List<Integer>> arr = new ArrayList<>();
    String line;
    while (( line = br.readLine())!=null){
      arr.add(line.chars().map(c -> (int)(c-'0')).boxed().collect(Collectors.toList()));
    }
    br.close();
    HashSet<Pos> visible = new HashSet<>();
    for(int x=0;x<arr.size();++x){
      int max =-1;
      for(int y=0;y<arr.get(x).size();++y){
        if (arr.get(x).get(y)>max){
          visible.add(new Pos(x, y));
          max = arr.get(x).get(y);
        }
      }
      max =-1;
      for(int y=arr.get(x).size()-1;y>=0;--y){
        if (arr.get(x).get(y)>max){
          visible.add(new Pos(x, y));
          max = arr.get(x).get(y);
        }
      }
    }
    for(int y=0;y<arr.get(0).size();++y){
      int max =-1;
      for(int x=0;x<arr.size();++x){
        if (arr.get(x).get(y)>max){
          visible.add(new Pos(x, y));
          max = arr.get(x).get(y);
        }
      }
      max =-1;
      for(int x=arr.size()-1;x>=0;--x){
        if (arr.get(x).get(y)>max){
          visible.add(new Pos(x, y));
          max = arr.get(x).get(y);
        }
      }
    }
    System.out.println(visible.size());
    int max =-1;
    for(int x=1;x<arr.size()-1;++x){
      for(int y=1;y<arr.get(x).size()-1;++y){
        int prod=1;
        int cnt=1;
        int a=x+1;
        while(a<arr.size()-1 && arr.get(a).get(y)<arr.get(x).get(y)){
          ++cnt;
          ++a;
        }
        prod*=cnt;
        cnt=1;
        a=x-1;
        while(a>0 && arr.get(a).get(y)<arr.get(x).get(y)){
          ++cnt;
          --a;
        }
        prod*=cnt;
        cnt=1;
        a=y+1;
        while(a<arr.get(x).size()-1 && arr.get(x).get(a)<arr.get(x).get(y)){
          ++cnt;
          ++a;
        }
        prod*=cnt;
        cnt=1;
        a=y-1;
        while(a>0 && arr.get(x).get(a)<arr.get(x).get(y)){
          ++cnt;
          --a;
        }
        prod*=cnt;
        if (max<prod){
          max=prod;
        }

      }
    }
    System.out.println(max);

  }
}
