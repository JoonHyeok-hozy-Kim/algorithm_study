//1181. 단어정렬
//https://www.acmicpc.net/problem/1181

#include <iostream>
#include <vector>
#include <algorithm>


bool cmp(std::string w1, std::string w2){
    if (w1.size() == w2.size()) return w1 < w2;
    else return w1.size() < w2.size();
}


int main() {
    // std::cout << std::boolalpha << ('a' < 'b') << std::endl;
    // std::cout << std::boolalpha << ("aa" < "ab") << std::endl;

    int N;
    std::cin >> N;

    std::string w;
    std::vector<std::string> words;
    words.reserve(N);
    for (int i=0; i<N; i++){
        std::cin >> w;
        words.push_back(w);
    }

    sort(words.begin(), words.end(), cmp);

    std::string prev = words[0];
    std::cout << prev << std::endl;
    for (int i=1; i<N; i++){
        if (words[i] == prev) continue;
        std::cout << words[i] << std::endl;
        prev = words[i];
    }    

    return 0;
}