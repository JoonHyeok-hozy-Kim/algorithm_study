#include <stdlib.h>
#include <iostream>
using namespace std;

template <typename T>
class SmartPointer {
    public:
        SmartPointer(T* ptr) {
            ref = ptr;
            ref_cnt = (unsigned *) malloc(sizeof(unsigned));
            *ref_cnt = 1;
        };

        SmartPointer(SmartPointer<T>& sptr) {
            ref = sptr.ref;
            ref_cnt = sptr.ref_cnt;
            ++(*ref_cnt);
        };

        SmartPointer<T> & operator=(SmartPointer<T>& sptr) {
            if (this == &sptr) return *this;

            if (*ref_cnt > 0){
                remove();
            }

            ref = sptr.ref;
            ref_cnt = sptr.ref_cnt;
            ++(*ref_cnt);
            return *this;
        }

        ~SmartPointer() {
            cout << "Destruct " << this->getValue() << endl;
            remove();
        };

        T getValue() {
            return *ref;
        }

    protected:
        void remove() {
            --(*ref_cnt);
            if (*ref_cnt == 0) {
                delete ref;
                free(ref_cnt);
                ref = NULL;
                ref_cnt = NULL;
            }
        }
    
    T * ref;
    unsigned * ref_cnt;
};


int main() {
    int *a = new int[1];
    a[0] = 3;
    SmartPointer<int> *s1 = new SmartPointer<int>(a);

    cout << s1->getValue() << endl;
    
    SmartPointer<int> *s2 = new SmartPointer<int>(*s1);
    delete s2;
}