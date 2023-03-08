class Employee:
    def __init__(self, title, upper_class=None):
        self._available = True
        self._title = title
        self._upper_class = upper_class
    
    def get_available(self):
        if self._available:
            return self
        elif self._upper_class is not None:
            return self._upper_class.get_available()
        else:
            return None
    
    def get_call(self):
        self._available = False

    def finish_call(self):
        self._available = True

    def __str__(self):
        text_list = []
        text_list.append(self._title)
        text_list.append('(')
        if self._available:
            text_list.append('O')
        else:
            text_list.append('X')
        text_list.append(')')
        return ''.join(text_list)


class Group:
    def __init__(self, manager):
        self._members = []
        self._manager = manager
    
    def add_member(self, member):
        self._members.append(member)
    
    def dispatch_call(self):
        target = None
        for member in self._members:
            if member._available:
                target = member
                break
        
        if target is None:
            target = self._manager.get_available()
        
        if target:
            target.get_call()
        
        return target

    def __str__(self):
        text_list = ["---<Group>---\n"]
        text_list.append(str(self._manager))
        text_list.append('\n')
        for member in self._members:
            text_list.append(str(member))
            text_list.append(" ")
        text_list.append("\n-------------")
        return ''.join(text_list)


if __name__ == '__main__':
    director = Employee("Director")
    managers = [Employee("Manager", director) for i in range(3)]
    groups = [Group(m) for m in managers]
    for g in groups:
        for i in range(5):
            g.add_member(Employee("Respondent", g._manager))
    
    print("==================================")
    print(director)
    for g in groups:
        print()
        print(g)
    print("==================================")
    
    groups[0].dispatch_call()
    
    print("==================================")
    print(director)
    for g in groups:
        print()
        print(g)
    print("==================================")

    for i in range(7):
        groups[1].dispatch_call()
        print("==================================")
        print(director)
        for g in groups:
            print()
            print(g)
        print("==================================")