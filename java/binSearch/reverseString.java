

class Solution {
    public String[] solve(String[] sentence) {

        int left = 0;
        int right = sentence.length - 1;

        while (left <= right) {
            String temp1 = sentence[left];
            sentence[left] = sentence[right];
            sentence[right] = temp1;
            left++;
            right--;
        }

        left = 0;
        right =0;
        for (int i = 0; i <= sentence.length - 1; i++) {
            if (sentence[i] == " " || i == sentence.length-1) {
                right =i-1;
                if (i == sentence.length-1) {
                    right =i;
                }
                while (left <= right) {
                    String temp1 = sentence[left];
                    sentence[left] = sentence[right];
                    sentence[right] = temp1;
                    left++;
                    right--;
                }
                left =i+1;
            }
            
        }

        return sentence;

    }

    public static void main(String[] args) {
        Solution ob  = new Solution();
        String[] input = { "h", "i", " ", "w", "o", "r", "l", "d" };
        ob.solve(input);
    }
}