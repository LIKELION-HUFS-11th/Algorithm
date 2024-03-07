package week22.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken()); // 이미 가지고 있는 랜선의 개수
        int N = Integer.parseInt(st.nextToken()); // 필요한 랜선의 개수

        int total = 0;
        int[] lines = new int[K];
        int length;
        for (int i = 0; i < K; i++) {
            length = Integer.parseInt(br.readLine());
            total += length;
            lines[i] = length;
        }

        int min = 0, max = total++, mid = 0;
        while (min < max) {
            mid = (min + max) / 2;

            long cnt = 0;

            for (int i = 0; i < K; i++) {
                cnt += (lines[i] / mid);
            }

            if (cnt < N) {
                max = mid;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(min-1);
    }
}
