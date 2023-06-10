package com.sunset.baekjoon.two_pointer.baekjoon21921;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st1.nextToken());
        int x = Integer.parseInt(st1.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());

        int[] day = new int[n];
        for (int i = 0; i < n; i++) {
            day[i] = Integer.parseInt(st2.nextToken());
        }

        ArrayList<Integer> result = new ArrayList<>();
        int end = 0;
        int num = day[0];
        for (int start = 0; start < n; start++) {
            while (start <= end && end < n-1) {
                end++;
                num += day[end];
                if (end - start + 1 == x) {
                    result.add(num);
                    break;
                }
            }
            num -= day[start];
        }



        int max = 0;
        for (Integer integer : result) {
            if (integer > max) {
                max = integer;
            }
        }
        if (max == 0) {
            System.out.println("SAD");
            System.exit(0);
        }
        System.out.println(max);

        int count = 0;
        for (Integer integer : result) {
            if (integer == max) {
                count++;
            }
        }
        System.out.println(count);
    }
}
