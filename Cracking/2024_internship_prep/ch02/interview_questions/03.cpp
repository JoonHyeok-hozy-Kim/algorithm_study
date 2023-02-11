#include <iostream>
#include <unordered_set>
#include <random>
using namespace std;

template <typename T>
class Node{
    public: 
        Node<T> *next = nullptr;
        T data;

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

        void delete_middle_node(){
            Node<T> *temp = this->next;
            this->data = temp->data;
            this->next = temp->next;
            delete temp;
        }
};


int main() {
    Node<char> x('a'); 
    for (int i=0; i<5; i++){
        x.append_to_tail('b'+i);
    }
    x.show_list();

    Node<char> *walk = &x;
    for(int i=0; i<3; i++) walk = walk->next;
    walk->delete_middle_node();

    x.show_list();
}