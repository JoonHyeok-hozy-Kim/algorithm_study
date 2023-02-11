#include <iostream>
using namespace std;

template <typename T>
class Node{
public:
    T value;
    Node *prev = nullptr;
    Node *next = nullptr;

    Node() {};
    Node(T t) : value(t) {};
    Node(T t, Node *prev_node, Node *next_node) {
        this->value = t;
        prev = prev_node;
        next = next_node;

        // cout << "[Node constructed] ";
        // show_node();
    };
    ~Node() {
        // cout << "[Node destructed] ";
        // show_node();
    };

    void show_node(){
        cout << "[Node] value : " << this->value;
        cout << " (prev : ";
        if (prev != nullptr) cout << this->prev->value;
        cout << ", next : ";
        if (next != nullptr) cout << this->next->value;
        cout << ")" << endl;
    }
};

template <typename T>
class LinkedList{
public:
    Node<T> *header;
    Node<T> *trailer;
    int size;

    LinkedList() {
        this->header = new Node<T>();
        this->trailer = new Node<T>();
        this->header->next = this->trailer;
        this->trailer->prev = this->header;
        this->size = 0;
    }

    ~LinkedList() {
        Node<T> *walk = this->header;
        while (walk != this->trailer){
            walk = walk->next;
            delete walk->prev;
        }
        delete walk;
    }

    void show_list() {
        Node<T> *walk = this->header->next;        
        cout << "[";
        while (walk != this->trailer){
            cout << walk->value;
            if (walk == this->trailer->prev){
                break;
            }
            else {
                cout << ", ";
            }
            walk = walk->next;
        }        
        cout << "]\n";
    }

    void add_before(Node<T> *N, T val){
        if (N == this->header) return;

        Node<T> *new_node = new Node<T>(val, N->prev, N);
        N->prev->next = new_node;
        N->prev = new_node;
        this->size++;
    }

    void add_last(T val){
        add_before(this->trailer, val);
    }

    void add_after(Node<T> *N, T val){
        if (N == this->trailer) return;

        Node<T> *new_node = new Node<T>(val, N, N->next);
        N->next->prev = new_node;
        N->next = new_node;
        this->size++;
    }

    void add_first(T val){
        add_after(this->header, val);
    }

    T erase(Node<T> *N){
        if (this->size == 0){
            throw out_of_range("Linkedlist is empty.");
        }

        T result = N->value;
        N->prev->next = N->next;
        N->next->prev = N->prev;
        delete N;
        return result;
    }

    T delete_first(){
        return this->erase(this->header->next);
    }

    T delete_last(){
        return this->erase(this->trailer->prev);
    }
};

int main() {
    // Node<int> n1;
    // n1.show_node();

    // Node<int> n2(3);
    // n2.show_node();

    // Node<int> n3(4);
    // n3.show_node();

    // Node<int> n4(5, &n2, &n3);
    // n4.show_node();

    LinkedList<int> l1;
    l1.show_list();

    for (int i=1; i<5; i++){
        l1.add_last(i);
        l1.show_list();
    }

    for (int i=1; i<5; i++){
        l1.add_first(-i);
        l1.show_list();
    }

    for (int i=0; i<4; i++){
        cout << l1.delete_first() << " deleted." << endl;
        l1.show_list();
    }

    for (int i=0; i<4; i++){
        cout << l1.delete_last() << " deleted." << endl;
        l1.show_list();
    }
}