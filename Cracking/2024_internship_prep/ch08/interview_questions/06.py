class TowersOfHanoi:
    def __init__(self, size):
        self._size = size
        self._towers = [[] for i in range(3)]
        for i in range(size, 0, -1):
            self._towers[0].append(i)
    
    def play(self):
        self.move_rings_at_once(0, 2, self._size)
    
    def move_rings_at_once(self, _from, _to, level):
        if level == 1:
            self.move_ring(_from, _to)
            return
        
        temp_set = set([0, 1, 2])
        # print('Set : {} / remove target : {}'.format(temp_set, self._towers.index(tower_from)))
        temp_set.remove(_from)
        # print('Set : {} / remove target : {}'.format(temp_set, self._towers.index(tower_to)))
        temp_set.remove(_to)
        third_idx = temp_set.pop()

        self.move_rings_at_once(_from, third_idx, level-1)
        self.move_ring(_from, _to)
        self.move_rings_at_once(third_idx, _to, level-1)
    
    def move_ring(self, _from, _to):
        tower_from, tower_to = self._towers[_from], self._towers[_to]
        if len(tower_from) == 0:
            raise Exception("No ring at tower_from.")
        print("\nmove_ring {} ({} -> {})".format(tower_from[-1], self._towers.index(tower_from), self._towers.index(tower_to)))
        if len(tower_to) > 0 and tower_from[-1] > tower_to[-1]:
            raise Exception("Cannot put big ring on small ring.")
        tower_to.append(tower_from.pop())
        self.show_towers()
    
    def show_towers(self):
        text_list = []
        max_digits_rev = [1] * 3
        for i, tower in enumerate(reversed(self._towers)):
            if len(tower) > 0:
                max_digits_rev[i] = len(str(tower[0]))
        
        for digits in max_digits_rev:
            for k in range(digits+1):
                text_list.append('-')
        text_list.append('\n')

        for i in range(self._size):
            for j, tower in enumerate(reversed(self._towers)):
                if len(tower) <= i:
                    for k in range(max_digits_rev[j]):
                        text_list.append(' ')
                else:
                    ring_str = str(tower[i])
                    for k in range(max_digits_rev[j]-len(ring_str)):
                        text_list.append(' ')
                    text_list.append(ring_str)
                text_list.append(' ')
            text_list.append('\n')
            
        for digits in max_digits_rev:
            for k in range(digits+1):
                text_list.append('-')
        text_list.append('\n')

        print(''.join(reversed(text_list)))


if __name__ == '__main__':
    T1 = TowersOfHanoi(5)
    T1.show_towers()

    # T1.move_ring(0, 1)
    # T1.show_towers()
    # # T1.move_ring(0, 1)
    # # T1.show_towers()
    # # T1.move_ring(1, 2)
    # # T1.show_towers()
    # T1.move_ring(0, 2)
    # T1.show_towers()

    # T1.move_rings_at_once(0, 1, 1)
    # T1.move_rings_at_once(0, 2, 3)

    T1.play()
