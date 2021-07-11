package day_97;

import java.io.*;
import java.util.*;

class A implements Comparable<A>{
    int s; int e; int v;   
    A(int s,int e,int v){
    	this.s = s;
    	this.e = e;
    	this.v = v;
    }
    
    @Override
    public int compareTo(A a){
       return a.v >= this.v ? -1 : 1; // 매개로 받은 간선값이 더 크면 -1,내가더크면 1반환
    }
    
}
class Node{
	int idx; int x; int y; int z;
	Node(int idx,int x,int y,int z){
		this.idx = idx;
		this.x = x;
		this.y = y;
		this.z = z;
	}
}

public class Main {
	static int V;
	static int[] parent;
	static int edgeCnt;
	static int ans;

	public static int find(int a) {
        if(a == parent[a]) return a; // 최상위부모
        parent[a] = find(parent[a]); // 부모를 최상위 부모로 설정
        return parent[a];
    }
    public static void union(A a){
        int start = a.s;
        int end = a.e; //a와 b가 연결되면 사이클이 생기지않는지 확인(부모가 이미같지 않은지 확인)
        int _start = find(start);
        int _end = find(end);
        if(_start != _end) { //다르다면 연결
            parent[_start] = end; // parent[_end] = start;도 가능 // 한쪽의 최상위 부모의 부모를  다른 한쪽으로 설정하여 연결
            edgeCnt++;
            ans += a.v;
        }
        else return;
    }
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		V = Integer.parseInt(st.nextToken()); // 노드개수
		parent = new int[V];
		edgeCnt = 0;
		ans = 0;
		Queue<A> pq = new PriorityQueue<>(); //간선크기 작은것 먼저 나오는 우선순위 큐		
		Node[] nodes = new Node[V];
		for(int i=0;i<V;i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			nodes[i] = new Node(i,x,y,z);
		}
		//1. 간선값 만들기
		//1-1. x기준 
		Arrays.sort(nodes, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				return o1.x >= o2.x ? -1 : 1;
			}			
		});
		for(int i=0;i<nodes.length-1;i++) {
			int s = i;
			int e = i+1;
			int v = Math.abs(nodes[s].x - nodes[e].x);
			pq.add(new A(nodes[s].idx,nodes[e].idx,v));
		}
		//1-2. y기준
		Arrays.sort(nodes, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				return o1.y >= o2.y ? -1 : 1;
			}			
		});
		for(int i=0;i<nodes.length-1;i++) {
			int s = i;
			int e = i+1;
			int v = Math.abs(nodes[s].y - nodes[e].y);
			pq.add(new A(nodes[s].idx,nodes[e].idx,v));
		}
		//1-3. z기준
		Arrays.sort(nodes, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				return o1.z >= o2.z ? -1 : 1;
			}			
		});
		for(int i=0;i<nodes.length-1;i++) {
			int s = i;
			int e = i+1;
			int v = Math.abs(nodes[s].z - nodes[e].z);
			pq.add(new A(nodes[s].idx,nodes[e].idx,v));
		}
		
		//2. kruskal 사용
		//2-0. parent 배열 기본값은 자기자신
		for(int i=0;i<V;i++) {
			parent[i] = i;
		}
		//2-1. pq에서 한개씩 poll해서 union(s,e)
		while(!pq.isEmpty()) {
			A a = pq.poll();
			union(a);
			//2. 이어진 간선의 개수가 전체 노드의 개수 - 1이되면 break
			if(edgeCnt == V - 1) break;		
		}
		System.out.println(ans);

	}

}
