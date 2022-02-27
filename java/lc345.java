public class lc345 {
        public String reverseVowels(String s) {

            char []str = s.toCharArray();
            int slow = 0, fast= str.length-1;

            while (slow<fast) {
                if (!isVowel(str[slow])) {
                    slow++;
                }
                if (!isVowel(str[fast])) {
                    fast--;
                }
                if (isVowel(str[slow]) && isVowel(str[fast])) {
                char temp = str[slow];
                str[slow] =  str[fast];
                str[fast] = temp;
                slow++;
                fast--;
                }
            }
            return new String(str);
            
        }

        public boolean isVowel(char ch) {
            if (ch =='a' ||ch =='e' || ch =='i'|| ch =='o' || ch =='u' ) {
                return true;
            }
            if (ch =='A' ||ch =='E' || ch =='I'|| ch =='O' || ch =='U' ) {
                return true;
            }
            return false;
        }

        public static void main(String[] args) {
            lc345 ob = new lc345();

            System.out.println(ob.reverseVowels("leetcode"));
        }
    
}
