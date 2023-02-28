# 6.1 : The Heavy Pill
### You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once. 

* Sol
  1. Number bottles from 1 to 20.
  2. Then, for the i-th bottle, put (10)^(i-1) pills on the scale.
  3. Get the weight from the scale.
  4. If the result contains 0.1 then the first bottle has 1.1 gram pills.
  5. Else, check where 2 is at. If 2 is at j-th digit starting from the least significant digit, (j+1)-th bottle will have 1.1 gram pills.

* Test with code
  ```python
  def get_unique_bottle(bottles: list) -> int:
    weight = 0
    power = 1
    for i in range(len(bottles)):
        weight += bottles[i] * power
        power *= 10
    
    if weight - int(weight) > 0:
        return 1
    else:
        cnt = 2
        int_weight = int(weight)
        while int_weight > 0:
            if int_weight % 10 == 2:
                return cnt
            else:
                int_weight //= 10
                cnt += 1

    return None

  if __name__ == '__main__':
    B = [1.0] * 20
    for i in range(20):
        B[i] = 1.1
        print(f"answer : {i+1}, result : {get_unique_bottle(B)}")
        B[i] = 1.0
  ```

# 6.2 Basketball
### You have a basketball hoop and someone says that you can play one of two games. 
* Game 1: You get one shot to make the hoop. 
* Game 2: You get three shots and you have to make two of three shots. 
### If p is the probability of making a particular shot, for which values of p should you pick one game or the other?

* Sol
  * The probability to win Game 1 is p.
  * The probability to win Game 2 is p^3 + 3 * p^2 * (1-p) = p^2 * (p + 3 - 3p) = p^2 * (3-2p)
  * Thus, if p > p^2 (3-2p), we must choose Game 1.
  * Hence, if p < 1/2, choose, Game 1. Else, Choose Game 2.


# 6.3 Dominos
### There is an 8x8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominos, and a single domino can cover exactly two squares. Can you use the 31 dominos to cover the entire board? Prove your answer (by providing an example or showing why it's impossible). 

![](https://github.com/JoonHyeok-hozy-Kim/algorithm_study/blob/main/Cracking/2024_internship_prep/ch06/interview_questions/03.png)

* Sol.
  * Suppose we are filling the edges of the board first.
  * Since two corners are cut-off, there will be exactly two slots that cannot be filled in two different edges. If we fill them with additional domino, the result will be another cut-off chess board with its size of 7X7.
  * Repeating the same operation with 7X7 board, we may get the cut-off board of 6X6.
  * This operation can be repeated until we get the 2X2 cut-off board, which is innately impossible to fill up with the dominos.


# 6.4 Ants on a Triangle
### There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed. Similarly, find the probability of collision with n ants on an n-vertex polygon. 

* Sol.
  * The action that each ant can take is choosing either left or right side.
  * Thus, the total number of cases that can take place is 2^3 = 8.
  * And there are only two cases that no ant collide with one another.
    * All of them choosing the identical direction, either left or right.
  * Hence, the probability that the collision takes place is 1 - (2/8) = 3/4
  * This can be generalized to N-polygon problem as follows.
    * There will be N ants choosing left or right, so the number of every cases is 2^N.
    * Again, there will be only two cases that no ant collide with another.
    * Thus, 1 - (2 / 2^N) = 1 - (1/2^(N-1)).


# 6.5 Jugs of Water
### You have a five-quart jug, a three-quart jug, and an unlimited supply of water (but no measuring cups). How would you come up with exactly four quarts of water? Note that the jugs are oddly shaped, such that filling up exactly "half" of the jug would be impossible. 

* Sol.
  * Fill the five-quart jug and pour them into the three-quart jug.
  * Gather the spilt water.
  * Repeat this again and you will have 4-quart of water.


# 6.6 Blue-Eyed Island
### A bunch of people are living on an island, when a visitor comes with a strange order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at 8:00 pm every evening. Each person can see everyone else's eye color, but they do not know their own (nor is anyone allowed to tell them). Additionally, they do not know how many people have blue eyes, although they do know that at least one person does. How many days will it take the blue-eyed people to leave?

* Sol.
  * Case 1) If there is one blue-eyed.
    * The only blue eyed knows that there is at least one blue-eyed person in island but no one around him/her has blue eyes. So, he/she will realize that the blue-eyed is him/her and leave immediately.
  * Case 2) 2 blue-eyed.
    * Knowing Case 1), blue-eyed will assume that the other blue eyed will leave right away. However, the other won't leave because he/she found another blue-eyed. Both of them witnessed that there exists one blue-eyed exists in the island but not leaving, they will realize that they themselves are the blue-eyed as well and leave the next day.
  * Case N) N blue-eyed.
    * Blue-eyed people will leave on (N-1)-th day.


