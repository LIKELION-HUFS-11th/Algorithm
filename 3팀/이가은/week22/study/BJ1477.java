package week22.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BJ1477 {
    static void binarySearch(int road, List<Integer> breakpoints, int minLength) {
        int start = 0;
        int end = road - 1;
        int mid;
        while(start < end) {
            mid = (start + end) / 2;

            for (int i = 0; i < breakpoints.size(); i++) {
                minLength = Math.min(minLength, breakpoints.get(i) - mid);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 현재 휴게소의 개수
        int M = Integer.parseInt(st.nextToken()); // 더 지으려는 휴게소의 개수
        int L = Integer.parseInt(st.nextToken()); // 고속도로의 길이

        List<Integer> breakpoints = new LinkedList<>();
        Collections.sort(breakpoints);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            breakpoints.add(Integer.parseInt(st.nextToken()));
        }


    }
}
