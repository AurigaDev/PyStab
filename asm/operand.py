from rtl.context import Context

class Operand:
    def evaluate(self, ctx:Context) -> Operand:
        rtl_expression = ExpressionFactory().create_operand(self)
        rtl_expr_eval = rtl_expression.evaluate(ctx)

        if rtl_expression.equals(rtl_expr_eval):
            return self
        else:
            operand_res = OperandFactory.create_operand(rtl_expr_eval)
            if operand_res is None:
                return self
            else:
                return operand_res