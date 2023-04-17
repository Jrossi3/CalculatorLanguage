import re
import sys

final = {}
counter = 0

class Parser:
    def __init__(self):
        self.variables = {}

    def parse(self, statement):
        global counter
        boolList = []
        i = 0
        while i == 0:
            if not isinstance(statement, (str, bytes)):
                statement = str(statement)
            if re.match(r"print\s+.*.*", statement):
                line = statement
                if "&&" in line and line.startswith("print"):
                    line = line.replace("print", "").replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                boolList.append("1")
                            else:
                                boolList.append("0")
                    final[counter] = " ".join(boolList)
                    counter = counter + 1
                elif "||" in line and line.startswith("print"):
                    line = line.replace("print", "").replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                boolList.append("1")
                            else:
                                boolList.append("0")
                    final[counter] = " ".join(boolList)
                    counter = counter + 1
                elif "!" in line and line.startswith("print"):
                    line = line.replace("print", "").replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                boolList.append("0")
                            else:
                                boolList.append("1")
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                boolList.append("1")
                            else:
                                boolList.append("0")
                    final[counter] = " ".join(boolList)
                    counter = counter + 1
                elif re.match(r"^print\s*\(?[-%+*/(),0-9\s^]+\)?$",statement):
                    parsed_expression = statement.replace("print", "").strip()
                    parsed_expression = parsed_expression.split(",")
                    result = []
                    while parsed_expression:
                        result.append(str(helper(parsed_expression[0].strip())))
                        parsed_expression.pop(0)
                        counter = counter + 1
                    final[counter]=(" ".join(result))
                else:
                    parsed_expression = statement.replace("print", "").strip()
                    if "++" in parsed_expression:
                        if parsed_expression[0:2] == "++":
                            parsed_expression = parsed_expression.replace("++", "")
                            self.variables[parsed_expression] = self.variables[parsed_expression] + 1
                            final[counter] = float(self.variables[parsed_expression] + 1)
                        else:
                            parsed_expression = parsed_expression.replace("++", "")
                            self.variables[parsed_expression] = self.variables[parsed_expression] + 1
                            final[counter] = float(self.variables[parsed_expression] - 1)
                    elif "--" in parsed_expression:
                        if parsed_expression[0:2] == "--":
                            parsed_expression = parsed_expression.replace("--", "")
                            self.variables[parsed_expression] = self.variables[parsed_expression] - 1
                            final[counter] = float(self.variables[parsed_expression])
                        else:
                            parsed_expression = expression.replace("--", "")
                            self.variables[parsed_expression] = self.variables[parsed_expression] - 1
                            final[counter] = float(self.variables[parsed_expression] + 1)
                    else:
                        expressions = re.findall(r"\w+|[-+*/%^()]|\d+\.\d+|\d+", statement[5:])
                        final[counter] = [self._evaluate(expression) for expression in expressions]
                    counter = counter + 1
            elif re.match(r"^\s*\(?[-+%*/(),0-9\s^]+\)?$",statement):
                parsed_expression = statement.strip().split(",")
                if len(parsed_expression[0]) == 1:
                    expressions = re.findall(r"\w+|[-+*/%^()]|\d+\.\d+|\d+", statement[5:])
                    final[counter]=(str([self._evaluate(expression) for expression in expressions][0]))
                    counter = counter + 1
                else:
                    result = []
                    while parsed_expression:
                        result.append(str(helper(parsed_expression[0])))
                        parsed_expression.pop(0)
                        final[counter]=(" ".join(result))
                        result.pop()
                        counter = counter + 1
            elif re.match(r"\w+\s*[-+*/%^]=\s*[^=]+", statement):
                var_name, op, expression = re.findall(r"(\w+)\s*([-+*/%^])=\s*([^=]+)", statement)[0]
                if var_name not in self.variables:
                    raise Exception(f"Undefined variable: {var_name}")
                if op == "+":
                    self.variables[var_name] += self._evaluate(expression)
                elif op == "-":
                    self.variables[var_name] -= self._evaluate(expression)
                elif op == "*":
                    self.variables[var_name] *= self._evaluate(expression)
                elif op == "/":
                    self.variables[var_name] /= self._evaluate(expression)
                elif op == "%":
                    self.variables[var_name] %= self._evaluate(expression)
                elif op == "^":
                    value = self._evaluate(expression)
                    if isinstance(self.variables[var_name], int) and isinstance(value, int):
                        self.variables[var_name] **= value
                    elif isinstance(self.variables[var_name], float) or isinstance(value, float):
                        self.variables[var_name] = int(self.variables[var_name]) ** int(value)
                    else:
                        raise TypeError("Unsupported operand type(s) for ^=: '{}' and '{}'".format(
                        type(self.variables[var_name]), type(value)))

            # Parse variable assignment statements
            elif re.match(r"\w+\s*=\s*[^=]+", statement):
                var_name, expression = statement.split("=", maxsplit=1)
                var_name = var_name.strip()
                expression = expression.strip()
                line = statement.split("=")[1]

                if "++" in expression:
                    if expression[0:2] == "++":
                        parsed_expression = expression.replace("++", "")
                        self.variables[var_name] = self.variables[parsed_expression] + 1
                        self.variables[parsed_expression] = self.variables[parsed_expression] + 1
                        final[counter] = float(self.variables[parsed_expression])
                    else:
                        parsed_expression = expression.replace("++", "")
                        self.variables[var_name] = self.variables[parsed_expression]
                        self.variables[parsed_expression] = self.variables[parsed_expression] + 1
                        final[counter] = float(self.variables[var_name])
                elif "--" in expression:
                    if expression[0:2] == "--":
                        parsed_expression = expression.replace("--", "")
                        self.variables[var_name] = self.variables[parsed_expression] - 1
                        self.variables[parsed_expression] = self.variables[parsed_expression] - 1
                        final[counter] = float(self.variables[parsed_expression])
                    else:
                        parsed_expression = expression.replace("--", "")
                        self.variables[var_name] = self.variables[parsed_expression]
                        self.variables[parsed_expression] = self.variables[parsed_expression] - 1
                        final[counter] = float(self.variables[var_name])
                elif "&&" in line:
                    line = line.replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                self.variables[var_name] = "1"
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                print("hi")
                                self.variables[var_name] = "1"
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                self.variables[var_name] = "1"
                            else:
                                self.variables[var_name] = "0"
                elif "||" in line:
                    line = line.replace("print", "").replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                self.variables[var_name] = "1"
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                self.variables[var_name] = "1"
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                self.variables[var_name] = "1"
                            else:
                                self.variables[var_name] = "0"
                elif "!" in line:
                    line = line.replace("print", "").replace(" ", "").split(",")
                    for i in range(len(line)):
                        if "||" in line[i]:
                            x = line[i].replace("||", " ").split(" ")
                            if int(x[0]) == 0 and int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                self.variables[var_name] = "1"
                        elif "&&" in line[i]:
                            x = line[i].replace("&&", " ").split(" ")
                            if int(x[0]) == 0 or int(x[1]) == 0:
                                self.variables[var_name] = "0"
                            else:
                                self.variables[var_name] = "1"
                        elif "!" in line[i]:
                            x = line[i].replace("!", "")
                            if int(x[0]) == 0:
                                self.variables[var_name] = "1"
                            else:
                                self.variables[var_name] = "0"
                else:
                    self.variables[var_name] = self._evaluate(expression)

            # Parse bare expressions
            else:
                print('parse error')
                exit()
            i += 1

    def _evaluate(self, expression):
        
        expression = re.sub(r"\s", "", expression)

        m1 = re.search(r"[/,*,*,-,==,^,<=,>=,>,<,!=](?![\dA-Za-z_\(])", expression)

        if m1:
            if(len(final)>1):
                exit()
            print("parse error")
            exit()

        while True:
            match = re.search(r"(\d+)\s*(==|<=|>=|!=|<|>)\s*(\d+)", expression)

            if match:
                left_operand = int(match.group(1))
                operator = match.group(2)
                right_operand = int(match.group(3))
                if operator == "==":
                    result = 1 if left_operand == right_operand else 0
                    print (result)
                elif operator == "<=":
                    result = 1 if left_operand <= right_operand else 0
                    print (result)
                elif operator == ">=":
                    result = 1 if left_operand >= right_operand else 0
                    print (result)
                elif operator == "!=":
                    result = 1 if left_operand != right_operand else 0
                    print (result)
                elif operator == "<":
                    result = 1 if left_operand < right_operand else 0
                    print (result)
                elif operator == ">":
                    result = 1 if left_operand > right_operand else 0
                    print (result)
                expression = expression[:match.start()] + str(result) + expression[match.end():]
            else:
                break
    # Replace variable names with their values
        for var_name in re.findall(r'\b\w+\b', expression):
            if var_name in self.variables:
                expression = expression.replace(var_name, str(self.variables[var_name]))
    # Evaluate expressions according to precedence rules
        while True:
            expression, parens_count = re.subn(r"\(([^()]*)\)", lambda m: str(self._evaluate(m.group(1))), expression)

        # Evaluate unary negation
            expression = re.sub(r"(?<![^\s*/%+^-])-([\w.]+)", r"(-\1)", expression)

        # Evaluate exponentiation from right to left
            while True:
                match = re.search(r"([\w.]+)\^([\w.]+)", expression)
                if not match:
                    break
                left_operand, right_operand = match.group(1), match.group(2)
                exponentiation_result = float(left_operand) ** float(right_operand)
                expression = re.sub(r"([\w.]+)\^([\w.]+)", str(exponentiation_result), expression, count=1)

        # Evaluate pre-increment and pre-decrement
            expression = re.sub(r"\+\+([\w.]+)", lambda m: f"{m.group(1)}+1", expression)
            expression = re.sub(r"--([\w.]+)", lambda m: f"{m.group(1)}-1", expression)


        # Evaluate multiplication, division, and modulus from left to right
            while True:
                
                m1 = re.search(r"[/,*+-](?![\dA-Za-z_\(])", expression)

                if m1:
                    if(len(final)>1):
                        exit()
                    print("parse error")
                    exit()

                match = re.search(r"([\w.]+)([*%/])([\w.]+)", expression)
                if not match:
                    break
                left_operand, operator, right_operand = match.group(1), match.group(2), match.group(3)
                if operator == '*':
                    operator_function = lambda x, y: x * y
                elif operator == '/':
                    if float(right_operand) == 0:
                        return print("divide by zero")
                    else:
                        operator_function = lambda x, y: x / y
                elif operator == '%':
                    operator_function = lambda x, y: x % y
                multiplication_result = operator_function(float(left_operand), float(right_operand))
                expression = re.sub(r"([\w.]+)([*%/])([\w.]+)", str(multiplication_result), expression, count=1)

        # Evaluate addition and subtraction from left to right
            while True:
                match = re.search(r"([\w.]+)([-+])([\w.]+)", expression)
                if not match:
                    break
                left_operand, operator, right_operand = match.group(1), match.group(2), match.group(3)
                if operator == '+':
                    operator_function = lambda x, y: x + y
                elif operator == '-':
                    operator_function = lambda x, y: x - y
                addition_result = operator_function(float(left_operand), float(right_operand))
                expression = re.sub(r"([\w.]+)([-+])([\w.]+)", str(addition_result), expression, count=1)

        # Evaluate post-increment and post-decrement
            expression = re.sub(r"([\w.]+)\+\+", lambda m: f"({m.group(1)}+1)", expression)
            expression = re.sub(r"([\w.]+)--", lambda m: f"({m.group(1)}-1)", expression)        

        # Evaluate unary plus
            expression = re.sub(r"\+([\w.]+)", r"\1", expression)

        # Evaluate unary minus
            expression = re.sub(r"-([\w.]+)", lambda m: f"(-{m.group(1)})", expression)

        # Evaluate assignment
        # If the expression is an assignment, store the value in the variable
            match = re.search(r"([\w.]+)=([\w.]+)", expression)
            if match:
                var_name, var_value = match.group(1), match.group(2)
                self.variables[var_name] = float(var_value)

        # If the expression is not an assignment, return the value
            else:
                return float(expression)
     
            # Stop when no more operators can be evaluated
            if parens_count == 0 and not re.search(r"[-+*/%^()]|\+\+|--", expression):
                break

    # If there are still operators left, raise an error
            if re.search(r"[-+*/%^()]|\+\+|--", expression):
                raise ValueError("Invalid expression")

    # Return the final result
        return float(expression)

