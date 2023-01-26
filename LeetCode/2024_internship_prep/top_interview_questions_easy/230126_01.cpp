#include <vector>
#include <iostream>
using namespace std;

int maxProfit(vector<int>& prices) {
    if (prices.size() == 1) return 0;
    
    int date = 0;
    int position_price = -1;
    bool up_flag = false;
    int total_profit = 0;
    
    while (prices[date] >= prices[date+1] && date < prices.size()-1) date++;
    
    if (date < prices.size()-1){
        position_price = prices[date];
        up_flag = true;
    }
    
    while (date < prices.size()-1){
        if (up_flag && prices[date+1] < prices[date]){
            total_profit += prices[date] - position_price;
            position_price = -1;
            up_flag = false;
        } else if (!up_flag && prices[date+1] > prices[date]){
            position_price = prices[date];
            up_flag = true;
        }
        date++;
    }
    
    if (position_price >= 0 && prices.back() > position_price){
        total_profit += prices.back() - position_price;
    }
    
    return total_profit;
}


int main(){
    // vector<int> v1 = {2, 1};
    // printf("%d\n", maxProfit(v1));

    vector<int> v2 = {2,1,2,0,1};
    printf("%d\n", maxProfit(v2));
}