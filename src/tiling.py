from operator import itemgetter
from src.gameSettings import board, tiles


def generateBoard(boardDescription):
    width = max(boardDescription, key=itemgetter('right'))['right']
    height = len(boardDescription)

    def generateLine(line):
        def generatePosition(x):
            if x < line['left'] or x >= line['right']:
                return 0
            if x + 1 in line['stone']:
                return 2
            if x + 1 in line['tree']:
                return 3
            if x + 1 in line['gold']:
                return 4
            if x + 1 in line['well']:
                return 5
            return 1

        return [generatePosition(x) for x in range(width)]

    board = [generateLine(line) for line in boardDescription]
    return {'width': width, 'height': height, 'board': board}


def rotateTile(tile):
    width = len(tile[0])
    height = len(tile)
    return [[tile[x][width - y - 1] for x in range(height)] for y in range(width)]


def testCrossingRiver(tile):
    def river(x, y):
        return board[y]['river']

    riverSide = board[tile['y']]['river']


def testTileCollision(tile1, tile2):
    pass


def testBoardCollision(tile):
    pass


if __name__ == '__main__':
    print(generateBoard(board))
    print(rotateTile(tiles['b']))
