from puzzle_reader import read_puzzle
import re

class Program:
    ''' A program with corrupted memory. '''

    def __init__(self, memory: str):
        self._memory = memory
        self._instructions = self._parse_instructions(memory)

    @property
    def memory(self) -> str:
        ''' A string representing the program's memory which contains
        instructions, but may contain invalid characters as well. '''
        return self._memory
    
    @property
    def instructions(self) -> list[str]:
        ''' A list of instructions where each instruction looks like this:
            mul(x,y)
        And where x and y are both integers between 0-999. '''
        return self._instructions
    
    def _parse_instructions(self, memory: str) -> list[str]:
        ''' Return a list of valid instructions parsed from the given
        string. '''
        instr_pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
        return re.findall(instr_pattern, memory)
    
    def execute_all(self) -> list[int]:
        ''' Executes the program's instructions and returns a list of
        integers which represent the instructions' output. '''
        return [self.execute(instr) for instr in self.instructions]

    def execute(self, instruction: str) -> int:
        ''' Execute the given instruction. An instruction is a string in this
        form: mul(x,y) where x,y are integers between 0-999. Executing the
        instruction returns the product of both integers.'''
        pattern = '[0-9]{1,3}'
        x,y = (int(num_str) for num_str in re.findall(pattern, instruction))
        return x * y


def solve_part_one():
    ''' Solve part one of the puzzle. '''

    puzzle_input = read_puzzle('input.dat')

    program = Program(puzzle_input)

    results = program.execute_all()

    print(f'The sum of the results is: {sum(results)}')

if __name__ == '__main__':
    solve_part_one()