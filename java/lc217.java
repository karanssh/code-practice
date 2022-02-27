import java.util.HashMap;
import java.util.Map;

public class lc217 {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> numsCount = new HashMap<>();
    
        for (int a: nums) {
            if (!numsCount.containsKey(a)) {
                numsCount.put(a, true);
            } else {
                return true;
            }
        }
        
        return false;
    }
} 
