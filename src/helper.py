import os
import shutil

from pathlib import Path
import requests


def downloadResource(url, file):
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    if not os.path.isfile(file):
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    downloadResource('https://images-na.ssl-images-amazon.com/images/I/71TS9IobWWL._AC_SL1500_.jpg', '../res/board.jpg')
    downloadResource('https://images-na.ssl-images-amazon.com/images/I/71H07a26emL._AC_SL1500_.jpg', '../res/tiles.jpg')

import remi.gui as gui
from remi import start, App


# polygon(56% 16%, 63% 17%, 62% 22%, 68% 22%, 68% 17%, 74% 17%, 74% 27%, 56% 27%, 49% 35%, 39% 28%)

class BoardGui(App):
    def __init__(self, *args):
        super(BoardGui, self).__init__(*args, static_file_path={'my_resources': '../res/'})

    def main(self):
        self.container = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_VERTICAL, margin='0px',
                                       style={'display': 'block', 'overflow': 'auto'})

        self.boardContainer = gui.Container(style={
            'height': str(1422 - 160 - 460) + 'px',
            'width': str(1242 - 280 - 157) + 'px',
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

        self.tileContainer = gui.Container(style={
            'top': '-160px',
            'left': '-160px',
            'height': '1060px',
            'width': '1060px',
            'clip-path': 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)',
            'background-image': 'url(/my_resources:tiles.jpg)',
            'background-size': 'cover'})
        self.container.append(self.boardContainer)

        svg = gui.Svg(style={
            'position': 'absolute',
            'top': '10px',
            'left': '10px'})
        svg.append(gui.SvgPath('M5 5 L66 5 L66 66 L5 66 Z'))
        self.container.append(svg)

        return self.container


# starts the web server
start(BoardGui)
