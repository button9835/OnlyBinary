# OnlyBinary

**OnlyBinary** is a stack-based, esoteric programming language where the entire source code consists only of binary digits (`0` and `1`). Each instruction is exactly **1 byte (8 bits)** and is interpreted as an ASCII character command.

---

## 🔧 How It Works

- **Source Code**: Only contains binary (`0` and `1`). No other characters are allowed.
- **Instruction Size**: Each instruction is exactly 8 bits (1 byte), representing an ASCII character.
- **Execution**: A stack is used for computation and control flow.
- **String Literals**: Enclosed in double quotes (`"`). You can push entire strings at once.

---

## 📁 .ob File Format

- `.ob` files contain nothing but a stream of `0` and `1` characters.
- Line breaks and whitespace are ignored.
- The binary stream is split into chunks of 8 bits.
- Each chunk is interpreted as one instruction using its ASCII code.

---

## 📜 Example

Example code is in example.ob file. 
- File represents: "Hello, World!"c

---

## 💡 Instruction Set

| Command | Description                                               |
| ------- | --------------------------------------------------------- |
| `0-9`   | Push the digit onto the stack as a number                 |
| `+`     | Add top two values of the stack                           |
| `-`     | Subtract top two values (`a - b`)                         |
| `*`     | Multiply top two values                                   |
| `/`     | Integer divide top two values (`a // b`)                  |
| `p`     | Print top of the stack as number                          |
| `c`     | Print entire stack as characters                          |
| `r`     | Pop (remove) top value of the stack                       |
| `i`     | Input one character, push ASCII to stack                  |
| `"`     | Toggle string mode. Text inside is pushed as ASCII values |
| `[`     | Begin a loop. While top of stack ≠ 0                      |
| `]`     | End of loop. Jump back to matching `[`                    |
| `?`     | If top of stack == 0, skip next instruction               |

---
## ⚠️ Error Handling

OnlyBinary throws runtime errors in the following cases:

- **Invalid characters**: If the code contains any characters other than `0` and `1`, an error will be raised.

   Error: Invalid character 'X' in binary code. Only 0 and 1 are allowed.

- **Non-multiple of 8**: Since the interpreter reads 1-byte (8-bit) chunks, the total length of the binary code must be a multiple of 8.

   Error: Binary code length must be a multiple of 8.

- **Stack underflow**: Trying to pop from an empty stack or accessing nonexistent values will raise an error.

   Error: Cannot pop from an empty stack.

- **Mismatched loops**: If `[` or `]` instructions are unmatched, a syntax error will be thrown.

   Error: Unmatched '[' at instruction 10.

- **Unknown command**: If an unknown ASCII instruction is interpreted, the program will raise an error.

   Error: Unknown command 'x'.

---

# This Language made by ChatGPT
