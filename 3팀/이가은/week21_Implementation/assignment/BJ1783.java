package week21_Implementation.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/**
 * 	14388KB	124ms
 */
public class BJ1783 {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int result;
        if (n == 1) {
            result = 1;
        } else if (n == 2){
            result = Math.min((m-1)/2+1, 4);
        } else if (m < 7){
            result = Math.min(m, 4);
        } else {
            result = 5 + (m-7);
        }

        System.out.println(result);
    }
}