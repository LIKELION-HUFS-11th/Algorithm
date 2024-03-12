package week23_DP.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 11864KB	92ms
 */
public class BJ11053 {
    static int N;
    static int[] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            grid[i] = Integer.parseInt(st.nextToken());
        }
        int result = findMaxCnt();
        System.out.println(result);
    }

    static int findMaxCnt() {
        int[] cntArr = new int[N];
        cntArr[0] = 1;

        for (int i = 1; i < N; i++) {
            int maxCnt = 0;
            for (int j = 0; j < i; j++) {
                if (grid[j] < grid[i] && maxCnt < cntArr[j]) maxCnt = cntArr[j];
            }
            cntArr[i] = maxCnt + 1;
        }

        int result = 1;
        for (int elem : cntArr) {
            if (result < elem) {
                result = elem;
            }
        }

        return result;
    }

}
