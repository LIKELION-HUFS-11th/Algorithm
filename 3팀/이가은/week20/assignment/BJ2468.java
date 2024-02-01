package week20.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 16792KB	264ms
 */
public class BJ2468 {
    static int N;
    static int[][] grid;
    static int[][] visited;
    static int maxHeight = Integer.MIN_VALUE;

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean in_range(int x, int y){
        return x >= 0 && x < N && y >= 0 && y < N;
    }
    static void dfs(int x, int y){
        for (int i=0; i<4; i++){
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            if (in_range(new_x, new_y) && visited[new_x][new_y] == 0){
                visited[new_x][new_y] = 1;
                dfs(new_x, new_y);
            }
        }
    }
    static int run(){
        int cnt = 0;
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (visited[i][j] == 0){
                    dfs(i, j);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
    // 침수된 지역 체크하는 함수
    static void setGrid(int height){
        for (int i=0; i<N; i++){
            for (int j = 0; j < N; j++) {
                if (grid[i][j] <= height) {
                    visited[i][j] = 2;
                }
            }
        }
    }

    static void initialize(){
        for (int i=0; i<N; i++){
            for (int j = 0; j < N; j++) {
                visited[i][j] = 0;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new int[N][N];
        visited = new int[N][N];
        for (int i=0; i<N; i++){
            String[] input = br.readLine().split(" ");
            for (int j=0; j<N; j++) {
                grid[i][j] = Integer.parseInt(input[j]);
                maxHeight = Math.max(maxHeight, grid[i][j]);
            }
        }

        int temp;
        int maxSafe = 0;
        for (int i=0; i<maxHeight; i++){
            initialize();
            setGrid(i);
            temp = run();
            maxSafe = Math.max(maxSafe, temp);
        }

        System.out.println(maxSafe);
    }
}
