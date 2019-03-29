from harness import Harness

class HeuristicHarness(Harness):
    CALL_INSTR_DISTANCE = 1
    procedure_heads = [[-0x75, -0x1, 0x55, -0x75, -0x14],
                       [0x55, -0x75, -0x14]]
    
    def __init__(self):
        self.program = Program.get_program()

        if isinstance(program.get_main_module(),AbstractCOFFModule):


    def install(self, program):
        seq = StatementSequence()

    def clear_reg(seq, rtl_var):
        seq.add_last(RTLVariableAssignment(rtl_var.get_bit_width(), 
                     rtl_var, ExpressionFactory.nondet(rtl_var.get_bit_width())))

    def put_sequence(seq, rtl_var):
        


    def contains(abs_addr):
        return abs_addr.get_value() >= PROLOGUE_BASE and
               abs_addr.get_value() <= last_address.get_value()

    def get_fallthrough_address(self, abs_addr):
        if abs_addr >= PROLOGUE_BASE and 
        abs_addr.get_value() <= last_address.get_value():
            return AbsoluteAddress(abs_addr.get_value+CALL_INSTR_DISTANCE)
        elif abs_addr.equals(last_address):
            return epilogue_address
        else:
            return None