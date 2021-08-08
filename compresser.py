with open('original.txt') as original:
    lines = original.read()

no_break_lines = lines.replace("\n", "0x")

compressed_spaces = no_break_lines.replace(" ", "1x")

compressing_com = compressed_spaces.replace("com", "2x")

compressing_as = compressing_com.replace("as", "3x")

new_text = open('comprimido.txt', 'w')
new_text.write(compressing_as)
new_text.close()

decodifer = open('comprimido.txt', 'a')
decodifer.write("\n{'\\n':'0x', ' ':'1x', 'com': '2x', 'as': '3x'}")

