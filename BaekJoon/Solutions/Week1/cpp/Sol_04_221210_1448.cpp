/*
1448 삼각형 만들기
https://www.acmicpc.net/problem/1448
*/


#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <numeric>

int N;
int straws[1000000];


int dfs(int i, std::vector<int>& v, int max_val);
int validate_triangle(std::vector<int>& v);
int main();


int dfs(int i, std::vector<int>& v, int max_val, int depth){
    // for (int y=0; y<depth; y++) std::cout << " ";
    // std::cout << "In dfs, i : " << i << ", size : " << v.size() << std::endl;

    if (v.size() == 3){
        // std::cout << "In dfs, size 3, max_val : " << max_val << ", v : ";
        // for (int x : v) std::cout << x << " ";
        // std::cout << std::endl;

        if (std::accumulate(v.begin(), v.end(), 0) > max_val) return std::max(validate_triangle(v), max_val);
        return max_val;
    }

    int temp_max = max_val;
    v.push_back(straws[i]);
    for (int j=i+1; j<N+1; j++){
        temp_max = std::max(temp_max, dfs(j, v, temp_max, depth+1));
    }
    v.pop_back();

    return temp_max;
}


int validate_triangle(std::vector<int>& v){
    std::priority_queue<int> pq;
    for (int x : v) pq.push(x);
    int test = pq.top();
    int sum = pq.top();
    for (int i=0; i<2; i++){
        pq.pop();
        test -= pq.top();
        sum += pq.top();
    }

    // std::cout << "In validate, test : " << test << ", sum : " << sum << std::endl;

    if (test < 0) return sum;
    else return -1;
}


bool cmp(int a, int b){
    return a > b;
}


int main(){
    std::cin >> N;
    for (int i=0; i<N; i++){
        std::cin >> straws[i];
    }

    std::sort(straws, straws+N, cmp);
    
    std::vector<int> V;
    V.reserve(3);
    int result = -1;
    for (int i=0; i<N; i++){
        result = std::max(result, dfs(i, V, result, 0));
    }
    
    std::cout << result << std::endl;
}