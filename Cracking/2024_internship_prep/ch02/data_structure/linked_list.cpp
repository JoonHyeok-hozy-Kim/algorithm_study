
template <typename T>
class LinkedList{
    class Node{
    public:
        Node *next;
        T value;

        Node();
        Node(int a) { value = a; };
        Node(int a, Node *next_node) {
            next = next_node;
            value = a;
        }
    };

    public:
        Node header;
        Node trailer;
        int size = 0;

        LinkedList();

        Node get(T t){
            Node result = this->header;
            while (result != this->trailer){
                if (result.value == t){
                    break;                    
                } else {
                    result = *(result.next);
                }
            }
            return result;
        }
};