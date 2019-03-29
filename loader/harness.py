
from ..asm.AbsoluteAddress import AbsoluteAddress

class harness:
    PROLOGUE_BASE = 0xface0000
    EPILOGUE_BASE = 0xfee70000

    prologue_address = AbsoluteAddress(PROLOGUE_BASE)
    epilogue_address = AbsoluteAddress(EPILOGUE_BASE)

    def install(program):
        raise Exception("Virtual function 'install' not defined")
    
    def contains(a):
        raise Exception("Virtual function 'contains' not defined")

    def get_fallthrough_address(a):
        raise Exception("Virtual function 'get_fallthrough_address' not defined")
