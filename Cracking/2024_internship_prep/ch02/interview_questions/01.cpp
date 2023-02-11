#include <iostream>
#include <unordered_set>
using namespace std;

template <typename T>
class Node{
    Node<T> *next = nullptr;
    T data;

    public: 
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

        void remove_dups_two_pointer(){
            Node<T> *walk = this;
            Node<T> *target;
            Node<T> *temp;
            while (walk->next != nullptr){
                target = walk;
                while (target->next != nullptr){
                    if (target->next->data == walk->data){
                        temp = target->next->next;
                        delete target->next;
                        target->next = temp;
                    } else {
                        target = target->next;
                    }
                }
                walk = walk->next;
            }
        }

        void remove_dups_hash(){
            unordered_set<T> S;
            Node<T> *walk = this;
            Node<T> *temp;
            S.insert(walk->data);

            while (walk->next != nullptr){
                if (S.find(walk->next->data) == S.end()){
                    S.insert(walk->next->data);
                    walk = walk->next;
                } else {
                    temp = walk->next->next;
                    delete walk->next;
                    walk->next = temp;
                }
            }
        }
};


int main() {
    // Node<char> x('a');
    // x.show_list();

    // for (int i=0; i<5; i++){
    //     x.append_to_tail('a'+i);
    //     x.show_list();
    // }

    Node<int> y(1);
    y.append_to_tail(2);
    y.append_to_tail(3);
    y.append_to_tail(3);
    y.append_to_tail(1);
    y.append_to_tail(4);
    y.append_to_tail(5);
    y.show_list();
    // y.remove_dups_two_pointer();
    y.remove_dups_hash();
    y.show_list();
}