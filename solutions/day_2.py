from __future__ import annotations
from puzzle_reader import read_puzzle
from abc import ABC, abstractmethod
from itertools import pairwise

class SafetyRule(ABC):
    ''' Abstract representation of a rule which can be evaluated to determine
    if reading levels are safe. '''

    @abstractmethod
    def evaluate(self, levels: list[int]) -> bool:
        ''' Returns True if the given levels passed this rule. '''

class AscendingDescendingRule(SafetyRule):
    ''' Safe if the levels are either exclusively ascending or exclusively
    descending. '''

    def evaluate(self, levels: list[int]) -> bool:
        return self._ascending(levels) or self._descending(levels)
    
    def _ascending(self, levels: list[int]) -> bool:
        ''' True if the levels are exclusively ascending. '''
        return levels == sorted(levels)
    
    def _descending(self, levels: list[int]) -> bool:
        ''' True if the levels are exclusively descending. '''
        return levels == sorted(levels, reverse=True)
    
class SlopeRule(SafetyRule):
    ''' Safe if the levels do not rise or fall too steeply - specifically that
    the difference between adjacent levels does not fall outside of a given
    range. '''

    MIN = 1
    MAX = 3

    def evaluate(self, levels: list[int]) -> bool:
        for (n1,n2) in pairwise(levels):
            if not self.MIN <= abs(n2-n1) <= self.MAX:
                return False
            
        return True

class Report:
    ''' A report of readings from the Red-Nosed Reindeer nuclear fusion/fission
    plant. The readings can either be considered safe or unsafe depending
    on various rules. '''

    def __init__(self, levels: list[int],
                safety_rules: list[SafetyRule] = None) -> None:
        self._levels = levels
        self._safety_rules = safety_rules if safety_rules else []

    @property
    def levels(self) -> list[int]:
        ''' A list of numbers representing the readings from the nuclear
        plant. '''
        return self._levels
    
    @property
    def safety_rules(self) -> list[SafetyRule]:
        ''' A list of safety rules to be applied to the readings to determine
        if they are safe. '''
        return self._safety_rules
    
    def add_safety_rule(self, rule: SafetyRule) -> None:
        ''' Adds a SafetyRule to this report's list of rules. '''
        self.safety_rules.append(rule)

    def is_safe(self) -> bool:
        ''' Returns True only if all rules evaluate to safe. '''
        return all([rule.evaluate(self.levels) for rule in self.safety_rules])
    
    @classmethod
    def from_str(self, s: str) -> Report:
        ''' Create a Report object from the given string representation which
        looks like this:
        7 6 4 2 1
        '''
        return Report([int(num_str) for num_str in s.split()])
    
    def __repr__(self) -> str:
        return ' '.join([str(lvl) for lvl in self.levels])

def solve_part_one():
    ''' Solve part one of the puzzle. '''

    puzzle_input = read_puzzle('input.dat')

    reports = [Report.from_str(line) for line in puzzle_input.split('\n')]

    for report in reports:
        report.add_safety_rule(AscendingDescendingRule())
        report.add_safety_rule(SlopeRule())

    safe_report_count = len([report for report in reports if report.is_safe()])

    print(f'Number of safe reports: {safe_report_count}')

if __name__ == '__main__':
    solve_part_one()