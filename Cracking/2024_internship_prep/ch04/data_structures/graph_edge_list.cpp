#include <iostream>
#include <vector>
#include <exception>
using namespace std;

template <typename T>
class Graph{
    public:
        class Vertex{
            private:
                T element;
            public:
                Vertex(T t) : element(t) {};
                
                T get_element() {return this->element;};
        };

        class Edge{
            private:
                Vertex *origin;
                Vertex *destination;

            public:
                Edge(Vertex* V1, Vertex* V2) : origin(V1), destination(V2) {};

                void show_edge(){
                    cout << this->origin->get_element() << " -> " << this->destination->get_element() << endl;
                }
        };

        vector<Vertex*> vertices;
        vector<Edge*> edges;

        Graph() {};

        Vertex* add_vertex(T t){
            Vertex *new_vertex = new Vertex(t);
            this->vertices.push_back(new_vertex);
            return new_vertex;
        }

        Edge* add_edge(Vertex* V1, Vertex* V2){
            Edge *new_edge = new Edge(V1, V2);
            this->edges.push_back(new_edge);
            return new_edge;
        }
};


int main(){
    Graph<int> G1;
    auto v1 = G1.add_vertex(1);
    auto v2 = G1.add_vertex(2);
    auto v3 = G1.add_vertex(3);

    for (auto v : G1.vertices){
        cout << v->get_element() << " ";
    }

    G1.add_edge(v1, v2);
    G1.add_edge(v2, v3);

    for (auto e : G1.edges){
        e->show_edge();
    }
}