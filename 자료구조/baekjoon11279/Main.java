package com.sunset.baekjoon.data_structure.baekjoon11279;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

    static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        int num = Integer.parseInt(br.readLine());

        for (int i = 0; i < num; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (priorityQueue.size() == 0) {
                    System.out.println(0);
                } else {
                    System.out.println(priorityQueue.poll());
                }
            } else {
                priorityQueue.add(x);
            }
        }
    }
}
