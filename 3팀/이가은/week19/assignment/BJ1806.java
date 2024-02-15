package week19.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ1806 {
    public static int min_len = 100000;
    public static int curr_len = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int s = Integer.parseInt(input[1]);

        String[] nums = br.readLine().split(" ");
        for (int i=0; i<n-1; i++){      // i = 0~n-2
            if (s <= Integer.parseInt(nums[i])) {
                min_len = 1;
                break;
            }
            for (int j=i; j<n; j++) {   // j = i~n-1
                curr_len += 1;
            }
        }
    }
}
