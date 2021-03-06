Class shortestDistanceToCharacter {
	public int[] shortestToChar(String S, char C) {
		int n = S.length();
		  int[] res = new int[n];
		  int prev = -n;
  
		  for (int i = 0; i < n; ++i) {
			  if (S.charAt(i) == C) prev = i;
			  res[i] = i - prev;
		  }
  
		  prev = -n;
		  for (int i = n-1; i >= 0; --i) {
			  if (S.charAt(i) == C) prev = i;
			  res[i] = Math.min(res[i], Math.abs(prev - i));
		  }
  
		  return res;   
	  }
  }
}