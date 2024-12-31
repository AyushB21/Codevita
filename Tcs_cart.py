def evaluate_gate(logic_type, input1, input2):
    if logic_type == "AND":
        return input1 & input2
    elif logic_type == "OR":
        return input1 | input2
    elif logic_type == "NAND":
        return ~(input1 & input2) & 1
    elif logic_type == "NOR":
        return ~(input1 | input2) & 1
    elif logic_type == "XOR":
        return input1 ^ input2
    else:
        raise ValueError("Invalid logic type")

def compute_result(num_gates, logic_definitions, num_cycles, input_signals, target_output):
    outputs = {gate: [0] * num_cycles for gate in logic_definitions.keys()}
    variables = {var: values for var, values in input_signals.items()}
    for cycle in range(1, num_cycles):
        for gate, (logic_type, inputs) in logic_definitions.items():
            in1 = variables[inputs[0]][cycle - 1] if inputs[0] in variables else outputs[inputs[0]][cycle - 1]
            in2 = variables[inputs[1]][cycle - 1] if inputs[1] in variables else outputs[inputs[1]][cycle - 1]
            outputs[gate][cycle] = evaluate_gate(logic_type, in1, in2)
    return outputs[target_output]

num_gates = int(input())
logic_definitions = {}
for _ in range(num_gates):
    definition = input().strip()
    gate, expr = definition.split("=")
    logic, inputs = expr.split("(")
    inputs = inputs[:-1].split(",")
    logic_definitions[gate] = (logic, inputs)

num_cycles = int(input())
input_signals = {}
for _ in range(num_cycles-1):
    data = input().split()
    var = data[0]
    values = list(map(int, data[1:]))
    input_signals[var] = values

target_output = input().strip()
result = compute_result(num_gates, logic_definitions, num_cycles, input_signals, target_output)
print(" ".join(map(str, result)))
