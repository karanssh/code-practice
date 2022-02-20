import java.util.HashMap;
import java.util.LinkedHashMap;

public class lc290 {
    public static boolean wordPattern(String pattern, String s) {

        String[] strs = s.split(" ");
        char[] patterns = pattern.toCharArray();

        if (strs.length != patterns.length) {
            return false;
        }

        HashMap<String, Character> wordToChar = new LinkedHashMap<>();
        HashMap<Character, String> charToWord = new LinkedHashMap<>();

        for (int i = 0; i < strs.length; i++) {
            if (wordToChar.containsKey(strs[i]) && ((patterns[i]==((wordToChar.get(strs[i])))))) {
                return false;

            } else {
                wordToChar.put(strs[i], patterns[i]);
                charToWord.put( patterns[i], strs[i]);

            }
        }

        for (int i = 0; i < strs.length; i++) {
            if (charToWord.containsKey(patterns[i]) && ((strs[i].equals((charToWord.get(patterns[i])))))) {
                return false;

            } else {
                wordToChar.put(strs[i], patterns[i]);
                charToWord.put( patterns[i], strs[i]);

            }
        }


        return true;
    }

    public static void main(String[] args) {

        System.out.println(wordPattern("abba","dog cat cat dog")); // true

        System.out.println(wordPattern("aba","dog dog dog")); // false

       

        System.out.println(wordPattern("abba", "dog cat cat fish")); // false

        System.out.println(wordPattern("aaaa", "dog cat cat dog")); // false
    }
}
