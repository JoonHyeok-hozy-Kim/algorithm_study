from collections import deque

class Slot:
    def __init__(self):
        self._id = id
        self._timer_start = None
    
    def fill(self, start_time):
        self._timer_start = start_time
    
    def empty(self, time):
        time_cnt = time - self._timer_start
        self._timer_start = None
        return time_cnt

class Car:
    def __init__(self, id, entrance_time):
        self._id = id

class ParkingLot:
    def __init__(self, size) -> None:
        self._slots = deque()
        for i in range(size):
            self._slots.append(Slot(i))
        self._parked = {}
        self._capacity = size
        self._occupied = 0
        self._time = 0
    
    def is_available(self):
        return self._capacity > self._occupied
    
    def park(self, car):
        if not self.is_available():
            raise Exception()
        new_slot = self._slots.popleft()
        new_slot.fill(self._time)
        self._parked[car] = new_slot
        self._occupied += 1
    
    def get_out(self, car):
        if self._occupied == 0:
            raise Exception()
        if car not in self._parked:
            raise Exception()
        target_slot = self._parked[car]
        del self._parked[car]
        self._occupied -= 1

        occupied_time = target_slot.empty(self._time)
        return occupied_time