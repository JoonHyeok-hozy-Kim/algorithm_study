#include <iostream>
using namespace std;

template <typename T>
class Stack{
    private:
        class Node{
            public:
                Node *next_node = nullptr;
                T data;

                Node(T t, Node *next) : data(t), next_node(next) {};
                ~Node() {};
        };
    
    public:
        Node *top_node = nullptr;
        int size = 0;

        Stack() {};

        bool is_empty() {
            return this->size == 0;
        }

        void push(T t) {
            Node *new_node = new Node(t, this->top_node);
            this->top_node = new_node;
            this->size++;
        }

        void pop(){
            if (this->is_empty()) throw exception();
            Node *popped = this->top_node;
            this->top_node = this->top_node->next_node;
            this->size--;
            delete popped;
        }

        T top(){
            if (this->is_empty()) throw exception();
            return this->top_node->data;    
        }

        void show(){
            Node *target_node = this->top_node;
            cout << "[ ";
            while (target_node != nullptr){
                cout << target_node->data << " ";
                target_node = target_node->next_node;
            }
            cout << "] ";
        }
};


template <typename T>
class MyQueue{
    public:
        Stack<T> back_stack;
        Stack<T> front_stack;

        MyQueue() {};
        ~MyQueue() {};

        bool is_empty(){
            return this->back_stack.is_empty() && this->front_stack.is_empty();
        }

        void migrate_to_front(){
            if (!this->front_stack.is_empty()) throw exception();
            while (!this->back_stack.is_empty()){
                this->front_stack.push(this->back_stack.top());
                this->back_stack.pop();
            }
        }

        void migrate_to_back(){
            if (!this->back_stack.is_empty()) throw exception();
            while (!this->front_stack.is_empty()){
                this->back_stack.push(this->front_stack.top());
                this->front_stack.pop();
            }
        }

        T front(){
            if (this->front_stack.is_empty()){
                if (this->back_stack.is_empty()) throw exception();
                else this->migrate_to_front();
            }
            return this->front_stack.top();
        }

        T back(){
            if (this->back_stack.is_empty()){
                if (this->front_stack.is_empty()) throw exception();
                else this->migrate_to_back();
            }
            return this->back_stack.top();
        }

        void push(T t){
            this->back_stack.push(t);
        }

        void pop(){
            if (this->front_stack.is_empty()) {
                if (this->back_stack.is_empty()) throw exception();
                else this->migrate_to_front();
            }
            this->front_stack.pop();
        }
};

int main(){
    MyQueue<int> Q;
    for (int i=0; i<3; i++){
        Q.push(i);
        cout << "Pushed : " << Q.front() << " ~ " << Q.back() << endl;
    }
    
    while (!Q.is_empty()){
        cout << "Popped : " << Q.front() << " ~ " << Q.back() << endl;
        Q.pop();
    }

    for (int i=0; i<5; i++){
        Q.push(i);
        cout << "Pushed : " << Q.front() << " ~ " << Q.back() << endl;
    }
    
    for (int i=0; i<3; i++){
        cout << "Popped : " << Q.front() << " ~ " << Q.back() << endl;
        Q.pop();
    }

    for (int i=0; i<5; i++){
        Q.push(i);
        cout << "Pushed : " << Q.front() << " ~ " << Q.back() << endl;
    }
    
    while (!Q.is_empty()){
        cout << "Popped : " << Q.front() << " ~ " << Q.back() << endl;
        Q.pop();
    }
}