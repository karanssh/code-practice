public class lc680 {
    public static boolean validPalindrome(String s) {
        int j = s.length()-1;
        int count=0;
        for (int i=0; i<s.length();i++) {
            if (s.charAt(i)!=s.charAt(j)) {
                if (count>1) {
                    return false;
                }
                count++;
            }
            j--;
        }

        return true;
    }
    public static void main(String[] args) {
        System.out.println(validPalindrome("abca")); // true

        System.out.println(validPalindrome("abba")); // true

        System.out.println(validPalindrome("aba")); // true

       

        
        System.out.println(validPalindrome("abc")); // false
    }
}
