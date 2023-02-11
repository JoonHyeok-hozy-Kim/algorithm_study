#include <iostream>
#include <unordered_set>
#include <random>
using namespace std;

template <typename T>
class Node{
    public: 
        Node<T> *next = nullptr;
        int id;
        T data;

        Node() {};
        Node(int i, T t) : id(i), data(t) {
            //cout << "Node generated : " << this->data << endl;
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

        void add_after(Node<T> *N){
            Node<T> *new_node = new Node<T>(i, t);
        }

        T delete_node(Node<T> *N){
            T result = N->data;
            delete N;
            return result;
        }
};

template <typename T>
class Stack{
    public:
        Node<T> *top;
        int id;

        Stack(int i, Node<T> &N) : id(i), top(&N) {};
        ~Stack() {};

        bool is_empty() {
            return this->top->id != this->id;
        }

        void push(T t){
            Node<T> *walk = this->top;
            while (walk->next != nullptr) walk = walk->next;
            walk->next = new Node<T>(this->id, t);
            this->top = walk->next;
        }

        void pop(){
            Node<T> *walk = this->top;
        }
};


int main(){
    Node<int> arr(0, 0);
    Stack<int> S1(1, arr);
}