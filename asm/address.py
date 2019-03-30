from asm.operand import Operand

class Address(Operand, BitVectorType):
  def get_effective_value(pc_value):
    return -1

  
  def get_bit_width() -> int:
    return 32


  def to_string(current_pc:int, sym_finder:SymbolFinder) -> str:
    address = get_effective_value(current_pc)
    if address < 0:
      return ""
    else:
      return sym_finder.get_symbol_for(address)
