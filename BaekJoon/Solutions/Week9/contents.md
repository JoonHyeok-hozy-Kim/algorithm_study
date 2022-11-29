## Week 9. Shortest Path Finding (Dijkstra, Floyd-Warshall, and Bellman-Ford)

### Theories
1. [Dijkstra's Algorithm revisited](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md#1462-dijkstras-algorithm)
2. [Floyd-Warshall Algorithm revisited](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md#tech-floyd-warshall-algorithm)
3. [Bellman-Ford]()


### Main Questions
|No.  |Question|Trial 1|
|:---:|:-------|:-----:|
|1.   |[전구를 켜라](https://www.acmicpc.net/problem/2423 )| [221122](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_01_221122_2423.py) |
|2.   |[Road Reconstruction](https://www.acmicpc.net/problem/20046)| [221123](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_02_221123_20046.py) |
|3.   |[홍익대학교 지하캠퍼스](https://www.acmicpc.net/problem/17833)| [221123](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_03_221123_17833.py) |
|4.   |[월요병](https://www.acmicpc.net/problem/14611)| [221123](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_04_221123_14611.py) |
|5.   |[The Other Way](https://www.acmicpc.net/problem/14554)| [221124](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_05_221124_14554.py) |
|6.   |[최소비용 구하기 2](https://www.acmicpc.net/problem/11779)| [221124](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_06_221124_11779.py) |
|7.   |[무엇을 아느냐가 아니라 누구를 아느냐가 문제다](https://www.acmicpc.net/problem/9694 )| [221124](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_07_221124_9694.py) |
|8.   |[거의 최단 경로](https://www.acmicpc.net/problem/5719 )| [221126](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_08_221126_5719_cheated.py) |
|9.   |[K번째 최단경로 찾기](https://www.acmicpc.net/problem/1854 )| [221126](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_09_221126_1854.py) |
|10.  |[노트 조각](https://www.acmicpc.net/problem/24888)| :hourglass:[221127](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_10_221127_24888_failed.py) |
|11.  |[텔레포트](https://www.acmicpc.net/problem/16958)| :hourglass:[221128](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol_11_221128_16958_failed2.py) |
|12.  |[밤편지](https://www.acmicpc.net/problem/23258)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol.py) |
|13.  |[Ignition](https://www.acmicpc.net/problem/13141)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol.py) |
|14.  |[arbitrage](https://www.acmicpc.net/problem/6598 )| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol.py) |
|15.  |[키 순서](https://www.acmicpc.net/problem/2458 )| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol.py) |
|16.  |[두 단계 최단경로 1](https://www.acmicpc.net/problem/23793)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/MainQuestions/Sol.py) |


### Advanced Questions
|No.  |Question|Trial 1|
|:---:|:-------|:-----:|
|1.   |[도로포장](https://www.acmicpc.net/problem/1162 )| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |
|2.   |[도로검문](https://www.acmicpc.net/problem/2307 )| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |
|3.   |[미로 만들기](https://www.acmicpc.net/problem/2665 )| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |
|4.   |[백양로 브레이크](https://www.acmicpc.net/problem/11562)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |
|5.   |[템포럴 그래프](https://www.acmicpc.net/problem/25953)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |
|6.   |[Forbidden Turns](https://www.acmicpc.net/problem/26106)| [](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/BaekJoon/Solutions/Week9/AdvancedQuestions/Sol.py) |

