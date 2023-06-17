package com.sunset.baekjoon.graphTraversal.baekjoon2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[][] graph;
    static boolean[][] visited;

    static int[] dx = {0, -1, 1, 0};
    static int[] dy = {1, 0, 0, -1};

    static int n, m;
    static List<Integer> result = new ArrayList<>();

    static Queue<int[]> queue = new LinkedList<int[]>();



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String[] split = br.readLine().split("");
            int m = 0;
            for (String s : split) {
                graph[i][m] = Integer.parseInt(s);
                m += 1;
            }
        }

        bfs(0, 0);

    }

    public static void bfs(int x, int y) {
        if (visited[x][y] == false) {
            visited[x][y] = true;
            graph[x][y] = 1;
            queue.offer(new int[]{x, y});
        }

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int a = poll[0];
            int b = poll[1];
            if (a == n - 1 && b == m - 1) {
                System.out.println(graph[a][b]);
            }

            for (int i = 0; i < 4; i++) {
                if (a + dx[i] >= 0 && a + dx[i] < n && b + dy[i] >= 0 && b + dy[i] < m) {
                    if (graph[a + dx[i]][b + dy[i]] != 0) {
                        if (!visited[a + dx[i]][b + dy[i]]) {
                            queue.offer(new int[]{a + dx[i], b + dy[i]});
                            visited[a + dx[i]][b + dy[i]] = true;
                            graph[a + dx[i]][b + dy[i]] = graph[a][b] + 1;
                        }
                    }

                }
            }

        }

    }
}
