#include <iostream>
using namespace std;

template <typename T>
class Node{
    public: 
        Node<T> *next = nullptr;
        T data;
        T min;

        Node() {};
        Node(T t, T min_cand, Node<T> *next_node) : data(t), next(next_node) {
            if (min_cand < t) {
                this->min = min_cand;
            } else {
                this->min = t;
            }
        };
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
};

template <typename T>
class Stack{
    public:
        Node<T> *top_node = nullptr;

        bool is_empty(){
            return this->top_node == nullptr;
        }

        T top(){
            if (this->is_empty()) throw exception();
            return this->top_node->data;
        }

        T min(){
            if (this->is_empty()) throw exception();
            return this->top_node->min;
        }

        void push(T t){
            T min_cand;
            if (this->is_empty()){
                min_cand = t;
            } else {
                min_cand = this->top_node->min;
            }

            Node<T> *new_top = new Node<T>(t, min_cand, this->top_node);
            this->top_node = new_top;
        }

        void pop(){
            if (this->is_empty()) throw exception();
            Node<T> *popped = this->top_node;
            this->top_node = this->top_node->next;
            delete popped;
        }
};


int main(){
    Stack<int> S1;
    for (int i=0; i<5; i++){
        S1.push(i);
        cout << "[top] " << S1.top() << " [min] " << S1.min() << endl;
    }
    for (int i=100; i>95; i--){
        S1.push(i);
        cout << "[top] " << S1.top() << " [min] " << S1.min() << endl;
    }
    for (int i=1; i<5; i++){
        S1.push(-i);
        cout << "[top] " << S1.top() << " [min] " << S1.min() << endl;
    }

    while (!S1.is_empty()){
        cout << "[top] " << S1.top() << " [min] " << S1.min() << endl;
        S1.pop();
    }
}