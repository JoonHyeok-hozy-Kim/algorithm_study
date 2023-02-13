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

        void sort(){
            Stack<T> temp_stack;
            T temp_val;
            Node *curr = this->top_node;
            bool ordered = false;

            while (!ordered){
                temp_val = this->top();
                this->pop();

                while (!this->is_empty() && temp_val >= this->top()){
                    temp_stack.push(temp_val);
                    temp_val = this->top();
                    this->pop();
                }

                // cout << "[temp_val] : " << temp_val << endl;

                if (this->is_empty()) ordered = true;
                else ordered = false;

                while (!this->is_empty() && this->top() >= temp_val){
                    temp_stack.push(this->top());
                    this->pop();
                }

                // cout << "this : ";
                // this->show();
                // cout << " / temp_val : " << temp_val;
                // cout << " / temp_stack : ";
                // temp_stack.show();
                // cout << endl;
                
                this->push(temp_val);
                while (!temp_stack.is_empty()){
                    if (this->top() > temp_stack.top()) ordered = false;
                    this->push(temp_stack.top());
                    temp_stack.pop();
                }

                // this->show();
            }
        }
};

int main() {
    Stack<int> S;
    S.push(5);
    S.push(1);
    S.push(3);
    S.push(4);
    S.push(2);
    S.show();

    S.sort();
    S.show();
}