package week23_DP.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/**
 *     134832KB  2100ms
 */
public class BJ11660 {
    static int N, M;
    static int[][] grid;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        grid = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                if (i == 0) {
                    if (j== 0) grid[i][j] = Integer.parseInt(st.nextToken());
                    else grid[i][j] = grid[i][j-1] + Integer.parseInt(st.nextToken());
                } else if (j == 0) {
                    grid[i][j] = grid[i-1][j] + Integer.parseInt(st.nextToken());
                } else {
                    grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1] + Integer.parseInt(st.nextToken());
                }
            }
        }

        int x1, y1, x2, y2;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken()) - 1;
            y1 = Integer.parseInt(st.nextToken()) - 1;
            x2 = Integer.parseInt(st.nextToken()) - 1;
            y2 = Integer.parseInt(st.nextToken()) - 1;

            int sum = 0;
            if (x1 == 0 && y1 == 0) sum = grid[x2][y2];
            else if (x1 == 0 && y1 != 0) sum = grid[x2][y2] - grid[x2][y1-1];
            else if (x1 != 0 && y1 == 0) sum = grid[x2][y2] - grid[x1-1][y2];
            else sum = grid[x2][y2] - grid[x1-1][y2] - grid[x2][y1-1] + grid[x1-1][y1-1];
            System.out.println(sum);
        }
    }

}