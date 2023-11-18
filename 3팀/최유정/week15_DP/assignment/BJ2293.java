import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class BJ2293 {
    private static int N;
    private static int K;
    public static void main(String[] args)  throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        Deque<Integer> coin = new ArrayDeque<>();
        int maxCoin = 0;

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            coin.add(num);
            maxCoin = Math.max(maxCoin, num);
        }
        int[] dp = new int[Math.max(K, maxCoin) + 1];
        int c;
        while(!coin.isEmpty()){
            c = coin.poll();
            dp[c] += 1;
            for(int i = c; i <= K; i++){
                dp[i] += dp[i-c];
            }
        }
        System.out.println(dp[K]);

    }
}
