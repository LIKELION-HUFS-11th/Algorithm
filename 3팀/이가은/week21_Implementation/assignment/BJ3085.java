package week21_Implementation.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/**
 * 15192KB	180ms
 */
public class BJ3085 {
    static int n;
    static String[][] grid;
    static int result;

    // 같은 거 최대개수 (십자가)
    static int findSame(int x, int y) {
        String prev = grid[0][y];
        int rowCnt = 1, maxRow = 1;
        for (int i=1; i<n; i++) {
            if (prev.equals(grid[i][y])) {
                rowCnt += 1;
                maxRow = Math.max(maxRow, rowCnt);
                prev = grid[i][y];
            } else {
                rowCnt = 1;
                prev = grid[i][y];
            }
        }

        prev = grid[x][0];
        int colCnt = 1, maxCol = 1;
        for (int i=1; i<n; i++) {
            if (prev.equals(grid[x][i])) {
                colCnt += 1;
                maxCol = Math.max(maxCol, colCnt);
                prev = grid[x][i];
            } else {
                colCnt = 1;
                prev = grid[x][i];
            }
        }

        return Math.max(maxRow, maxCol);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        grid = new String[n][n];
        for (int i=0; i<n; i++) {
            String[] input = br.readLine().split("");
            for (int j=0; j<n; j++) {
                grid[i][j] = input[j];
            }
        }

        for (int i=0; i<n-1; i++) {
            for (int j=0; j<n; j++) {
                String temp = grid[i][j];
                grid[i][j] = grid[i+1][j];
                grid[i+1][j] = temp;
                int maxTemp = Math.max(findSame(i, j), findSame(i+1, j));
                result = Math.max(result, maxTemp);

                temp = grid[i][j];
                grid[i][j] = grid[i+1][j];
                grid[i+1][j] = temp;
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n-1; j++) {
                String temp = grid[i][j];
                grid[i][j] = grid[i][j+1];
                grid[i][j+1] = temp;
                int maxTemp = Math.max(findSame(i, j), findSame(i, j+1));
                result = Math.max(result, maxTemp);

                temp = grid[i][j];
                grid[i][j] = grid[i][j+1];
                grid[i][j+1] = temp;
            }
        }
        System.out.println(result);
    }
}