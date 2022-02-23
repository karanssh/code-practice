import java.util.Arrays;

public class lc179 {
    public String largestNumber(int[] nums) {

        Integer[] numsInteger = Arrays.stream(nums).boxed().toArray(Integer[]::new);

        Arrays.sort(numsInteger, (a, b) -> {

            String s1 = a.toString() + b.toString();
            String s2 = b.toString() + a.toString();

            return s2.compareTo(s1);
            
        });

        //System.out.println(numsInteger);
        String outStr = "";
        
        for (Integer a : numsInteger ) {
            outStr += a.toString();
        }
        try {
            Long aa = Long.parseLong(outStr);
            return aa.toString();
        } catch(Exception e) {
            return outStr;
        }
        
    }

    public static void main(String[] args) {
        lc179 ob = new lc179();
        int[] input = { 999999998,999999997,999999999 };
        System.out.println(ob.largestNumber(input));

        int[] input2 = { 3,30,34,5,9 };
        System.out.println(ob.largestNumber(input2));
    }
}
