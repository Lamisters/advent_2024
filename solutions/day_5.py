from __future__ import annotations
from puzzle_reader import read_puzzle

class PageUpdateVerifier:
    ''' Holds a set of rules for ordering pages during Safety Manual
    page updates. Rules can be applied to a list of pages to update
    to verify if they are being done in the correct order. '''

    def __init__(self, rules: dict[int:tuple[int,int]]):
        self._rules = rules

    @property
    def rules(self) -> dict[tuple[int,int]]:
        ''' Each rule is a tuple of integers that represent the order
        in which page updates should be made. '''
        return self._rules
    
    def verify(self, updates: list[int]) -> bool:
        ''' Verify if the given list of page numbers to update are
        in the correct order per the rules. '''
        for page_num in updates:
            try:
                for n1,n2 in self.rules[page_num]:
                    try:
                        if updates.index(n1) > updates.index(n2):
                            return False
                    except ValueError:
                        pass
            except KeyError:
                pass

        return True

    
    @classmethod
    def from_str(self, s: str) -> PageUpdateVerifier:
        ''' Create a PageUpdateVerifier object from the given string
        representation of its rules. Each line is a pipe-delimited
        list of page numbers. '''
        rules = {}
        for line in s.split('\n'):
            nums = tuple(int(num_str) for num_str in line.split('|'))
            for num in nums:
                try:
                    rules[num].append(nums)
                except KeyError:
                    rules[num] = [nums]
        return PageUpdateVerifier(rules)
    
    def __repr__(self):
        return '\n'.join([str(nums) for nums in self.rules.values()])

def middle_page_of(page_nums: list[int]) -> int:
    ''' Returns the integer in the middle of the list. If the list is
    empty or has an even number of elements, returns None. '''
    if len(page_nums) % 2 == 0:
        return None
    else:
        return page_nums[len(page_nums) // 2]

def solve_part_one():
    ''' Solve part one of the puzzle. '''
    puzzle_input = read_puzzle('input.dat')

    rule_section, updates_section = puzzle_input.split('\n\n')
    verifier = PageUpdateVerifier.from_str(rule_section)

    # sum up the middle pages of valid updates to get the puzzle answer
    middle_sum = 0
    for update_str in updates_section.split('\n'):
        page_nums = [int(num_str) for num_str in update_str.split(',')]
        if verifier.verify(page_nums):
            middle_sum += middle_page_of(page_nums)

    print(f'Sum of the middle page numbers: {middle_sum}')

if __name__ == '__main__':
    solve_part_one()