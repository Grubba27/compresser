import ast

with open('comprimido.txt') as original_instructions:
    instructions = original_instructions.readlines()

instructions_dict = ast.literal_eval(instructions[1])
original_instructions.close()

with open('comprimido.txt') as original:
    compressed = original.readline()

no_break_lines = compressed.replace("0x", "\n")

descompressed_spaces = no_break_lines.replace("1x", " ")

descompressing_com = descompressed_spaces.replace("2x", "com")

descompressing_as = descompressing_com.replace("3x", "as")

new_text = open('descomprimido.txt', 'w')
new_text.write(descompressing_as)
