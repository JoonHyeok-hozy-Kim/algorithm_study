#include <iostream>
#include <vector>
#include <exception>
#include <deque>
using namespace std;

template <typename T>
class Graph{
    public:
        class Vertex{
            protected:
                T element;
                vector<Vertex*> children;
            public:
                Vertex(T t) : element(t) {};
                
                T get_element() {return this->element;};
                
                void add_child(Vertex* V){
                    this->children.push_back(V);
                }

                void dfs_show(){
                    cout << this->get_element() << " ";
                    for (auto c : this->children){
                        c->dfs_show();
                    }
                }

                void bfs_show(){
                    deque<Vertex*> Q;
                    Vertex* temp;
                    Q.push_back(this);
                    while (!Q.empty()){
                        temp = Q.front();
                        Q.pop_front();
                        for (auto c : temp->children){
                            Q.push_back(c);
                        }
                        cout << temp->get_element() << " ";
                    }
                }
        };

        vector<Vertex*> vertices;

        Graph() {};

        Vertex* add_vertex(T t){
            Vertex *new_vertex = new Vertex(t);
            this->vertices.push_back(new_vertex);
            return new_vertex;
        }
};


int main(){
    Graph<int> G1;
    auto v1 = G1.add_vertex(1);
    auto v2 = G1.add_vertex(2);
    auto v3 = G1.add_vertex(3);
    auto v4 = G1.add_vertex(4);

    for (auto v : G1.vertices){
        cout << v->get_element() << " ";
    }
    cout << endl;

    v1->add_child(v2);
    v2->add_child(v3);
    v1->add_child(v4);

    v1->dfs_show();
    cout << endl;
    v1->bfs_show();
    cout << endl;
}