package week21_Implementation.assignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 	261972KB 576ms
 */
public class BJ1138 {
    static int n;

    // permutation
    static List<int[]> tries = new ArrayList<>(); // 가능한 순열 저장하는 리스트
    static int[] numbers;
    static boolean[] visited;
    static void permutation(int index) {
        if (index == n) { 			// 종료파트
            int[] temp = numbers.clone();
            tries.add(temp);
            return;
        } else { // 재귀파트
            for (int i=1; i<=n; i++) {
                if (visited[i]) continue;
                numbers[index] = i;
                visited[i] = true;
                permutation(index + 1);
                visited[i] = false;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] info = new int[n+1];
        for (int i=1; i<=n; i++) info[i] = Integer.parseInt(input[i-1]);

        // 초기화
        numbers = new int[n];
        visited = new boolean[n+1];
        visited[0] = true;
        permutation(0); // 가능한 순열 만들기
//        for (int[] elem : tries) System.out.println(Arrays.toString(elem));
        boolean flag;
        for (int[] elem : tries) {
//            System.out.println(Arrays.toString(elem));
            flag = true;
            for (int i=0; i<n; i++){
                if (i == 0 && info[elem[i]]!=0) {
                    flag = false;
                    break;
                } else if (i == 0 && info[elem[i]] == 0) {
                    continue;
                }

                int cnt = 0;
                for (int j=0; j<i; j++){
                    if (elem[j] > elem[i]) cnt++;
                }
                if (info[elem[i]] != cnt) {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                for(int num : elem) System.out.print(num + " ");
                break;
            }
        }
    }
}

