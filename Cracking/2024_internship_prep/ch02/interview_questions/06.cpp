#include <iostream>
#include <unordered_set>
#include <random>
using namespace std;

template <typename T>
class Node{
    public: 
        Node<T> *prev = nullptr;
        Node<T> *next = nullptr;
        T data;

        Node() {};
        Node(T t) : data(t) {};
        Node(T t, Node<T> *prev_node, Node<T> *next_node) : data(t), prev(prev_node), next(next_node) {};
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
            walk->next = new Node<T>(val, walk, nullptr);
        }

        T delete_node(Node<T> *N){
            T result = N->data;
            delete N;
            return result;
        }
};

bool check_palindrome(Node<char> &N1){
    Node<char> *start = &N1;
    if (start->next == nullptr) return true;

    Node<char> *end = start;
    while (end->next != nullptr) end = end->next;

    while (start != end && end->next != start){
        if (start->data != end->data) return false;
        start = start->next;
        end = end->prev;
    }
    return true;
}


int main() {
    Node<char> x1('a');
    x1.append_to_tail('b');
    x1.show_list();
    cout << boolalpha << check_palindrome(x1) << endl;

    x1.append_to_tail('a');
    x1.show_list();
    cout << boolalpha << check_palindrome(x1) << endl;

    Node<char> x2('a');
    x2.append_to_tail('a');
    x2.show_list();
    cout << boolalpha << check_palindrome(x2) << endl;
}