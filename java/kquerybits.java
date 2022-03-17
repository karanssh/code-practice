
/* Java Program to find the number of elements
   in a range L to R having the Kth bit as set */

public class kquerybits {

  // Maximum bits required in binary representation
  // of an array element
  static int MAX_BITS = 32;

  /*
   * Returns true if n has its kth bit as set,
   * else returns false
   */
  static boolean isKthBitSet(int n, int k) {
    if ((n & (1 << (k - 1))) != 0) {
      return true;
    }
    return false;
  }

  // Return pointer to the prefix sum array
  static int[][] buildPrefixArray(int N, int[] arr) {

    // Build a prefix sum array P[][]
    // where P[i][j] represents the number of
    // elements from 0 to i having the jth bit as set
    int[][] P = new int[N + 1][MAX_BITS + 1];
    for (int i = 0; i <= MAX_BITS; i++) {
      P[0][i] = 0;
    }
    for (int i = 0; i < N; i++) {
      for (int j = 1; j <= MAX_BITS; j++) {

        // prefix sum from 0 to i for each bit
        // position jhas the value of sum from 0
        // to i-1 for each j
        if (i != 0) {
          P[i][j] = P[i - 1][j];
        }

        // if jth bit set then increment P[i][j] by 1
        boolean isJthBitSet = isKthBitSet(arr[i], j);
        if (isJthBitSet) {
          P[i][j]++;
        }
      }
    }
    return P;
  }

  /*
   * Returns the answer for each query with range
   * L to R querying for the number of elements with
   * the Kth bit set in the range
   */
  static int answerQuery(int L, int R, int K, int[][] P) {

    /*
     * Number of elements in range L to R with Kth
     * bit set = (Number of elements from 0 to R with
     * kth bit set) - (Number of elements from 0 to L-1
     * with kth bit set)
     */
    if (L != 0) {
      return P[R][K] - P[L - 1][K];
    } else {
      return P[R][K];
    }
  }

  // Print the answer for all queries
  static void answerQueries(int[][] queries, int Q,
      int[] arr, int N) {

    // Build Prefix Array to answer queries efficiently
    int[][] P = buildPrefixArray(N, arr);
    int query_L, query_R, query_K;
    for (int i = 0; i < Q; i++) {
      query_L = queries[i][0] - 1;
      query_R = queries[i][1] - 1;
      query_K = queries[i][2];
      System.out.println("Result for Query " + (i + 1) + " = " + answerQuery(query_L, query_R, query_K, P));
    }
  }

  // Driver Code
  public static void main(String[] args) {
    int[] arr = { 8, 9, 1, 3 };
    int N = arr.length;

    /*
     * queries[][] denotes the array of queries
     * where each query has three integers
     * query[i][0] -> Value of L for ith query
     * query[i][0] -> Value of R for ith query
     * query[i][0] -> Value of K for ith query
     */
    int[][] queries = { { 1, 3, 4 }, { 2, 4, 1 } };
    int Q = queries.length;
    answerQueries(queries, Q, arr, N);
  }
}
