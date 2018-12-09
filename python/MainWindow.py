import sys
from TitleBar import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.InitializeWindow()

    def InitializeWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT);
        self.InitializeViews()
        self.setStyleSheet(str(self.LoadStyleFromQss(WINDOW_QSS)))

    def InitializeViews(self):
        self.titleBar = TitleBar(self)
        self.client = QWidget(self)
        self.center = QWidget(self)

        self.setCentralWidget(self.center)

        self.lay = QVBoxLayout(self)
        self.center.setLayout(self.lay)

        self.lay.addWidget(self.titleBar);
        self.lay.addWidget(self.client);
        self.lay.setStretch(1, 100);
        self.lay.setSpacing(0);
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.titleBar.SetIcon(QPixmap(WINDOW_ICON));
        self.titleBar.SetTitle(WINDOW_TITLE);

    def LoadStyleFromQss(self, f):
        file = open(f)
        lines = file.readlines()
        file.close()
        res = ''
        for line in lines:
            res += line

        return res


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
    pass
