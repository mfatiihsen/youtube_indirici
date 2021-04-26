from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit,QMainWindow, QPushButton
import sys
from pytube import YouTube

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.show()
        self.ustAyarlar()
        self.anaMenu()
        
    def ustAyarlar(self):
        self.setGeometry(400,200,800,400)
        self.setWindowTitle("YouTube Video İndirici - MFS Software")

    def anaMenu(self):
        self.yazi = QLabel("<b>YouTube linkini giriniz : </b>",self)
        self.yazi.setGeometry(100,100,170,30)
        self.yazi.show()

        self.link = QLineEdit(self)
        self.link.setGeometry(270,100,300,30)
        self.link.show()

        self.indir = QPushButton("İndir",self)
        self.indir.setGeometry(600,100,80,30)
        self.indir.show()
        self.indir.clicked.connect(self.indir_video)
        
    def indir_video(self):
        url = self.link.text()
        YouTube(url).streams.first().download()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Win()
    pencere.show()
    sys.exit(app.exec())