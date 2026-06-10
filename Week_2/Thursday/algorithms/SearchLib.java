package Week_2.Thursday.algorithms;

/**
 * Pair exercise — implement linearSearch and binarySearch.
 * Precondition: sorted ascending, may contain duplicates; return any matching index.
 */

public class SearchLib {
    public static int linearSearch(int[] sorted, int target) {
        for (int i = 0; i < sorted.length; i++) {
            if (sorted[i] == target) {
                return sorted[i];
            }
        }
        return -1;
    }
}
