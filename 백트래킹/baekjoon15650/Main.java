package com.sunset.baekjoon.backTracking.baekjoon15649;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int[] result;
    static int n;
    static int m;
    static boolean[] visited;


    public static void main(String[] args) throws IOException {
        //입력값 받기
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        result = new int[m];
        visited = new boolean[n + 1];
        dfs(1, 0);
    }

    public static void dfs(int num, int count){
        if (count == m){
            for (int i : result) {
                System.out.print(i);
                System.out.print(" ");
            }
            System.out.println();
            return;
        }

        for (int i = num; i < n + 1; i++) {
            if (visited[i] == false) {
                visited[i] = true;
                result[count] = i;
                count+=1;
                dfs(i, count);
                visited[i] = false;
                count-=1;
            }

        }


    }
}
