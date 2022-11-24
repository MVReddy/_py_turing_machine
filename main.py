"""
Turing Impmentation in Python.
@Author: Venkata Mulam
@Date: Nove 24 2022
"""

class TuringMachine:
    """
    initialize the Turing Machine, read the program and input
    """

    def __init__(self, program, input, N, state=0):
        self.trf = {}
        self.state = str(state)
        self.tape = ''.join(['_'] * N)
        self.head = N // 2  # head is positioned in the middle
        self.tape = self.tape[:self.head] + input + self.tape[self.head:]
        for line in program:
            s, a, r, d, s1 = list(line)
            self.trf[s, a] = (r, d, s1)

    def step(self):
        if self.state != 'H':
            # assert self.head >= 0 and self.head < len(self.tape) here
            a = self.tape[self.head]
            action = self.trf.get((self.state, a))
            if action:
                r, d, s1 = action
                self.tape = self.tape[:self.head] + r + self.tape[self.head + 1:]
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                self.state = s1
                print(self.state + ": " + self.tape.replace('_', '') )

    def run(self, max_iter=9999):
        i = 0
        while self.state != 'H' and i < max_iter:  # prevent infinite loop
            self.step()
            i += 1
        print(self.tape, self.state)


if __name__ == "__main__":
    print("Reading TM.txt...")
    program = open('TM.txt').read().splitlines()
    N = int(program[0])
    S = program[1]
    program = program[2:]
    initial_input = input("Enter the starting tape with one leading and one trailing blank (_): ")
    print("Processing...")
    tm = TuringMachine(program, initial_input, N)
    tm.run()
