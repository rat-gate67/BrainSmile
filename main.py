import sys
import table
from convert import conv2fuck, conv2smile

TABLE = table.TABLE

class BrainSmile:
    def __init__(self):
        self.mem = [0] * 30000
        self.index = 0
        self.code = ""
        self.commands = TABLE

    def GT(self):
        if self.index < len(self.mem) - 1:
            self.index += 1
    
    def LT(self):
        if self.index > 0:
            self.index -= 1
        else:
            print("under flow")

    def PLUS(self):
        self.mem[self.index] += 1

    def MINUS(self):
        self.mem[self.index] -= 1

    def DOT(self):
        print(chr(self.mem[self.index]), end="")

    def COMMA(self):
        self.mem[self.index] = ord(input(""))

    def LBRACKET(self):
        if self.mem[self.index] == 0:
            count = 1
            while count != 0:
                if self.index < len(self.mem) - 1:
                    self.index += 1
                self.index += 1
                if self.mem[self.index] == 91:
                    count += 1
                elif self.mem[self.index] == 93:
                    count -= 1

    def RBRACKET(self):
        if self.mem[self.index] != 0:
            count = 1
            while count != 0:
                if self.index > 0:
                    self.index -= 1
                self.index -= 1
                if self.mem[self.index] == 91:
                    count -= 1
                elif self.mem[self.index] == 93:
                    count += 1
    
    def set_code(self, code):
        self.code = code

    def read_code(self, filename):
        with open(filename, "r") as f:
            self.code = f.read()

    def execute(self):
        for ch in self.code:
            if ch == " " or ch == "\n":
                continue

            c = self.commands[ch]
            
            if c == ">":
                self.GT()
            elif c == "<":
                self.LT()
            elif c == "+":
                self.PLUS()
            elif c == "-":
                self.MINUS()
            elif c == ".":
                self.DOT()
            elif c == ",":
                self.COMMA()
            elif c == "[":
                self.LBRACKET()
            elif c == "]":
                self.RBRACKET()
            else:
                pass


def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    bs = BrainSmile()
    bs.read_code(sys.argv[1])
    bs.execute()

if __name__ == "__main__":
    main()