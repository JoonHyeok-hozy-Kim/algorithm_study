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

        bool intersecting_check(Node<T> &other){
            unordered_set<Node<T>*> US;
            Node<T> *this_node = this;
            while (this_node != nullptr){
                US.insert(this_node);
                this_node = this_node->next;
            }

            Node<T> *other_node = &other;
            while (other_node != nullptr){
                if (US.find(other_node) != US.end()) return true;
                other_node = other_node->next;
            }

            return false;
        }
};


int main() {
    Node<int> n1(0);
    for (int i=0; i<5; i++){
        n1.append_to_tail(i+1);
    }
    n1.show_list();

    Node<int> n2(0);
    for (int i=0; i<4; i++){
        n2.append_to_tail(-i-1);
    }
    n2.show_list();

    cout << boolalpha << n1.intersecting_check(n2) << endl;

    Node<int> *n1_node = &n1;
    for (int i=0; i<3; i++) n1_node = n1_node->next;
    Node<int> *n2_node = &n2;
    while (n2_node->next != nullptr) n2_node = n2_node->next;
    n2_node->next = n1_node;

    n1.show_list();
    cout << n1_node->data << endl;
    n2.show_list();
    cout << boolalpha << n1.intersecting_check(n2) << endl;
}