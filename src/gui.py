import remi.gui as gui
from time import time


class BoardGui(gui.Container):

    def __init__(self, **kwargs):
        super(BoardGui, self).__init__(**kwargs)
        self.container = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_VERTICAL, margin='0px',
                                       style={'display': 'block', 'overflow': 'auto'})

        self.boardWidth = 1242 - 280 - 157
        self.boardHeight = 1422 - 160 - 460
        self.boardContainer = gui.Container(style={
            'width': str(self.boardWidth) + 'px',
            'height': str(self.boardHeight) + 'px',
            'overflow': 'hidden'})
        self.board = gui.Container(style={
            'position': 'absolute',
            'top': '-160px',
            'left': '-157px',
            'height': '1422px',
            'width': '1242px',
            'clip-path': 'inset(160px 280px 460px 160px)',
            'background-image': 'url(/my_resources:board.jpg)',
            'background-size': 'cover',
            'overflow': 'hidden'})
        self.boardContainer.append(self.board)
        self.append(self.boardContainer)
        self.tileContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_VERTICAL, margin='0px',
                                           style={'display': 'block', 'overflow': 'auto'})
        self.append(self.tileContainer)

    def displayTiles(self, tiles):
        self.removeTiles()
        svg = gui.Svg(style={
            'position': 'absolute',
            'width': str(self.boardWidth) + 'px',
            'height': str(self.boardHeight) + 'px',
            'top': '10px',
            'left': '10px'})
        for tile in tiles:
            self.addTile(svg, tile['tile'], tile['xPos'], tile['yPos'])
        self.tileContainer.append(svg)

    def addTile(self, svg, tile, xPos, yPos):
        width = len(tile[0])
        height = len(tile)
        if len(tile) == 1 and len(tile[0]) == 1:
            self.addRect(svg, xPos, yPos, 1, 0)
            return
        for x in range(width):
            for y in range(height):
                if tile[y][x]:
                    if x < width - 1 and y < height - 1 and tile[y][x + 1] and tile[y + 1][x] and tile[y + 1][x + 1]:
                        self.addRect(svg, x + xPos, y + yPos, 1, 1)
                    if x < width - 1 and tile[y][x + 1]:
                        self.addRect(svg, x + xPos, y + yPos, 1, 0)
                    if y < height - 1 and tile[y + 1][x]:
                        self.addRect(svg, x + xPos, y + yPos, 0, 1)

    def addRect(self, svg, x, y, xSpan, ySpan):
        squareWidth = 71.7
        squareHeight = 70.7
        margin = 8
        path = f'M{x * squareWidth + margin} {y * squareHeight + margin} L{(x + 1 + xSpan) * squareWidth - margin} {y * squareHeight + margin} L{(x + 1 + xSpan) * squareWidth - margin} {(y + 1 + ySpan) * squareHeight - margin} L{x * squareWidth + margin} {(y + 1 + ySpan) * squareHeight - margin} Z'
        svg.append(gui.SvgPath(path, style={'fill': 'blue'}))

    def removeTiles(self):
        self.remove_child(self.tileContainer)
        self.tileContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_VERTICAL, margin='0px',
                                           style={'display': 'block', 'overflow': 'auto'})
        self.append(self.tileContainer)
