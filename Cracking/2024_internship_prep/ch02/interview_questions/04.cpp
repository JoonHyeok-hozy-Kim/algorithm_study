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
            delete N;
            return result;
        }

        void data_swap(Node<T> *N, Node<T> *M){
            T temp = N->data;
            N->data = M->data;
            M->data = temp;
        }

        void partition(T criterion){
            Node<T> *pivot = this;
            Node<T> *walk;
            while (pivot->next != nullptr){
                // this->show_list();
                while ((pivot != nullptr && pivot->next != nullptr) && pivot->data < criterion) pivot = pivot->next;
                if (pivot == nullptr || pivot->next == nullptr){
                    // cout << "In partition return 1" << endl;
                    return;
                } else {
                    walk = pivot->next;
                    while (walk != nullptr && walk->data >= criterion) walk = walk->next;
                    if (walk == nullptr){
                        // cout << "In partition return 2" << endl;
                        return;
                    } else {
                        this->data_swap(pivot, walk);
                    }
                }
            }
            // cout << "In partition return 3" << endl;
        }
};


int main() {
    Node<int> x1(3); 
    x1.append_to_tail(5);
    x1.append_to_tail(8);
    x1.append_to_tail(5);
    x1.append_to_tail(10);
    x1.append_to_tail(2);
    x1.append_to_tail(1);
    x1.show_list();

    x1.partition(5);
    x1.show_list();

    Node<int> x2(2);
    x2.append_to_tail(3);
    x2.show_list();
    // x2.partition(1);
    // x2.show_list();

    // x2.partition(2);
    // x2.show_list();

    x2.partition(10);
    x2.show_list();
}