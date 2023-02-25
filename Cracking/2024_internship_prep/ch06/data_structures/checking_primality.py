from math import sqrt

def prime_with_square(N: int) -> bool:
    if N < 2:
        return False
    
    sq = sqrt(N)
    for i in range(2, int(sq)+1):
        if N % i == 0:
            return False

    return True

class ListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        
        return self.next


def generate_prime_list_with_sieve_of_eratosthenes(N: int) -> list:
    temp = [i for i in range(2, N+1)]
    result = []
    idx = 0
    while idx < len(temp):
        curr = idx+1
        while curr < len(temp):
            if temp[curr] % temp[idx] == 0:
                temp.pop(curr)
            else:
                curr += 1
            # print(result)
        result.append(temp[idx])
        idx += 1
    return temp

if __name__ == '__main__':
    for i in range(15):
        print(f"{i} - Prime : {prime_with_square(i)}")
    
    print(generate_prime_list_with_sieve_of_eratosthenes(50))