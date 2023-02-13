#include <iostream>
#include <exception>
using namespace std;

template <typename T>
class SetOfStacks{
    private:
        class Stack{
            private:
                class Node{
                    public:
                        Node *next_node = nullptr;
                        T data;

                        Node(T t, Node *next) : data(t), next_node(next) {};
                        ~Node() {};
                };
            
            public:
                Node *top_node = nullptr;
                Stack *next_stack = nullptr;
                int size = 0;

                Stack(Stack *next) : next_stack(next) {};

                bool is_empty() {
                    return this->size == 0;
                }

                void push(T t) {
                    Node *new_node = new Node(t, this->top_node);
                    this->top_node = new_node;
                    this->size++;
                }

                void pop(){
                    if (this->is_empty()) throw exception();
                    Node *popped = this->top_node;
                    this->top_node = this->top_node->next_node;
                    this->size--;
                    delete popped;
                }

                T top(){
                    if (this->is_empty()) throw exception();
                    return this->top_node->data;    
                }

                void show(){
                    Node *target_node = this->top_node;
                    cout << "[ ";
                    while (target_node != nullptr){
                        cout << target_node->data << " ";
                        target_node = target_node->next_node;
                    }
                    cout << "] ";
                }
        };

    public:
        Stack *first_stack = nullptr;
        Stack *last_stack = nullptr;
        int capacity;
        int stack_cnt = 0;

        SetOfStacks() {};
        SetOfStacks(int capa) : capacity(capa) {};
        ~SetOfStacks() {};

        bool is_empty(){
            return this->last_stack == nullptr;
        }

        void add_stack(){
            Stack *new_stack = new Stack(this->last_stack);
            this->stack_cnt++;
            this->last_stack = new_stack;
        }

        void push(T t) {
            if (this->is_empty() || this->last_stack->size >= this->capacity) this->add_stack();
            this->last_stack->push(t);
        }

        void pop() {
            if (this->is_empty()) throw exception();
            this->last_stack->pop();
            if (this->last_stack->is_empty()){
                Stack *popped = this->last_stack;
                this->last_stack = popped->next_stack;
                delete popped;
                this->stack_cnt--;
            }
        }

        void top() {
            if (this->is_empty()) throw exception();
            return this->last_stack->top();
        }

        void pop_at(int index){
            if (index >= this->stack_cnt) throw exception();
            else if (index == this->stack_cnt - 1) this->pop();
            else {
                Stack *walk = this->last_stack;
                for (int i=0; i<(this->stack_cnt-index-2); i++){
                    walk = walk->next_stack;
                }
                // cout << "Point 1" << endl;
                Stack *target_stack = walk->next_stack;
                // cout << "Point 2 : " << walk->top_node->data << endl;
                target_stack->pop();
                // cout << "Point 3" << endl;
                if (target_stack->is_empty()){
                    walk->next_stack = target_stack->next_stack;
                    this->stack_cnt--;
                }
            }
        }

        void show(){
            Stack *target_stack = this->last_stack;
            cout << "< ";
            while (target_stack != nullptr) {
                target_stack->show(); 
                target_stack = target_stack->next_stack;
            }        
            cout << ">\n";  
        }
};


int main() {
    SetOfStacks<int> SS(3);
    // SS.show();

    for (int i=0; i<10; i++){
        SS.push(i);
        // SS.show();
    }

    for (int i=0; i<5; i++){
        SS.pop();
        // SS.show();
    }

    for (int i=0; i<4; i++){
        SS.push(-i-1);
        // SS.show();
    }

    SS.show();
    for (int i=0; i<4; i++){
        SS.pop_at(1);
        SS.show();
    }
}