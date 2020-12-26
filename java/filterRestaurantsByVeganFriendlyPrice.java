import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

//https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance
class filterRestaurantsByVeganFriendlyPrice {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
            return Arrays.stream(restaurants)
            .filter(x->{
                return veganFriendly==1?x[2]==1:true;
            })
            .filter(x->x[3]<=maxPrice)
            .filter(x->x[4]<=maxDistance)
            .sorted(new Comparator<int[]>(){
                @Override
                public int compare(int[] x1, int[] x2){
                    return x2[1]==x1[1]?x2[0]-x1[0]:x2[1]-x1[1];
                }
            })
            .map(x->x[0])
            .collect(Collectors.toList());
    }
}