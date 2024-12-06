from puzzle_reader import read_puzzle

class WordGrid:
    ''' The word search puzzle as represented by a grid. Each letter can
    be accessed by an (x,y) co-ordinate. '''

    def __init__(self, rows: list[str]):
        self._rows = rows

    @property
    def rows(self) -> list[str]:
        ''' A list of strings where each string is one line of the word
        search grid. '''
        return self._rows
    
    def char_at(self, pos: tuple[int,int]) -> str:
        ''' The character at the given (x,y) position in the word search
        grid. Returns None if the given position is outside the grid. '''
        x,y = pos
        try:
            if x < 0 or y < 0:
                raise IndexError
            return self.rows[y][x]
        except IndexError:
            return None
        
    def count_matches_from(self, pos: tuple[int,int], target_word: str) -> int:
        ''' Returns the count of matches for the given word starting at the
        given (x,y) position. A match can happen forwards/backwards in any
        direction including diagonal. '''
        # orthogonal/diagonal directions as represented by deltas in (x,y)
        xy_deltas = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

        x,y = pos
        matches_found = 0
        for dx,dy in xy_deltas:

            # every (x,y) position in this direction, for the length of the
            # given word that we are looking for
            positions = []
            for i in range(0, len(target_word)):
                positions.append((x + dx*i, y + dy*i))

            word_here = ''.join([self.char_at((x,y)) for x,y in positions
                                 if self.char_at((x,y)) is not None])
            
            if word_here == target_word:
                matches_found += 1

        return matches_found

    def count_all_matches(self, word: str) -> int:
        ''' Return the number of matches found for the given word across
        the entire puzzle. A match can be forward/backward in any direction
        including diagonals. '''

        total_matches = 0

        # check for matches from any position in the puzzle grid where that
        # character is the first letter of the target word
        first_letter = word[0]
        for y,row in enumerate(self.rows):
            for x,char in enumerate(row):
                if char == first_letter:
                    total_matches += self.count_matches_from((x,y), word)

        return total_matches

    def __repr__(self):
        return '\n'.join(self.rows)
    
def solve_part_one():
    ''' Solve part one of the puzzle. '''

    puzzle_input = read_puzzle('input.dat')

    grid = WordGrid([line for line in puzzle_input.split('\n')])

    word = 'XMAS'

    match_count = grid.count_all_matches(word)

    print(f'Total matches found for {word}: {match_count}')

if __name__ == '__main__':
    solve_part_one()