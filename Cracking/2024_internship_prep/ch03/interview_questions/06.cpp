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
                int cnt;

                Node(T t, int n) : data(t), cnt(n), next(nullptr) {};
        };

    public:
        Node *first;
        Node *last;
        int node_cnt = 0;

        MyQueue() : first(nullptr), last(nullptr) {};
        ~MyQueue() {};

        bool is_empty(){
            return first == nullptr;
        }

        void push(T t){
            Node *new_node = new Node(t, node_cnt);
            node_cnt++;
            if (this->is_empty()){
                this->first = new_node;
                this->last = first;
            } else {
                this->last->next = new_node;
                this->last = new_node;                
            }
        }

        void push(T t, int given_cnt){
            Node *new_node = new Node(t, given_cnt);
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

        void show(){
            Node *walk = this->first;
            cout << "[ ";
            while (walk != nullptr){   
                cout << "(" << walk->data << ", " << walk->cnt << ") ";
                walk = walk->next;
            }
            cout << "]\n";
        }

        T pop_specific(T t){
            int initial_cnt = this->first->cnt;
            T result = '\0';
            T temp;
            int temp_cnt;
            if (this->front() == t){
                result = this->front();
                this->pop();
            } else {
                temp = this->front();
                temp_cnt = initial_cnt;
                this->pop();
                this->push(temp, temp_cnt);

                while (this->first->cnt != initial_cnt){
                    if (this->front() == t){
                        result = this->front();
                        this->pop();
                        break;
                    } else {
                        temp = this->front();
                        temp_cnt = this->first->cnt;
                        this->pop();
                        this->push(temp, temp_cnt);
                    }
                }
            }

            if (result == '\0') throw exception();

            return result;
        }
};

int main(){
    MyQueue<char> Q;
    Q.push('c');
    Q.show();
    Q.push('d');
    Q.show();
    Q.push('c');
    Q.show();
    Q.push('d');
    Q.show();
    Q.push('d');
    Q.show();
    Q.push('c');
    Q.show();

    Q.pop();
    Q.show();

    Q.pop_specific('c');
    Q.show();

    Q.pop_specific('d');
    Q.show();

    // Q.pop_specific('3');
    // Q.show();
}