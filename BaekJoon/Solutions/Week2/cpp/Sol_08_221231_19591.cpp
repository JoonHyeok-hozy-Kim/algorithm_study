/*
독특한 계산기
https://www.acmicpc.net/problem/19591
*/

#include <iostream>
#include <string>
#include <deque>
#include <typeinfo>
// #include <cstdio>
// #include <cstdlib>
using namespace std;

typedef long long ll;

ll operate(ll oprnd1, ll oprnd2, char oprtr){
    switch (oprtr){
        case '+':
            return oprnd1 + oprnd2;
        case '-':
            return oprnd1 - oprnd2;
        case '*':
            return oprnd1 * oprnd2;
        case '/':
            return oprnd1 / oprnd2;
        default:
            break;
    }
}

void compare(deque<ll> * nd, deque<char> * od){
    ll front_num, back_num, front_temp, back_temp;
    if ((od->front() == '*' || od->front() == '/') && (od->back() == '+' || od->back() == '-')){
        front_num = nd->front();
        nd->pop_front();
        front_temp = operate(front_num, nd->front(), od->front()); 
        od->pop_front();
        nd->pop_front();
        nd->push_front(front_temp);
        return;
    } else if ((od->back() == '*' || od->back() == '/') && (od->front() == '+' || od->front() == '-')) {
        back_num = nd->back();
        nd->pop_back();
        back_temp = operate(nd->back(), back_num, od->back());
        od->pop_back();
        nd->pop_back();
        nd->push_back(back_temp);
        return;
    } else {
        front_num = nd->front();
        nd->pop_front();
        back_num = nd->back();
        nd->pop_back();

        front_temp = operate(front_num, nd->front(), od->front()); 
        back_temp = operate(nd->back(), back_num, od->back());
        if (front_temp >= back_temp){
            od->pop_front();
            nd->pop_front();
            nd->push_front(front_temp);
            nd->push_back(back_num);
        } else {
            od->pop_back();
            nd->push_front(front_num);
            nd->pop_back();
            nd->push_back(back_temp);
        }
    }
}


int main(){

    // printf("%d\n", operate(6, 3, '+'));
    // printf("%d\n", operate(6, 3, '-'));
    // printf("%d\n", operate(6, 3, '*'));
    // printf("%d\n", operate(6, 3, '/'));

    // 3 / 2       = 1, 
    // (−3) / 2    = −1, 
    // 3 / (−2)    = −1, 
    // (−3) / (−2) = 1
    // printf("%d\n", 3 / 2      );
    // printf("%d\n", (-3) / 2   );
    // printf("%d\n", 3 / (-2)   );
    // printf("%d\n", (-3) / (-2));

    string expr;
    cin >> expr;
    // cout << expr << endl;

    deque<ll> num_deque;
    deque<char> opr_deque;

    int cnt = 0;
    ll sign;
    ll temp_num;
    int zero_ascii = '0';
    // cout << zero_ascii << endl;
    bool new_num = true;

    for (auto i=expr.begin(); i!=expr.end(); i++){
        // cout << *i << endl;
        if (i == expr.begin() && *i == '-'){
            sign = -1;
            continue;
        }

        if (isalnum(*i)){
            // cout << "alnum : " << *i << endl;
            if (new_num){
                temp_num = (ll) (*i - zero_ascii);
                new_num = false;
            } else {
                temp_num *= 10;
                temp_num += (ll) (*i - zero_ascii);
            }
        } else {
            // cout << "els : " << *i << endl;
            if (sign == -1){
                temp_num *= sign;
                sign = 1;
            }       
            num_deque.push_back(temp_num);
            new_num = true;
            opr_deque.push_back(*i);
        }
    }

    if (sign == -1) temp_num *= sign;
    num_deque.push_back(temp_num);

    // for (int n : num_deque) cout << n << endl;
    // for (char o : opr_deque) cout << o << endl;

    if (opr_deque.empty()){
        printf("%lld", num_deque.front());
    } else {
        while (!opr_deque.empty()){
            // for (int i=0; i<num_deque.size(); i++){
            //     cout << num_deque[i];
            //     if (i<num_deque.size()-1){
            //         cout << opr_deque[i];
            //     } else {
            //         cout << endl;
            //     }
            // }

            if (opr_deque.size() == 1){
                printf("%lld", operate(num_deque.front(), num_deque.back(), opr_deque.front()));
                opr_deque.pop_front();
            } else {
                compare(&num_deque, &opr_deque);
            }
        }
    }
}