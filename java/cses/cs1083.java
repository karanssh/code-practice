package cses;

import java.util.Scanner;

public class cs1083 {
    public static void main(String[] args) {
        findMissingNum();
    }

    public static void findMissingNum() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n]; 

        for (int i=0; i<n-1; i++) {
            int inp = sc.nextInt();
            nums[inp-1] = inp;
        }

        for (int i=0; i<nums.length; i++) {
            if (nums[i]!= i+1) {
                System.out.println(i+1);
            }
        }
        sc.close();
    }

    public static void findMissingNumV2() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n]; 
        int sumExpect = (n * (n+1))/2;
        int sumActual = 0;

        for (int i=0; i<n-1; i++) {
            sumActual += sc.nextInt();
            
        }

        sc.close();
    }
}
