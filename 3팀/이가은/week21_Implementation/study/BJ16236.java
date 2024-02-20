package week21_Implementation.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class BJ16236 {
    static int n;
    static int[][] grid;
    static boolean[][] canVisit;
    static List<fish> fishList = new ArrayList<>();
    static List<fish> smallList;

    public static class fish {
        int x;
        int y;
        int size;
        int dist;
        public fish(int x, int y, int size){
            this.x = x;
            this.y = y;
            this.size = size;
        }

        @Override
        public String toString() {
            return "fish" + Integer.toString(size);
        }
    }

    // 사이즈가 자신보다 작은 물고기 찾기
    static void find_smaller(int size){
        smallList = new ArrayList<>();
        for (fish elem : fishList){
            if (elem.size < size) {
                smallList.add(elem);
            }
        }
    }

    // 자신보다 작은 물고기의 거리 찾기
    static void setRoad(int sharkX, int sharkY, int fishX, int fishY, int size){
        int startX = Math.min(sharkX, fishX);
        int startY = Math.min(sharkY, fishY);
        int finX = Math.max(sharkX, fishX);
        int finY = Math.max(sharkY, fishY);

        for (int i=startX; i<=finX; i++) {
            for (int j=startY; j<=finY; j++){
                if (grid[i][j] < size){
                    canVisit[i][j] = false;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        canVisit = new boolean[n][n];
        StringTokenizer st;
        for (int i=0; i<n; i++){
            st  = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++){
                int size = Integer.parseInt(st.nextToken());
                grid[i][j] = size;
                if (size != 0 && size != 9){
                    fishList.add(new fish(i, j, size));
                }
            }
        }
        find_smaller(3);
        for (fish elem : smallList){
            System.out.println(elem);
        }

    }
}
