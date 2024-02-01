package week20.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 	20592KB	388ms
 */
public class BJ11403 {
    static int[][] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        for(int i=0; i<n; i++){
            String[] input = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                grid[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                for (int k=0; k<n; k++){
                    if (grid[j][i] == 1 && grid[i][k] == 1){
                        grid[j][k] = 1;
                    }
                }
            }
        }

        for (int[] row : grid){
            for (int elem : row){
                System.out.print(elem + " ");
            }
            System.out.println();
        }
    }
}
