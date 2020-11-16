from threading import Timer, Thread

from remi import start, App

from src.bruteForceSearch import BruteForceSearch
from src.gameSettings import tiles, board
from src.gui import BoardGui
from src.helper import downloadResource


class MainApp(App):
    def __init__(self, *args):
        self.boardGui = BoardGui()
        super(MainApp, self).__init__(*args, static_file_path={'my_resources': '../res/'})

    def main(self):
        downloadResource('https://images-na.ssl-images-amazon.com/images/I/71TS9IobWWL._AC_SL1500_.jpg',
                         '../res/board.jpg')
        downloadResource('https://images-na.ssl-images-amazon.com/images/I/71H07a26emL._AC_SL1500_.jpg',
                         '../res/tiles.jpg')

        self.bruteForceSearch = BruteForceSearch(tiles, board, self.updateFunction)

        Thread(target=self.bruteForceSearch.start).start()

        self.intervalFunction(1)  # first call, then the function is called automatically by timer

        return self.boardGui

    def intervalFunction(self, updateInterval):
        Timer(updateInterval, self.intervalFunction, (updateInterval,)).start()

    def updateFunction(self, update):
        self.boardGui.displayTiles(update['tiles'])


if __name__ == '__main__':
    # starts the web server
    start(MainApp)#, start_browser=False)

    # search without GUI
    # BruteForceSearch(tiles, board, lambda result: None).start()
