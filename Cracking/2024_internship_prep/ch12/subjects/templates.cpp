template <class T>
class ShiftedList {
        T* array;
        int offset, size;
    public:
        ShiftedList(int size) : offset(0), size(size) {
            array = new T[size];
        };

        ~ShiftedList() {
            delete[] array;
        }

        void shiftBy(int n){
            offset = (offset+n) % size;
        }

        T get(int i){
            return array[convertIndex(i)];
        }

        void set(T item, int i){
            array[convertIndex(i)] = item;
        }
    
    private:
        int convertIndex(int i){
            int index = (i - offset) % size;
            while (index < 0) index += size;
            return index;
        }
};