#include <iostream>
using namespace std;
#define NAME_SIZE 50

class Person {
    protected:
        int id;
        string name;

    public:
        Person(int id, string name) : id(id), name(name) {};
        virtual ~Person() { cout << "Person deleted." << endl; };

        virtual void aboutMe() {
            cout << "I am " << this->name << "." << endl;
        };
};

class Student : public Person {
    public:
        Student(int id, string name) : Person(id, name) {};
        ~Student() { cout << "Student deleted." << endl; };

        void aboutMe() {
            cout << "I am a " << this->name << ", a student." << endl;
        }
};

int main() {
    Person *p1 = new Person(1, "hozy");
    p1->aboutMe();

    Student *s1 = new Student(2, "AJ");
    s1->aboutMe();

    Person *s2 = new Student(2, "AJ");
    s2->aboutMe();

    delete p1;
    delete s1;
    delete s2;
}