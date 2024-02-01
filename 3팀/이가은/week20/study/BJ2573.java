package week20.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 	26260KB	472ms
 */

public class BJ2573 {
//    입력받기
//    그리드에서 0이 아닌 숫자가 나타나면 동서남북 탐색 후 바다인 것 개수 세기
//        바로 빼기
//    dfs로 덩어리 개수 탐색

    static int n, m;
    static int[][] grid; // 주어진 2차원 배열
    static int[][] nxt_grid; // 1년 지나 녹은 배열 저장
    static boolean[][] visited; // dfs 때 사용
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    // grid 돌면서 0이 아닌 곳은 동서남북 탐색해서 0의 개수만큼 빼기, 만약 grid가 전부 0일 시 false 리턴
    static boolean reset(){
        int cnt;
        boolean flag = true;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (grid[i][j] != 0){ // 만약 바다가 아니면
                    cnt = 0;
                    for (int k=0; k<4; k++){ // 4면 중 바다인 면 탐색
                        int new_i = i + dx[k];
                        int new_j = j + dy[k];
                        if (grid[new_i][new_j] == 0){
                            cnt += 1;
                        }
                    }
                    int melt = grid[i][j] - cnt; // 녹이기
                    if (melt <= 0){ // 녹았으면 0으로 세팅
                        nxt_grid[i][j] = 0;
                    } else {
                        nxt_grid[i][j] = melt;
                        flag = false; // 다 녹지 않았으면 false 리턴
                    }
                }
            }
        }
        return flag;
    }

    // grid, nxt_grid 초기화
    static void copy(){
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                grid[i][j] = nxt_grid[i][j];
                nxt_grid[i][j] = 0;
                visited[i][j] = false;
            }
        }
    }

    // 좌표가 범위 내에 있는지 확인(dfs 때 사용)
    static boolean in_range(int x, int y){
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    // 빙산 dfs로 탐색
    static void dfs(int x, int y){
        for (int i=0; i<4; i++){
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            if (in_range(new_x, new_y) && nxt_grid[new_x][new_y] != 0 && !visited[new_x][new_y]){
                visited[new_x][new_y] = true;
                dfs(new_x, new_y);
            }
        }
    }

    // 모든 좌표 돌면서 빙산의 개수 세기
    static int count(){
        int cnt = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (nxt_grid[i][j] != 0 && !visited[i][j]){
//                    System.out.println("dfs : " + i + ", " + j);
                    dfs(i, j);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        grid = new int[n][m];
        nxt_grid = new int[n][m];
        visited = new boolean[n][m];
        for (int i=0; i<n; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                grid[i][j] = Integer.parseInt(input[j]);
            }
        }

        int year = 0;
        while(true){
            boolean melted = reset();
            year += 1; // 한번 수행할 때마다 년도 추가
            if (melted){ // 만약 얼음이 분리되기 전에 다 녹으면 0 출력
                System.out.println(0);
                break;
            } else{ // 얼음이 다 녹지 않았을 경우
                int cnt = count(); // dfs로 빙산 개수 세기
                if (cnt >= 2){ // 빙산 개수가 2개 이상일 경우
                    System.out.println(year); // 빙산 개수 출력 후 break
                    break;
                } else { // 빙산 개수가 1개일 경우
                    copy(); // grid, nxt_grid, visited 초기화 후 다시 수행
                }
            }
        }
//        reset();
//        System.out.println();
//        System.out.println("org");
//        for (int[] row : grid){
//            System.out.println(Arrays.toString(row));
//        }
//        System.out.println("nxt");
//        for (int[] row : nxt_grid){
//            System.out.println(Arrays.toString(row));
//        }
//        copy();
//
//        reset();
//        System.out.println();
//        System.out.println("org");
//        for (int[] row : grid){
//            System.out.println(Arrays.toString(row));
//        }
//        System.out.println("nxt");
//        for (int[] row : nxt_grid){
//            System.out.println(Arrays.toString(row));
//        }
//
//        int cnt = count();
//        System.out.println("visited");
//        for (boolean[] row : visited){
//            System.out.println(Arrays.toString(row));
//        }
//        System.out.println("cnt: " + cnt);
    }
}
