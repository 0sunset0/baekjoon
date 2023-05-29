package com.sunset.baekjoon.math.baekjoon21919;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.System.exit;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<Integer> prime = new HashSet<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (isPrime(num)) {
                prime.add(num);
            }
        }

        if (prime.size() == 0) {
            System.out.println(-1);
            exit(0);
        }
        long result = 1;
        for (Integer num : prime) {
            result *= num;
        }
        System.out.println(result);

    }

    private static boolean isPrime(int num) {
        if (num == 2 || num == 3) {
            return true;
        }

        for (int i = 2; i < Math.sqrt(num)+1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

