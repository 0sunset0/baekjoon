package com.sunset.baekjoon.graphTraversal.baekjoon11725;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] parent;

    static List<ArrayList<Integer>> graph = new ArrayList<>();
    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        parent = new int[n + 1];

        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }


        parent[0] = 1;
        parent[1] = 1;

        bfs(1);

        for (int i = 2; i < n + 1; i++) {
            System.out.println(parent[i]);
        }


    }

    public static void bfs(int node) {
        queue.offer(node);

        while (!queue.isEmpty()) {
            Integer integer = queue.poll();

            for (Integer i : graph.get(integer)) {
                if (parent[i] == 0) {
                    parent[i] = integer;
                    queue.add(i);
                }
            }
        }

    }

}
