package itmo;

import java.util.Scanner;

public class binsearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] numbers = new int[n];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        int[] searchTerms = new int[k];

        for (int i = 0; i < searchTerms.length; i++) {
            searchTerms[i] = sc.nextInt();
        }

        for (int searchItem : searchTerms) {
            if (binarySearch(numbers, searchItem)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

        sc.close();
    }

    public static boolean binarySearch(int[] array, int searchTerm) {

        int l = 0;
        int r = array.length - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            if (array[m] == searchTerm) {
                return true;
            } else if (array[m] < searchTerm) {
                l = m + 1;
            } else if (array[m] > searchTerm) {
                r = m - 1;
            }
        }

        return false;
    }
}
