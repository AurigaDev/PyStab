from rtl.expressions.writable import Writable

class Context:
  def __init__(proto=None):
    self.substitutions = {}
    self.assignments = {}
    if proto is not None:
      for sub in proto.substitutions:
        self.substitutions[sub] = proto.substitutions[sub]
      for ass in proto.assignments:
        self.assignments[ass] = proto.assignments[ass]

  
  def substitute(self, w:Writable, expr:RTLExpression) -> None:
    if isinstance(w, RTLBitRange):
      self.substitutions[w] = expr
    else:
      raise Exception("Invalid Type of Argument")


  def add_assignment(self, w:Writable, expr:RTLExpression) -> None:
    if isinstance(w, RTLBitRange):
      self.assignments[w] = expr
    else:
      raise Exception("Invalid Type of Argument")


  def remove_assignment(self, _input) -> bool:
    if isinstance(_input, Writable):
      if _input in self.assignments:
        del self.assignments[_input]
        return True
      else:
        return False
    elif isinstance(_input, SetOfVariables):
      all_removable = False
      for var in _input:
        if var in self.assignments:
          del self.assignments[var]
        else:
          all_removable = False
      return all_removable
    else:
      raise Exception("Invalid Type of Argument")


  def get_substitution(self, w:Writable) -> RTLExpression:
    if w in self.substitutions:
      rtl_expr_res = self.substitutions[w]
    else:
      return w
    
    if rtl_expr_res is not None:
      return rtl_expr_res
    else:
      return w


  def get_assignment(self, w:Writeable) -> RTLExpression:
    if w in self.assignments:
      rtl_expr_res = self.assignments[w]
    else:
      return w
    
    if rtl_expr_res is not None:
      return rtl_expr_res
    else:
      return w


  def get_assignments(self):
    return self.assignments

  
  def get_substitutions(self):
    return self.substitutions