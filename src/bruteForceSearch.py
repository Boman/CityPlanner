class BruteForceSearch():
    def __init__(self, availableTiles, board, updateFunction):
        self.availableTiles = availableTiles.values()
        self.board = board
        self.updateFunction = updateFunction
        self.searchList = [{'xPos': -1, 'yPos': 0, 'tiles': []}]
        self.resultList = []

    def start(self):
        while len(self.searchList) > 0:
            searchItem = self.searchList.pop()
            for tile in self.availableTiles:
                nextPosition = self.findNextPosition(searchItem, tile)
                # print(f'Started search for {searchItem} found: {nextPosition}')
                if nextPosition != None:
                    xPos, yPos = nextPosition
                    tileToAdd = {'xPos': xPos, 'yPos': yPos, 'tile': tile}
                    # print(f'Add tile {tile} at position: {nextPosition}')
                    self.searchList.append({'xPos': xPos, 'yPos': yPos, 'tiles': searchItem['tiles'] + [tileToAdd]})
                else:
                    result = self.getResult(searchItem)
                    if not self.resultList or result['score'] > self.resultList[-1]['score']:
                        print(f'found new result: {result}')
                        self.resultList.append(result)
                        self.updateFunction(result)
        print("finished")

    def findNextPosition(self, searchItem, tile):
        xPos, yPos, tiles = searchItem['xPos'], searchItem['yPos'], searchItem['tiles']
        while yPos < len(self.board):
            xPos += 1
            if self.isLeftFromBoard(xPos, yPos):
                continue
            if self.isRightFromBoard(xPos, yPos):
                yPos += 1
                xPos = -1
                continue
            if not self.tileFitsBoard(xPos, yPos, tile):
                continue
            if self.tileInterleaveTiles(xPos, yPos, tile, tiles):
                continue
            return xPos, yPos
        return None

    def isLeftFromBoard(self, xPos, yPos):
        return xPos < self.board[yPos]['left']

    def isRightFromBoard(self, xPos, yPos):
        return xPos >= self.board[yPos]['river']

    def tileFitsBoard(self, xPos, yPos, tile):
        if yPos + len(tile) > len(self.board):
            return False
        for y, tileLine in enumerate(tile):
            if self.isLeftFromBoard(xPos + tileLine.index(1), yPos + y):
                return False
            if self.isRightFromBoard(xPos + len(tileLine) - tileLine[::-1].index(1) - 1, yPos + y):
                return False
        return True

    def tileInterleaveTiles(self, xPos, yPos, tile, tiles):
        for tile2 in tiles:
            if self.tilesInterleave(tile2['xPos'] - xPos, tile2['yPos'] - yPos, tile, tile2['tile']):
                return True
        return False

    def tilesInterleave(self, xDelta, yDelta, tile1, tile2):
        for y, tile1Line in enumerate(tile1):
            if 0 <= y - yDelta < len(tile2):
                for x, tile1Entry in enumerate(tile1Line):
                    if 0 <= x - xDelta < len(tile2[y - yDelta]):
                        if tile1Entry == 1 and tile2[y - yDelta][x - xDelta] == 1:
                            return True
        return False

    def getResult(self, searchItem):
        print(f'searchItem = {searchItem}')
        score = 0
        for y in range(len(self.board)):
            for x in range(self.board[y]['left'], self.board[y]['river']):
                if not self.tileInterleaveTiles(y, x, [[1]], searchItem['tiles']):
                    if x in self.board[y]['tree']:
                        print('found tree')
                        score += 2
                    elif x in self.board[y]['stone']:
                        print('found stone')
                        score -= 2
                    elif x not in self.board[y]['gold'] and x not in self.board[y]['well']:
                        print('found empty field')
                        score -= 1
                print(f'{x}, {y} = {score}')
        return {'score': score, 'tiles': searchItem['tiles']}
