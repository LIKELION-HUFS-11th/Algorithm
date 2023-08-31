import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1931{
	private static int N, start, end, total, maxEnd;
	private static int[][] arr;
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());

		arr = new int[N][2];

		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			start = Integer.parseInt(st.nextToken());
			end = Integer.parseInt(st.nextToken());
			int[] temp = {end, start};
			arr[i] = temp;
		}
		Arrays.sort(arr, (x, y)-> x[0]==y[0] ? x[1]-y[1]  : x[0]-y[0]);
		for(int[] a : arr) {
			if (maxEnd <= a[1]) {
				total += 1;
				maxEnd = a[0];
			}
		}

		System.out.println(total);
	}
}