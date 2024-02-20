package week21_Implementation.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 295628KB	660ms
 */
public class BJ2589 {

    public static class xylen{
        int x;
        int y;
        int len;
        public xylen(int x, int y, int len){
            this.x = x;
            this.y = y;
            this.len = len;
        }
    }

    static int n, m; // row, col
    static String[][] grid;
    static int[][] visited;

    // 새 좌표가 범위 내에 있는지 확인
    static boolean in_range(int x, int y){
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    // dfs
    static int[] dx = new int[] {1, 0, -1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};

    static int bfs(xylen xylen) {
        int result = 0;
        Queue<xylen> queue = new LinkedList<>();
        queue.add(xylen);
        visited[xylen.x][xylen.y] = 1;

        while(!queue.isEmpty()){
            xylen curr = queue.poll();
            for (int i=0; i<4; i++){
                int new_x = curr.x + dx[i];
                int new_y = curr.y + dy[i];

                if (in_range(new_x, new_y) && grid[new_x][new_y].equals("L") && visited[new_x][new_y] == 0){
                    visited[new_x][new_y] = 1;
                    queue.add(new xylen(new_x, new_y, curr.len + 1));
                    result = Math.max(result, curr.len + 1);
                }
            }
        }
        return result;
    }
    static void initialize(){
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                visited[i][j] = 0;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        // grid 초기화
        grid = new String[n][m];
        for (int i=0; i<n; i++){
            input = br.readLine().split("");
            for (int j=0; j<m; j++){
                grid[i][j] = input[j];
            }
        }
        // visited 초기화
        visited = new int[n][m];

        int maxLen = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (grid[i][j].equals("L")){
                    initialize();
                    int result = bfs(new xylen(i, j, 0));
                    maxLen = Math.max(result, maxLen);
                }
            }
        }
        System.out.println(maxLen);
    }
}
