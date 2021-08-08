import ast

with open('comprimido.txt') as original_instructions:
    instructions = original_instructions.readlines()

instructions_dict = ast.literal_eval(instructions[1])
original_instructions.close()

with open('comprimido.txt') as original:
    compressed = original.readline()

for key in instructions_dict:
    compressed = compressed.replace(instructions_dict[key], key)

new_text = open('descomprimido.txt', 'w')
new_text.write(compressed)
