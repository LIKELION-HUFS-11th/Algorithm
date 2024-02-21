package week19.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ17609 {
    public static boolean isPalin(String[] sArray){
        boolean flag = true;
        int length = sArray.length;
        int center = 0;
        if (length%2 == 0){ // length가 짝수인 경우
            center = (int)length/2;
        }
        else {              // length가 홀수인 경우
            center = (int)length/2;
        }
        for (int i=0; i<center; i++){
            if (sArray[i].equals(sArray[length - i - 1])){
                continue;
            } else {
                flag = false;
                break;
            }
        }
        return flag;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++){
            int result = 2;
            String[] sArr = br.readLine().split("");
            if (isPalin(sArr) == true){
                result = 0;
            } else {
                String[] destArr = new String[sArr.length - 1];
                for (int j = 0; j < sArr.length; j++) {
                    int removeIdx = j;
                    // 배열 구하기

                    if (isPalin(destArr) == true) {
                        result = 1;
                        break;
                    }
                }
            }
            System.out.println(result);
        }
    }
}
