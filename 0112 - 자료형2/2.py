morse_code = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__',
              'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..'}


def print_morse(s):
    result = ''
    s = s.upper()

    for char in s:
        if char == ' ':
            continue
        result += morse_code[char]

    return result


print(print_morse('hello python'))
