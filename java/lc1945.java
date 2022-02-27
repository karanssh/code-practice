public class lc1945 {
    public int getLucky(String s, int k) {
        
        //first transform 

        String ans = stringToWordViaCharVals(s);
        int sum=0;
        while(k-->0 && ans.length()>1)
        {   
            sum=0;
            for(int i=0;i<ans.length();i++)
            sum+=Character.getNumericValue(ans.charAt(i));
            
            ans=String.valueOf(sum);
        }
        return sum;
    }

    public String stringToWordViaCharVals(String s) {
        StringBuffer sb = new StringBuffer();
        for (char a: s.toCharArray()) {
            int value = a - 'a' +1;
            sb.append(value);

        }
        return sb.toString();
    }

    public int digitSum(int num) {
        int sum = 0;
        while (num>0) {
            int rem = num%10;
            sum += rem;
            num /= 10;
        }
        return sum;
    }
    public static void main(String[] args) {
        lc1945 ob = new lc1945();
        System.out.println(ob.getLucky("leetcode", 2));
    }
}
