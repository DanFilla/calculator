def parse_exp(exp):
    def add(operand1, operand2):
        return str(float(operand1) + float(operand2))

    def sub(operand1, operand2):
        return str(float(operand1) - float(operand2))

    def mult(operand1, operand2):
        return str(float(operand1) * float(operand2))

    def div(operand1, operand2):
        return str(float(operand1) / float(operand2))

    while 1:
        for num in range(len(exp)):
            #Loop to find mult and div
            if exp[num] == "*":
                exp = exp[:num-1] + [mult(exp[num-1], exp[num+1])] + exp[num+2:]
                break
            elif exp[num] == "/":
                exp = exp[:num-1] + [div(exp[num-1], exp[num+1])] + exp[num+2:]
                break
        else:
            break

    while 1:
        for num in range(len(exp)):
            #Loop to find mult and div
            if exp[num] == "+":
                exp = exp[:num-1] + [add(exp[num-1], exp[num+1])] + exp[num+2:]
                break
            elif exp[num] == "-":
                exp = exp[:num-1] + [sub(exp[num-1], exp[num+1])] + exp[num+2:]
                break
        else:
            break

    return str(exp[0])

def evaluate_expression(exp):
    while 1:
        if "(" not in exp or ")" not in exp:
            #Evaluate current paren
            return parse_exp(exp)

        else:
            #Continue with recursion
            start_paren = -1
            end_paren = -1
            for num in range(len(exp)):
                if exp[num] == "(" and start_paren == -1:
                    start_paren = num
                    break

            paren_count = 0
            for num in range(start_paren+1, len(exp)):
                if exp[num] == "(":
                    paren_count += 1
                elif exp[num] == ")":
                    paren_count -= 1
                if paren_count < 0:
                    end_paren = num
                    break

            exp = exp[:start_paren] + [evaluate_expression(exp[start_paren+1:end_paren])] + exp[end_paren+1:]

def calculate(exp):
    formated_string = exp.split()
    return evaluate_expression(formated_string)

sample = "3 / ( 2 + 1234 ) * ( 1 + ( 23 / 24 ) + ( 13 * 191 ) ) + 165"
print(calculate(sample))
