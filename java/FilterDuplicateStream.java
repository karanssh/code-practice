import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

// Java class to stream an arrya and remove its duplicates
public class FilterDuplicateStream {
    public static void main(String[] args) {
        int[] duplicateArr = { 1, 2, 3, 4, 3, 2 };
        int[] noduplicates = removeDuplicates(duplicateArr);
        System.out.println(Arrays.toString(noduplicates));
    }

    static public int[] removeDuplicates(int[] nums) {
        Set<Integer> output = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int len = output.size();
        int[] output2 = new int[len];
        int i = 0;
        for (Integer test : output) {
            output2[i++] = test;

        }
        return output2;
    }
}