import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from default import *

class TitleBar(QWidget):
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.win = parent
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setFixedHeight(TITLE_BAR_HEIGHT)
        self.InitializeViews()
        pass

    def InitializeViews(self):
        self.iconLabel = QLabel(self)
        self.titleLabel = QLabel(self)

        self.minButton = QPushButton(self)
        self.restoreButton = QPushButton(self)
        self.closeButton = QPushButton(self)

        self.minButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE);
        self.restoreButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE);
        self.closeButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE);

        self.iconLabel.setFixedSize(TITLE_LABEL_SIZE, TITLE_LABEL_SIZE);
        self.titleLabel.setFixedHeight(TITLE_LABEL_SIZE);

        self.iconLabel.setAlignment(Qt.AlignCenter);
        self.titleLabel.setAlignment(Qt.AlignCenter);

        self.minButton.setIcon(QIcon(TITLE_MIN_ICON));
        self.restoreButton.setIcon(QIcon(TITLE_RESTORE_ICON));
        self.closeButton.setIcon(QIcon(TITLE_CLS_ICON));

        self.minButton.clicked.connect(self.ShowMininizedWindow)
        self.restoreButton.clicked.connect(self.ShowRestoreWindow)
        self.closeButton.clicked.connect(self.CloseWindow)

        self.lay = QHBoxLayout(self)
        self.setLayout(self.lay)

        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

    def ShowMininizedWindow(self):
        self.win.showMinimized()

    def ShowMaximizedWindow(self):
        self.window.showMaximized()

    def ShowRestoreWindow(self):
        if self.win.isMaximized():
            self.win.showNormal()
        else:
            self.win.showMaximized()

    def CloseWindow(self):
        self.win.close()

    def SetTitle(self, str):
        self.titleLabel.setText(str)

    def SetIcon(self, pix):
        self.iconLabel.setPixmap(pix.scaled(self.iconLabel.size() - QSize(TITLE_ICON_MAG, TITLE_ICON_MAG)))

    def mouseDoubleClickEvent(self, event):
        self.ShowRestoreWindow()
        return QWidget().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self.win.isMaximized:
                self.win.showNormal()

            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.win.move(self.win.pos() + movePos)

        return QWidget().mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TitleBar(None)
    win.show()
    sys.exit(app.exec_())
    pass
