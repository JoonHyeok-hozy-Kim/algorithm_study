#include <iostream>
#include <unordered_set>
#include <random>
using namespace std;

template <typename T>
class Node{
    Node<T> *next = nullptr;
    T data;

    public: 
        Node() {};
        Node(T t) : data(t) {};
        ~Node() {};

        void show_list(){
            Node<T> *walk = this;
            cout << "[";
            while (walk != nullptr){
                cout << walk->data;
                if (walk->next == nullptr){
                    break;
                } else {
                    cout << ", ";
                }
                walk = walk->next;
            }
            cout << "]" << endl;
        }

        void append_to_tail(T val){
            Node<T> *walk = this;
            while (walk->next != nullptr){
                walk = walk->next;
            }
            walk->next = new Node<T>(val);
        }

        T delete_node(Node<T> *N){
            T result = N->data;
            if (N->next != nullptr){
                Node<T> *walk = this;
                while (walk->next != N) walk = walk->next;
                walk->next = N->next;
            }
            delete N;
            return result;
        }

        class cnt_val{
            public:
                int cnt;
                T val;

                cnt_val() {};
                cnt_val(int c, T v) : cnt(c), val(v) {};
                ~cnt_val() {};
        };

        T kth_to_last(int K){
            return _kth_to_last(this, 0, K)->val;
        }

        cnt_val* _kth_to_last(Node<T> *N, int cnt, int K){
            cnt_val* cv;
            if (N->next == nullptr){
                cv = new cnt_val(cnt+1, N->data);
                return cv;
            }
            cv = _kth_to_last(N->next, cnt+1, K);
            if (cv->cnt > K) {
                cv->val = N->data;
                cv->cnt--;
            }
            return cv;
        }

};


int main() {
    Node<char> x('a'); 
    for (int i=0; i<20; i++){
        x.append_to_tail('b'+i);
    }
    x.show_list();
    cout << x.kth_to_last(5) << endl;
}