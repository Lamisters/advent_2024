from puzzle_loader import read_puzzle_input

def solve_part_one():
    ''' Solve part one of the puzzle. '''

    input = read_puzzle_input('input.dat')

    left_nums = sorted([int(line.split()[0]) for line in input.split('\n')])
    right_nums = sorted([int(line.split()[1]) for line in input.split('\n')])

    # pair the minumums from each list
    pairs = zip(left_nums, right_nums)

    # compute the differences
    differences = [max(p) - min(p) for p in pairs]

    total_difference = sum(differences)

    print(f'The total difference is {total_difference}')

if __name__ == '__main__':
    solve_part_one()