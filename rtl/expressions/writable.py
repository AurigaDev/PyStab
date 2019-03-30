from rtl.expressions.set_of_variables import SetOfVariables

class Writable(RTLExpression):

  def get_used_on_write() -> SetOfVariables:
    raise Exception("Function has not been defined")
      
  def get_defined_variable_on_write() -> SetOfVariables:
    raise Exception("Function has not been defined")

  def get_used_memory_location_on_write() -> set:
    raise Exception("Function has not been defined")

  def get_defined_memory_locations_on_write() -> set:
    raise Exception("Function has not been defined")
