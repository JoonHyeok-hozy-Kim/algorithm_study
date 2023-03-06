
class PoisonCheck:
    class Bottle:
        def __init__(self, id, poisoned=False):
            self.id = id
            self.poisoned = poisoned


    class TestStrip:
        def __init__(self, id, poisoned=False):
            self.id = id
            self.poisoned = poisoned
        
        def is_poisoned(self):
            return self.poisoned
    
    class Test:
        def __init__(self, test_strip, start_date):
            self.poisoned = False
            self.bottles = []
            self.strip = test_strip
            self.start_date = start_date

            
        def add_bottle(self, bottle):
            self.bottles.append(bottle)

        
        def start_test(self):
            for b in self.bottles:
                if b.poisoned:
                    self.poisoned = True
                    break

        
        def get_result(self, check_date):
            if check_date >= self.start_date + 7 and self.poisoned:
                self.strip.poisoned = self.poisoned
                print('self.poisoned : {} / strip.poisoned : {}'.format(self.poisoned, self.strip.poisoned))
                return True
            return False
        

    def __init__(self, bottle_cnt, poisoned_bottle_idx, strip_cnt):
        self.bottles = [None] * bottle_cnt
        self.strips = [None] * strip_cnt
        self.date = 0
        self.test_queue = {}

        for i in range(bottle_cnt):
            self.bottles[i] = self.Bottle(i)
        
        self.bottles[poisoned_bottle_idx].poisoned = True

        for i in range(strip_cnt):
            self.strips[i] = self.TestStrip(i)

    
    def show_test_strips(self):
        test_list = ["Date ", str(self.date), "\n"]
        strip_cnt = len(self.strips)
        max_length = len(str(strip_cnt - 1))            
        
        for i in range(strip_cnt * (max_length+1)):
            test_list.append('-')
        test_list.append('\n')

        for i in range(len(self.strips)):
            for j in range(max_length-len(str(i))):
                test_list.append(' ')
            test_list.append(str(i))
            test_list.append(' ')
        test_list.append('\n')

        for i in range(len(self.strips)):
            for j in range(max_length-1):
                test_list.append(' ')
            if self.strips[i].poisoned:
                test_list.append('P')
            else:
                test_list.append('-')
            test_list.append(' ')
        test_list.append('\n')
        
        for i in range(strip_cnt * (max_length+1)):
            test_list.append('-')
        test_list.append('\n')

        print(''.join(test_list)) 


    def add_date(self):
        if self.date in self.test_queue:
            target_case = self.test_queue[self.date]
            for test in target_case:
                if test.get_result(self.date):
                    break
            del self.test_queue[self.date]
        self.date += 1


    def set_test(self):
        if self.date + 7 in self.test_queue:
            raise Exception("Test already done on this date.")
        test_case = []
        for s in self.strips:
            test_case.append(self.Test(s, self.date))
        self.test_queue[self.date + 7] = test_case
        return test_case


if __name__ == '__main__':
    P = PoisonCheck(1000, 628, 10)

    test_case1 = P.set_test()
    for bottle in P.bottles:
        test_case1[bottle.id % 10].add_bottle(bottle)
    for test in test_case1:
        test.start_test()
    P.show_test_strips()

    P.add_date()
    test_case2 = P.set_test()
    for bottle in P.bottles:
        if bottle.id == 1000:
            break
        test_case2[(bottle.id // 10) % 10].add_bottle(bottle)
    for test in test_case2:
        test.start_test()
    P.show_test_strips()

    P.add_date()
    test_case3 = P.set_test()
    for bottle in P.bottles:
        if bottle.id == 1000:
            break
        test_case3[(bottle.id // 100) % 10].add_bottle(bottle)
    for test in test_case3:
        test.start_test()
    P.show_test_strips()

    for i in range(8):
        P.add_date()
        P.show_test_strips()