def helper(expression):
    if "++" in expression:
        expression = expression.replace("++", "")
        return float(expression) + 1
    elif "--" in expression:
        expression = expression.replace("--", "")
        return float(expression) - 1
    expression  = expression.replace(" ", "")
    operand_stack = []
    operator_stack = []
    def evaluate():
        try:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operator = operator_stack.pop()
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                if operand1 is None:
                    result = 0 - operand2
                else:
                    result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand1 / operand2
            elif operator == '^':
                result = operand1 ** operand2
            elif operator == '%':
                result = operand1 % operand2
            operand_stack.append(result)
        except (IndexError, ZeroDivisionError):
            if operand2 == 0:
                items = ""
                for values in final.values():
                    if isinstance(values, list):
                        values = " ".join(map(str,values))
                    items = items + values + " "
                print(items + "divide by zero")
            else:
                print("parse error")
            exit()

    i = 0
    while i < len(expression):
        if expression[i] in set(['+', '-']):
            while operator_stack and operator_stack[-1] in set(['+', '-', '*', '/', '^']):
                evaluate()
            operator_stack.append(expression[i])
            i += 1
        elif len(operator_stack) == 0 and (expression[i] == '-' and i+1 < len(expression) and expression[i+1].isdigit()):
            j = i
            if expression[i] == '-':
                j += 1
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            operand_stack.append(float(expression[i:j]))
            i = j
        
        elif expression[i] in set(['*', '/']):
            while operator_stack and operator_stack[-1] in set(['*', '/', '^']):
                evaluate()
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == '^':
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == '%':
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operator_stack[-1] != '(':
                evaluate()
            operator_stack.pop()
            i += 1
        else:
            operand_stack.append(float(expression[i]))
            i += 1
    while operator_stack:
        evaluate()
    global counter
    counter = counter + 1
    return operand_stack[-1]

class Evaluator:
    def __init__(self, parser):
        self.parser = parser
    
    def evaluate(self, statements):
        self.parser.parse(statements)
        
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

if __name__ == '__main__':
    def start():
        global counter
        check = True
        parser = Parser()
        evaluator = Evaluator(parser)
        hello = True
        try:
            while True:
                line = input()
                line = line.strip()
                hello = False
                if line == "":
                    continue
                if "/*" in line.strip():
                    check = False
                elif "*/" in line.strip():
                    check = True
                    continue
                elif line.strip().startswith("#"):
                    continue
                if(check):
                    evaluator.evaluate(line)
        except EOFError:
            if hello:
                print("parse error")
                exit()
            if not check:
                print("parse error")
                exit()
            for values in final.values():
                if isinstance(values, list):
                    values = " ".join(map(str,values))
                print(values)
    start()