package cses;

import java.util.Scanner;

public class cs1094 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i=0; i<n; i++) {
            nums[i] = sc.nextInt();
        }
        
        System.out.println(findIncreasingArray(nums));
       
        sc.close();

    }

    public static long findIncreasingArray(int[] nums) {
        long reps = 0;
        for (int i = 1; i<nums.length; i++) {
             
            if (nums[i] < nums[i-1]) {
                // i th position must be 
                // equal to i-1 th position
                reps += nums[i-1]- nums[i];
                nums[i]= nums[i-1];
            }


        }

        return reps;
    }
}
