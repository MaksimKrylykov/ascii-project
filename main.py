import sys

FIRST_SYMBOL = ' '
LAST_SYMBOL = '~'
CHAR_HEIGHT = 8


def fix_str(string):
    fixed_str = ""
    i = 0
    while i < len(string):
        if i + 1 < len(string) and string[i] == '\\' and string[i + 1] == 'n':
            fixed_str += '\n'
            i += 2
            continue
        
        fixed_str += input_text[i]
        i += 1
    return fixed_str


def ascii_art(text, banner = "standard"):
    try:
        banner_file = open(f"./banners/{banner}.txt")
    except:
        banner_file = open("./banners/standard.txt")
        
    lines = banner_file.readlines()
    
    ascii_map = dict()
    current_line = 1
    for i in range(ord(FIRST_SYMBOL), ord(LAST_SYMBOL) + 1):
        art = [lines[i][:-1] for i in range(current_line, current_line + CHAR_HEIGHT)]
        
        ascii_map[chr(i)] = art
        
        current_line += CHAR_HEIGHT + 1

    matrix_art = []
    current_line = 0

    for char in text:
        if char == '\n':
            current_line = len(matrix_art)
            matrix_art.append('')
            continue

        if not ascii_map.get(char):
            continue

        while len(matrix_art) < current_line + CHAR_HEIGHT:
            matrix_art.append('')

        for i in range(current_line, current_line + CHAR_HEIGHT):
            matrix_art[i] += ascii_map[char][i - current_line]

    final_art = ''

    for i in range(len(matrix_art)):
        final_art += matrix_art[i]
        final_art += '\n'

    return final_art


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        input_text = sys.argv[1].strip()

        try:
            banner = sys.argv[2].strip()
        except:
            banner = "standard"

        fixed_text = fix_str(input_text)
        
        print(ascii_art(fixed_text, banner), end='')
        
    else:
        print("Usage: python3 main.py [STRING] [BANNER]")
        print()
        print("EX: python3 main.py something standard")
    
