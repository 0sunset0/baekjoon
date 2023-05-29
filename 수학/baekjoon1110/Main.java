package com.sunset.baekjoon.math.baekjoon1110;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int newNum;
    private static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());


        count += 1;
        if (num < 10) {
            newNum = num * 10 + num;
        } else {
            newNum = ((num % 10) * 10) + (((num % 10) + num / 10) % 10);
        }

        while (newNum != num) {
            count += 1;
            if (newNum < 10) {
                newNum = newNum * 10 + newNum;
            } else {
                newNum = ((newNum % 10) * 10) + (((newNum % 10) + newNum / 10) % 10);
            }
        }

        System.out.println(count);

    }
}
