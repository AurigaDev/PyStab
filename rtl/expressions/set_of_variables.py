from rtl.expressions.set_of_variables import SetOfVariables

class SetOfVariables():
    serial_version_uid = -5505393011046912608

    def __init__(self, collection=None):
        self.bit_set = BitSet(ExpressionFactory.DEFAULT_VARIABLE_COUNT)
        
        if not collecction == None:
            add_all(collection)

    EMPTY_SET = SetOfVariables()
    

    def add(self, rtl_var:RTLVariable) -> bool:
        if self.bit_set.get(e.get_index()):
            return False
        self.bit_set.set(e.get_index())
        return True


    def add_all(self, _input) -> bool:
        changed = False

        for element in c:
            changed |= self.add(element)
        
        return changed

    
    def clear(self) -> None:
        self.bit_set.clear()

    
    def contains(self, obj) -> bool:
        if isinstance(obj, RTLVariable):
            return self.get(obj.get_index())
        else:
            return False

    
    def equals(self, _input) -> bool:
        if isinstance(obj, SetOfVariables):
            return (not _input == None) and (self.bit_set.equals(_input.bit_set))
        else:
            return __super__.equals(_input)


    def hash_code(self) -> int:
        return self.bit_set.hash_code()

    
    def is_empty(self) -> bool:
        return self.bit_set.is_empty()