#include <iostream>
#include <exception>
using namespace std;

template <typename T>
class MyStack{
    private:    
        class MyStackNode{
            public:
                MyStackNode *next;
                T data;

                MyStackNode(T t) : data(t) {};
        };

    public:
        MyStackNode *top_node;
        MyStack() : top_node(nullptr) {};

        bool is_empty(){
            return this->top_node == nullptr;
        }

        void push(T t){
            MyStackNode *new_node = new MyStackNode(t);
            new_node->next = this->top_node;
            this->top_node = new_node;
        }

        void pop(){
            if (this->is_empty()) throw exception();
            MyStackNode *popped = this->top_node;
            this->top_node = popped->next;
            delete popped;
        }

        T top(){
            if (this->is_empty()) throw exception();
            return this->top_node->data;
        }
};


int main(){
    MyStack<int> S;
    cout << boolalpha << S.is_empty() << endl;
    for (int i=0; i<10; i++){
        S.push(i);
    }
    while (!S.is_empty()){
        cout << S.top() << endl;
        S.pop();
    }

    MyStack<int> S2;
    S2.pop();
}