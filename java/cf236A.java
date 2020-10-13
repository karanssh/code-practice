import java.util.*;

public class cf236A {
  public static void main(String[] args) {
    // System.out.println("Hello world!");
    Scanner sc = new Scanner(System.in);
    
      String input = sc.next();
      int out = printDistinct(input);
      if (out %2 ==0 ){
System.out.println("CHAT WITH HER!");
      }else {
System.out.println("IGNORE HIM!");
      }
      sc.close();
      
   
    // printDistinct("kkaran");
  }
  static int printDistinct(String str) {
    Set<Character> origSet = new LinkedHashSet<Character>();
    StringBuilder concat = new StringBuilder();
    for (int i = 0; i < str.length(); i++) {
        if (origSet.add(str.charAt(i))) {
            concat.append(str.charAt(i));
        }
    }
    return concat.length();
}
}