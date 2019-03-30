from asm.address import Address

class AbsoluteAddress(Address):
    value = None

    def __init__(self,input):
        # Combining Constructors
        if isinstance(value,RTLNumber()):
            if (input.get_bit_width()==16):
                self.value = 0xFFFF & input.long_value()
            elif (input.get_bit_width()==32):
                self.value = 0xFFFFFFFF & input.long_value()
            else:
                self.value = input.long_value()  
        else:
            self.value =value

    def to_numeric_constant():
        ExpressionFactory.create_number(value, get_bit_width())       
        # Define get_bit_width later

    def compare_to(self,abs_address):
        if (self.value < abs_address.value):
            return -1
        elif (self.value > abs_address.value):
            return 1
        else:
            return 0

    def get_value(self):
        return self.value

    def get_effective_value(pc_value):
        return get_value()

    def to_string():
        sb = ""
        sb+="0x"
        sb+="%08x"%value
        return sb
    
    def hash_code(self):
        prime = 31
        result = 1
        result = prime * result +(self.value ^ (value >> 32))
        return result

    def equals(self,obj):
        if (obj == None):
            return False
        elif (self == obj):
            return True
        elif (obj.__class__.___name___ != self.__class__.__name__):
            return False
        other = obj
        if (self.value != other.value):
            return False
        return True






