
package cses;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class cs1068 {
    public static void main(String[] args) {
        weirdAlgorithm();
    }

    public static void weirdAlgorithm() {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextInt();
        sc.close();

        List<Long> ans = new ArrayList<>();
        if (n < 1) {
            return;
        }
        if (n == 1) {
            System.out.println(n);
            return;
        }

        while (n != 1) {

            ans.add(n);
            if (n % 2 == 0) {
                n = n / 2;

                // n is even
            } else {
                n = n * 3 + 1;
            }

        }

        ans.add(n);

        for (long a : ans) {
            System.out.print(a + " ");
        }

    }
}
