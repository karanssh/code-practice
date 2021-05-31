import java.io.*; 
public class q2 {
    public static String q2Impl(String inputData) {
        if (inputData.length() <=1) {
            return inputData;
        }
        if (inputData.charAt(0) ==inputData.charAt(1)) {
            return q2Impl(inputData.substring(1));
        } else {
            return inputData.charAt(0) + q2Impl(inputData.substring(1));
        }
      
        
    }
    public static void main(String[] args) {
     String test1 = "abbaca"; 
     String test2 = q2Impl(test1);
     System.out.println("the value is :" + test2);   
    }
}
