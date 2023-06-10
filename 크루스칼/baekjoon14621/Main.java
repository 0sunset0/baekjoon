package com.sunset.baekjoon.kruskal.baekjoon14621;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st1.nextToken());
        int m = Integer.parseInt(st1.nextToken());
        String[] school = br.readLine().split(" ");

        int[] parent = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }
        int result = 0;
        ArrayList<Edge> edges = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());
            int cost = Integer.parseInt(st2.nextToken());
            edges.add(new Edge(a, b, cost));
        }

        edges.sort((a, b)-> (a.cost - b.cost));

        int count = 0;
        for (Edge edge : edges) {
            if (findParent(edge.a, parent) != findParent(edge.b, parent)) {
                if (!school[edge.a - 1].equals(school[edge.b - 1])) {
                    union(edge.a, edge.b, parent);
                    result += edge.cost;
                    count+=1;
                }
            }
        }
        if (count != n - 1) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    private static void union(int a, int b, int[] parent) {
        int aRoot = findParent(a, parent);
        int bRoot = findParent(b, parent);
        if (aRoot > bRoot) {
            parent[aRoot] = findParent(b, parent);
        } else {
            parent[bRoot] = findParent(a, parent);
        }
    }

    private static int findParent(int x, int[] parent) {
        if (x != parent[x]) {
            parent[x] = findParent(parent[x], parent);
        }
        return parent[x];
    }

    static class Edge {
        public int a;
        public int b;
        public int cost;

        public Edge(int a, int b, int cost) {
            this.a = a;
            this.b = b;
            this.cost = cost;
        }
    }
}
