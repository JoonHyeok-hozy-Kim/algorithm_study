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
};

Node<int> sum_lists(Node<int> &N1, Node<int> &N2){
    Node<int> *p1, *p2;
    p1 = &N1;
    p2 = &N2;
    Node<int> temp(-1);
    int temp_sum;
    int carry = 0;

    while (p1 != nullptr && p2 != nullptr){
        temp_sum = p1->data + p2->data + carry;
        if (temp_sum > 9){
            carry = 1;
            temp_sum -= 10;
        } else {
            carry = 0;
        }
        temp.append_to_tail(temp_sum);

        p1 = p1->next;
        p2 = p2->next;
    }

    if (p1 != nullptr) temp.append_to_tail(p1->data + carry);
    else if (p2 != nullptr) temp.append_to_tail(p2->data + carry);

    Node<int> *result = temp.next;
    return *result;
}

struct NodeCarry{
    Node<int> *np;
    int carry;
};

NodeCarry* _sum_lists_reversed(Node<int> *p1, Node<int> *p2, NodeCarry *nc){
    if (p1 == nullptr && p2 == nullptr){
        nc->carry = 0;
    } else if (p1 == nullptr){        
        nc->np->append_to_tail(p2->data);
        nc->carry = 0;
    } else if (p2 == nullptr){
        nc->np->append_to_tail(p2->data);
        nc->carry = 0;
    } else {
        Node<int> *new_node = nc->np->append_to_tail(p1->data + p2->data);
        _sum_lists_reversed(p1->next, p2->next, nc);
        new_node->data += nc->carry;
        if (new_node->data > 9){
            nc->carry = 1;
            new_node->data -= 10;
        } else {
            nc->carry = 0;
        }
    }
    // nc->np->show_list();
    // cout << "Carry : " << nc->carry << endl;
    return nc;
}

Node<int> sum_lists_reversed(Node<int> &N1, Node<int> &N2){
    NodeCarry *nc = new NodeCarry();
    nc->np = new Node<int>(-1);
    nc = _sum_lists_reversed(&N1, &N2, nc);

    Node<int> result;
    if (nc->carry == 1){
        nc->np->data = 1;
        result = *(nc->np);
    } else {
        result = *(nc->np->next);
        delete nc->np;        
    }
    return result;
}


int main() {
    Node<int> n1(7);
    n1.append_to_tail(1);
    n1.append_to_tail(6);

    Node<int> n2(5);
    n2.append_to_tail(9);
    n2.append_to_tail(2);

    Node<int> n3 = sum_lists(n1, n2);
    n3.show_list();

    
    Node<int> n11(8);
    n11.append_to_tail(1);
    n11.append_to_tail(7);

    Node<int> n21(2);
    n21.append_to_tail(9);
    n21.append_to_tail(5);

    Node<int> n31 = sum_lists_reversed(n11, n21);
    n31.show_list();
}