# 6.7 The Apocalypse
### In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy that is, they have continue to have children until they have one girl, at which point they immediately stop-what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.

* Sol.
  * Suppose there are N people in the world.
  * Then N/2 will have one girl.
  * And N/4 will have one girl and one boy.
  * And N/8 will have one girl and two boys.
  * And N/16 will have one girl and three boys.
  * And so on.
  * Thus, the total number of second generation will be as follows.
    $$ N \sum\limits_{k=1}^{[log(n)]} {k \over 2^k} $$


# 6.8 The Egg Drop Problem
### There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break. If it's dropped from any floor below, it will not break. You're given two eggs. Find N, while minimizing the number of drops for the worst case. 

* Sol.
  * Load balancing is required
  * How?
    * Let two eggs, e1 and e2, where e1 will be dropped prior to egg2.
    * Dropping scenario for e1 and e2 can be depicted as follows.
      1. Suppose e1 was dropped on f1 floor.
        * If e1 breaks, then e2 should be dropped at most f1-1 times.
          * why?) 1 ~ f1-1
      2. Else, we may drop e1 on (f1+f2) floor.
        * If e1 breaks, then e2 should be drooped at most f2-1 times.
          * why?) (f1+1) ~ (f1+f2-1)
      3. Else, we may drop e1 on (f1+f2+f3) floor.
        * If e1 breaks, then e2 should be drooped at most f3-1 times.
          * why?) (f1+f2+1) ~ (f1+f2+f3-1)
    * We may balance the load of e2 by gradually reducing the potential drop of e2.
      * We can achieve this by setting f2 = f1-1, f3 = f2-1, ... , fn = f(n-1)-1
      * Thus, set f1 such that f1 + (f1-1) + (f1-2) + ... + 1 = 100
      * Then f1 = 13.65
    * Now compare f1 = 13 and f1 = 14
      * Case 1) f1 = 13
         |Round|1|2|3|4|5|6|7|8|9|
         |---|-|-|-|-|-|-|-|-|-|
         |e1 Steps|13|12|11|10|9|8|7|6|5|4|3|2|1|
         |e1 New Floor|13|25|36|46|55|63|70|76|81|85|88|90|91|
         |e2 Potential Drops|12|11|10|9|8|7|6|5|4|3|2|1|**10**|
         * Final potential drop of e2 is 10 -> NOT BALANCED!
      * Case 1) f1 = 13
         |Round|1|2|3|4|5|6|7|8|9|
         |---|-|-|-|-|-|-|-|-|-|
         |e1 Steps|14|13|12|11|10|9|8|7|6|5|4|
         |e1 New Floor|14|27|39|50|60|69|77|84|90|95|99|
         |e2 Potential Drops|13|12|11|10|9|8|7|6|5|4|3|
         * Balanced!
    * Therefore, 14 is idealistic! 


# 6.9 100 Lockers
### There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?

* Sol
  * The i-th locker must have been toggled by (the number of divisors excluding 1) times
    |i       |**1**|2|3|**4**|5|6|7|8|**9**|10|
    |--------|-|-|-|-|-|-|-|-|-|--|
    |divisors|-|2|3|2,4|5|2,3,6|7|2,4,8|3,9|2,5,10|
    |count   |**0**|1|1|**2**|1|3|1|3|**2**|3|
  * Only the perfect square numbers will be left opened!


# 6.10 Poison
### You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible? 
* FOLLOW UP 
### Write code to simulate your approach. 

* Sol
  * By implementing binary search, you may get the result in 70 days.