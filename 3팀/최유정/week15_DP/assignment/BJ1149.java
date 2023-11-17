import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1149 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[][] paintCost = new int[N][3];
        int[][] dp = new int[N][3];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<3; j++){
                paintCost[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = paintCost[0][0];
        dp[0][1] = paintCost[0][1];
        dp[0][2] = paintCost[0][2];

        for(int i=1; i<N; i++){
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + paintCost[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + paintCost[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + paintCost[i][2];
        }

        int result = Arrays.stream(dp[N-1]).min().getAsInt();
        System.out.println(result);
    }
}
