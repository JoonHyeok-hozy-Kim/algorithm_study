#include <iostream>
using namespace std;

class MyString {
    public:
        string content;

        MyString(string content) : content(content) {};
        MyString(const MyString& str) { this->content = str.content; }
        ~MyString() {};
        bool operator==(const MyString& str);
};

bool MyString::operator==(const MyString& str){
    if (this->content.size() != str.content.size()) {
        return false;
    }

    for (int i = 0; i < this->content.size(); i++) {
        if ((this->content)[i] != (str.content)[i]) {
            return false;
        }
    }

    return true;
}


int main() {

    MyString s1 = MyString("abc");
    MyString s2 = MyString("abc");

    // cout << boolalpha << (s1 == s 2) << endl;
}