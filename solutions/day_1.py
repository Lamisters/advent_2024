from puzzle_reader import read_puzzle

def solve_part_one():
    ''' Solve part one of the puzzle. '''

    input = read_puzzle('input.dat')

    left_nums = sorted([int(line.split()[0]) for line in input.split('\n')])
    right_nums = sorted([int(line.split()[1]) for line in input.split('\n')])

    # pair the minumums from each list
    pairs = zip(left_nums, right_nums)

    # compute the differences
    differences = [max(p) - min(p) for p in pairs]

    total_difference = sum(differences)

    print(f'The total difference is {total_difference}')

def solve_part_two():
    ''' Solve part two of the puzzle. '''

    input = read_puzzle('input.dat')

    left_nums = sorted([int(line.split()[0]) for line in input.split('\n')])
    right_nums = sorted([int(line.split()[1]) for line in input.split('\n')])

    similarity_score = 0
    for n in left_nums:
        similarity_score += n * right_nums.count(n)

    print(f'The similarity score is: {similarity_score}')

if __name__ == '__main__':
    solve_part_two()