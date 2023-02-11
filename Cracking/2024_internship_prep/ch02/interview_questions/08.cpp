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
        Node(T t) : data(t) {
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

        Node<T>* append_to_tail(T val){
            Node<T> *walk = this;
            while (walk->next != nullptr){
                walk = walk->next;
            }
            walk->next = new Node<T>(val);
            return walk->next;
        }

        T delete_node(Node<T> *N){
            T result = N->data;
            delete N;
            return result;
        }

        Node<T>* detect_loop(){
            unordered_set<Node<T>*> US;
            Node<T> *walk = this;
            while (walk != nullptr){
                // cout << "In detect_loop, " << walk->data << endl;
                if (US.find(walk) == US.end()){
                    US.insert(walk);
                    walk = walk->next;
                } else {
                    break;
                }
            }
            return walk;
        }
};


int main() {
    Node<int> n1(0);
    for (int i=0; i<5; i++){
        n1.append_to_tail(i+1);
    }
    n1.show_list();
    cout << n1.detect_loop() << endl;

    Node<int> *n1_node = &n1;
    Node<int> *n1_last = &n1;
    for (int i=0; i<3; i++) n1_node = n1_node->next;
    while (n1_last->next != nullptr) n1_last = n1_last->next;
    n1_last->next = n1_node;

    cout << n1.detect_loop()->data << endl;
}