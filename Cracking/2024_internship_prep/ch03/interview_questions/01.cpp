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

        Node<T>* add_after(Node<T> *N, int i, T t){
            Node<T> *new_node = new Node<T>(i, t);
            new_node->next = N->next;
            N->next = new_node;
            return new_node;
        }

        Node<T>* delete_node(){
            Node<T> *delete_next = this->next;
            delete this;
            return delete_next;
        }
};

template <typename T>
class Stack{
    public:
        Node<T> *global_top;
        Node<T> *stack_top;
        int id;

        Stack(int i, Node<T> &N) : id(i), global_top(&N), stack_top(&N) {};
        ~Stack() {};

        bool is_empty() {
            return this->id != this->stack_top->id;
        }

        void push(T t){
            Node<T> *new_node = this->stack_top->add_after(this->stack_top, this->id, t);
            this->stack_top = new_node;
        }

        void pop(){
            if (this->is_empty()) throw exception();
            Node<T> *new_top = this->global_top;
            while (new_top->next != this->stack_top) new_top = new_top->next;
            new_top->next = this->stack_top->delete_node();
            if (new_top->id == this->id) {
                this->stack_top = new_top;
            } else {
                this->stack_top = this->global_top;
            }
        }

        T top(){
            if (this->is_empty()) throw exception();
            return this->stack_top->data;
        }
};


int main(){
    Node<int> G(0, -999);
    Stack<int> S1(1, G);
    cout << boolalpha << S1.is_empty() << endl;
    
    for (int i=0; i<10; i++){
        S1.push(i);
        cout << "S1 pushed. top : " << S1.top() << ", G : ";
        G.show_list();
    }

    for (int i=0; i<5; i++){
        S1.pop();
        cout << "S1 popped. top : " << S1.top() << ", G : ";
        G.show_list();
    }

    Stack<int> S2(2, G);
    for (int i=0; i<4; i++) {
        S2.push(-i-1);
        S1.pop();
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top() << ", G : ";
        G.show_list();
    }

    for (int i=1; i<5; i++){
        S1.push(i*100);
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top() << ", G : ";
        G.show_list();
    }

    Stack<int> S3(3, G);
    for (int i=1; i<4; i++){
        S3.push(i*1000);
        S1.pop();
        S2.push(-i*100);
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top();
        cout << " S3 top : " << S3.top() << ", G : ";
        G.show_list();
    }

    while (!S2.is_empty()){
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top();
        cout << " S3 top : " << S3.top() << ", G : ";
        G.show_list();
        S2.pop();
    }

    while (!S3.is_empty()){
        cout << "S1 top : " << S1.top() << ", S3 top : " << S3.top();
        cout << ", G : ";
        G.show_list();
        S3.pop();
    }

    for (int i=0; i<5; i++){
        S2.push(-i-1);
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top();
        cout << ", G : ";
        G.show_list();
    }

    while (!S1.is_empty()){
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top();
        cout << ", G : ";
        G.show_list();
        S1.pop();
    }

    G.show_list();

    for (int i=100; i<106; i++){
        S1.push(i);
        cout << "S1 top : " << S1.top() << ", S2 top : " << S2.top();
        cout << ", G : ";
        G.show_list();
    }
}