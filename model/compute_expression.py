# S-expressions calculator
# Adan J. Suarez

class Compute_Expression(object):
    def __init__(self, expr):
        self.expr = expr
        self.count = self.expr.count("(")
        self.pointer = 1

    def get_value(self):
        if self.count == 0:
            return int(self.expr)
        if self.count != 0:
            return self.calc_expression(self.expr)
    
    def set_pointer(self, pointer):
        self.pointer = pointer

    def calc_expression(self, expr):
        count = expr.count("(")
        if count == 0:
            return int(expr.replace(")", ""))
        if count != 0:
            return self.calc_complex_expression(expr)
    
    def calc_complex_expression(self, expr):
        function, sub_expr1, sub_expr2 = "", "", ""
        function = self.extract_function(expr)            
        sub_expr1 = self.extract_expression(expr)
        sub_expr2 = self.extract_expression(expr)
        if function == "add":
            return self.calc_expression(sub_expr1) + self.calc_expression(sub_expr2)
        elif function == "multiply":
            return self.calc_expression(sub_expr1) * self.calc_expression(sub_expr2)
        else: 
            raise Exception('### Error in function ###')

    def extract_function(self, expr):
        function = ""
        self.set_pointer(1)
        for char in expr[1:]:
            self.pointer += 1
            if char == " ":
                break
            function = function + char
        return function

    def extract_expression(self, expr):
        counter = 0
        result = ""
        new_expr = expr[self.pointer:]
        first_char = new_expr[0]
        for char in new_expr:
            self.pointer += 1
            if first_char != "(":
                if char == " ":
                    break
                result = result + char
            elif char == "(":
                counter += 1
                result = result + char
            elif char == ")":
                counter -= 1
                result = result + char
                if counter == 0:
                    self.pointer += 1
                    break
            elif char != "(" and ")":
                result = result + char
        return result
