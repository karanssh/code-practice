package cses;

import java.util.Scanner;

public class cs1069 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); 
        String s = sc.next();
        System.out.println(findReps(s));
        // System.out.println(findReps("ATTCGGGA"));
        // System.out.println(findReps("ATTCGGGG"));
        sc.close();

    }

    public static int findReps(String s) {
        int reps = 0;
        s = s.toUpperCase() + "L";
        // this is a nice stupid hack to make this work
        // but it messes up speed of running program
        // should probably use a string buffer or just change logic 
        // to handle some edge case where its all AAAA or ATTTTT or similar
        // but I am a lazy person

        char[] arr = s.toCharArray();
        int start = 0;
        for (int i = 0; i<arr.length-1; i++) {
             
            if (arr[i+1] != arr[i]) {
                //contigous cycle has been broken 
               int maxSoFar = i- start +1;
               reps = Math.max(reps, maxSoFar);

               start = i+1;
            }


        }

        return reps;
    }
}
