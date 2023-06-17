package com.sunset.baekjoon.binary_search.baekjoon2417;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static long n, key;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Long.parseLong(br.readLine());

        long sqrt = (long) Math.sqrt(n);
        if (sqrt*sqrt < n) {
            key =  sqrt+1;
        } else {
            key = sqrt;
        }
        binarySearch(1, n);

    }

    private static void binarySearch(long start, long end) {
        long mid = (start + end) / 2 ;


        if (start < end) {
            if (mid == key) {
                System.out.println(mid);

            } else if (mid > key) {
                if (start <= mid - 1)
                    binarySearch(start, mid - 1);

            } else if (mid < key) {
                if (mid+1 <= end)
                    binarySearch(mid + 1, end);

            }
        } else {
            System.out.println(mid);
        }
    }
}
