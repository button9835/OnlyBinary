def run_onlybinary(binary_code: str):
    for ch in binary_code:
        if ch not in ('0', '1'):
            raise ValueError(f"Invalid character '{ch}' in binary code. Only 0 and 1 are allowed.")
    
    if len(binary_code) % 8 != 0:
        raise ValueError("Binary code length must be a multiple of 8.")
    
    stack = []
    i = 0
    in_string = False
    string_buffer = ''
    loop_stack = []
    
    instructions = []

    while i + 8 <= len(binary_code):
        byte = binary_code[i:i+8]
        instructions.append(chr(int(byte, 2)))
        i += 8

    ip = 0
    while ip < len(instructions):
        char = instructions[ip]

        if char == '"':
            in_string = not in_string
            if not in_string:
                for ch in string_buffer:
                    stack.append(ord(ch))
                string_buffer = ''
        elif in_string:
            string_buffer += char

        elif char.isdigit():
            stack.append(int(char))
        elif char == '+':
            if len(stack) < 2:
                print("Error: Stack underflow for '+'")
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
        elif char == '-':
            if len(stack) < 2:
                print("Error: Stack underflow for '-'")
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
        elif char == '*':
            if len(stack) < 2:
                print("Error: Stack underflow for '*'")
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
        elif char == '/':
            if len(stack) < 2:
                print("Error: Stack underflow for '/'")
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(a // b if b != 0 else 0)
        elif char == 'p':
            if not stack:
                print("Error: Stack empty for 'p'")
            else:
                print(stack[-1])
        elif char == 'c':
            while stack:
                print(chr(stack.pop(0) % 256), end='')
            print()
        elif char == 'r':
            if not stack:
                print("Error: Stack empty for 'r'")
            else:
                stack.pop()
        elif char == 'i':
            user_input = input("Input : ")
            if user_input:
                stack.append(ord(user_input[0]))
        elif char == '?':
            if not stack:
                print("Error: Stack empty for '?'")
                ip += 1
            elif stack[-1] == 0:
                ip += 1
        elif char == '[':
            loop_stack.append(ip)
        elif char == ']':
            if not stack:
                print("Error: Stack empty for ']'")
            elif stack[-1] != 0:
                ip = loop_stack[-1]
                continue
            else:
                loop_stack.pop()
        else:
            pass

        ip += 1
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python onlybinary.py <file.ob>")
        exit(1)

    with open(sys.argv[1], "r") as f:
        code = f.read().replace("\n", "").replace(" ", "")

    try:
        run_onlybinary(code)
    except ValueError as e:
        print(f"Error: {e}")
