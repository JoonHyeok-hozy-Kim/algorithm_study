#include <iostream>
#include <exception>
using namespace std;

template <typename T>
class MyQueue{
    private:    
        class Node{
            public:
                Node *next;
                T data;

                Node(T t) : data(t), next(nullptr) {};
        };

    public:
        Node *first;
        Node *last;

        MyQueue() : first(nullptr), last(nullptr) {};
        ~MyQueue() {};

        bool is_empty(){
            return first == nullptr;
        }

        void push(T t){
            Node *new_node = new Node(t);
            if (this->is_empty()){
                this->first = new_node;
                this->last = first;
            } else {
                this->last->next = new_node;
                this->last = new_node;                
            }
        }

        void pop(){
            if (this->is_empty()) throw exception();
            else if (this->first == this->last){
                delete this->first;
                this->first = nullptr;
                last = nullptr;
            } else {
                Node *popped = this->first;
                this->first = this->first->next;
                delete popped;
            }
        }

        T front(){
            if (this->is_empty()) throw exception();
            return this->first->data;
        }

        T back(){
            if (this->is_empty()) throw exception();
            return this->last->data;
        }
};

int main(){
    MyQueue<int> Q;
    for (int i=0; i<10; i++) Q.push(i);
    while (!Q.is_empty()) {
        cout << Q.front() << " ~ " << Q.back() << endl;
        Q.pop();
    }
    
    for (int i=0; i<10; i++) Q.push(-i);
    while (!Q.is_empty()) {
        cout << Q.front() << " ~ " << Q.back() << endl;
        Q.pop();
    }
}