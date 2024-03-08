package week23_DP.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/**
 * 12028KB    84ms
 */
public class BJ2225 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        double[][] grid = new double[K+1][N+1];
        for (int k = 0; k < K + 1; k++) {
            for (int n = 0; n < N + 1; n++) {
                if (k == 0) grid[k][n] = 0;
                else if (k == 1) grid[k][n] = 1;
                else if (n == 0) grid[k][n] = 1;
                else grid[k][n] = (grid[k-1][n] + grid[k][n-1]) % Math.pow(10, 9);
            }
        }

        double result = grid[K][N] % Math.pow(10, 9);
        String[] strResult = Double.toString(result).split("");
        StringBuilder sb = new StringBuilder();
        int strLen = strResult.length;
        if (strResult[strLen-2].equals("E")) {
            int E = Integer.parseInt(strResult[strLen-1]); // 10의 E승
            for (int i = 0; i <= strLen-3; i++) {
                if (strResult[i].equals(".")) {
                    continue;
                }
                sb.append(strResult[i]);
            }
            // zeros = E - (문자열길이-4)
            int zeros = E - (strLen - 4);
            if (zeros != 0) {
                for (int i = 0; i < zeros; i++) {
                    sb.append(0);
                }
            }
        } else {
            for (int i = 0; i <= strLen-3; i++) {
                sb.append(strResult[i]);
            }
        }
        System.out.println(sb);
    }
}