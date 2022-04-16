public class lc991 {
    public int brokenCalc(int startValue, int target) {
        int ops =0;

       
        while (startValue!= target) {
            if ((target-startValue) < startValue) {
                startValue--;
            } else {
                startValue = 2*startValue;
            }
            ops++;
        }
        
        return ops;
    }
    public static void main(String[] args) {
        lc991 obj = new lc991();
        System.out.println(obj.brokenCalc(5, 8));
        
        System.out.println(obj.brokenCalc(2, 3));
        
        System.out.println(obj.brokenCalc(3, 10));
        
        System.out.println(obj.brokenCalc(4, 5)); 
    }
}
