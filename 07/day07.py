import numpy as np
import sys

wires = {}

def int_or_key(name,dic_name):
    try:
        int(name)
        return name
    except ValueError:
        return f"{dic_name}['{name}']"

def decode_instruction(string, dic_name):
    if "AND" in string:
        names = [int_or_key(name,dic_name) for name in string.split(" AND ")]
        return f"{names[0]} & {names[1]}"
    elif "OR" in string:
        names = [int_or_key(name,dic_name) for name in string.split(" OR ")]
        return f"{names[0]} | {names[1]}"
    elif "LSHIFT" in string:
        names = [int_or_key(name,dic_name) for name in string.split(" LSHIFT ")]
        return f"{names[0]} << {names[1]}"
    elif "RSHIFT" in string:
        names = [int_or_key(name,dic_name) for name in string.split(" RSHIFT ")]
        return f"{names[0]} >> {names[1]}"
    elif "NOT" in string:
        name = int_or_key(string.replace("NOT ",""),dic_name)
        return f"~{name} + 65536"
    else:
        return int_or_key(string,dic_name)

with open("input.txt","r") as file:
    instructions = np.array(file.read().splitlines())
    
part_two = True
if part_two:
    for i,instruction in enumerate(instructions):
        if instruction.endswith("-> b"):
            instructions[i] = "46065 -> b"

old_kept = np.inf
while True:
    kept = []
    for i,string in enumerate(instructions):
        instruction, var_name = string.split(" -> ")
        cmd = f"wires['{var_name}'] = {decode_instruction(instruction, 'wires')}"
        try:
            exec(cmd)
        except KeyError as e:
            kept.append(i)
    if kept:
        print(f"{len(kept)} instructions remaining")
        if old_kept == len(kept):
            print("STUCK")
            break
        old_kept = len(kept)
        instructions = instructions[kept]
    else:
        break