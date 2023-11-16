import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ1463 {
    private static int N;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int[] dp = new int[N+1];

        if (N >= 2) dp[2] = 1;
        if (N >= 3) dp[3] = 1;

        for(int i=4; i <= N; i++){
            dp[i] = dp[i-1] + 1;
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i/2]+1);
            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i/3]+1);
        }
        System.out.println(dp[N]);
    }
}
