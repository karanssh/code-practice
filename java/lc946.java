import java.util.ArrayDeque;
import java.util.Deque;

public class lc946 {
    public boolean validateStackSequences(int[] pushed, int[] popped) {

        Deque<Integer> st = new ArrayDeque<Integer>();

        int j = 0; 
        
        for(int val : pushed){
            st.push(val); 
            while(!st.isEmpty() && st.peek() == popped[j]){ 
                st.pop(); 
                j++; 
            }
        }
        return st.isEmpty();
    }
    public static void main(String[] args) {
        int[] pushed = new int[]{1,2,3,4,5};
        int[] popped = new int[]{4,5,3,2,1};


        lc946 obj  = new lc946();

        System.out.println( obj.validateStackSequences(pushed, popped));
       
    }
}
