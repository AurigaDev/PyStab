from asm.absolute_address import AbsoluteAddress

class StubProvider:
  STUB_BASE         = 0xFF000000
  # Stack is not cleared
  CDECL             = 0
  # all parameters on stack, stack is cleared
  STDCALL           = 1
  # two parameters in registers, remaining on stack, stack is cleared
  FASTCALL          = 2
  # non-function, but a variable
  EXTERNAL_VARIABLE = 3

  def resolve_symbol(library:str, symbol:str) -> AbsoluteAddress:
    raise Exception('Function not defined')
  
  def get_symbol_finder():
    raise Exception('Function not defined')

