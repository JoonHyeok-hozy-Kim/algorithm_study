#include <vector>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
    for (auto i=digits.rbegin(); i!=digits.rend(); i++){
        if (*i < 9){
            *i += 1;
            return digits;
        } else {
            *i = 0;
        }
    }
    
    if (digits[0] == 0){
        digits.insert(digits.begin(), 1);
    }
    
    return digits;
}