# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp3_player.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtGui
from pygame import mixer
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 458)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 181, 441))
        self.frame.setStyleSheet("#frame{\n"
"    background-color:#33c2c2;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mysong_btn = QtWidgets.QPushButton(self.frame)
        self.mysong_btn.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.mysong_btn.setFont(font)
        self.mysong_btn.setStyleSheet("#mysong_btn{\n"
"    \n"
"    background-color:#33c2c2;\n"
"    border-radius:100%;\n"
"    \n"
"}\n"
"")
        self.mysong_btn.setObjectName("mysong_btn")
        self.recentplayed_btn = QtWidgets.QPushButton(self.frame)
        self.recentplayed_btn.setGeometry(QtCore.QRect(20, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.recentplayed_btn.setFont(font)
        self.recentplayed_btn.setStyleSheet("#recentplayed_btn{\n"
"    backgroung-color:#33c2c2;\n"
"    border-radius:100%;\n"
"}")
        self.recentplayed_btn.setObjectName("recentplayed_btn")
        self.playlist_btn = QtWidgets.QPushButton(self.frame)
        self.playlist_btn.setGeometry(QtCore.QRect(20, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.playlist_btn.setFont(font)
        self.playlist_btn.setStyleSheet("#playlist_btn{\n"
"    backgroung-color:#33c2c2;\n"
"    border-radius:100%;\n"
"}")
        self.playlist_btn.setObjectName("playlist_btn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(180, 290, 481, 131))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color:#5e90a2;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 451, 31))
        self.textEdit.setObjectName("textEdit")
        self.volume = QtWidgets.QSlider(self.frame_2)
        self.volume.setGeometry(QtCore.QRect(300, 60, 131, 22))
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")
        self.forward_btn = QtWidgets.QPushButton(self.frame_2)
        self.forward_btn.setGeometry(QtCore.QRect(210, 50, 51, 41))
        self.forward_btn.setStyleSheet("#forward_btn{\n"
"    background-color:blue;\n"
"    border-style:outside;\n"
"    border-width:5px;\n"
"    border-radius:20px;\n"
"    \n"
"}")
        self.forward_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/forward02.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward_btn.setIcon(icon)
        self.forward_btn.setIconSize(QtCore.QSize(27, 28))
        self.forward_btn.setObjectName("forward_btn")
        self.play_btn = QtWidgets.QPushButton(self.frame_2)
        self.play_btn.setGeometry(QtCore.QRect(130, 50, 51, 41))
        self.play_btn.setStyleSheet("#play_btn{\n"
"    background-color:white;\n"
"    border-style:outside;\n"
"    border-width:5px;\n"
"    border-radius:20px;\n"
"    \n"
"}")
        self.play_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/play01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QtCore.QSize(26, 23))
        self.play_btn.setCheckable(False)
        self.play_btn.setObjectName("play_btn")
        self.backward_btn = QtWidgets.QPushButton(self.frame_2)
        self.backward_btn.setGeometry(QtCore.QRect(60, 50, 51, 41))
        self.backward_btn.setStyleSheet("#backward_btn{\n"
"    background-color:blue;\n"
"    border-style:outside;\n"
"    border-width:5px;\n"
"    border-radius:20px;\n"
"    \n"
"}")
        self.backward_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/Backward-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backward_btn.setIcon(icon2)
        self.backward_btn.setIconSize(QtCore.QSize(30, 30))
        self.backward_btn.setObjectName("backward_btn")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(180, 0, 451, 291))
        self.frame_3.setStyleSheet("#frame_3{\n"
"      background-color:#5e90a2;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.playlist_btn02 = QtWidgets.QPushButton(self.frame_3)
        self.playlist_btn02.setGeometry(QtCore.QRect(200, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.playlist_btn02.setFont(font)
        self.playlist_btn02.setStyleSheet("#playlist_btn02{\n"
"    background-color:#5e90a2;\n"
"    border-radius:100%;\n"
"\n"
"}")
        self.playlist_btn02.setObjectName("playlist_btn02")
        self.songs_btn = QtWidgets.QPushButton(self.frame_3)
        self.songs_btn.setGeometry(QtCore.QRect(30, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.songs_btn.setFont(font)
        self.songs_btn.setStyleSheet("#songs_btn{\n"
"    backgroung-color:#5e90a2;\n"
"    border-radius:100%;\n"
"}")
        self.songs_btn.setObjectName("songs_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        self.menuSETTING = QtWidgets.QMenu(self.menubar)
        self.menuSETTING.setObjectName("menuSETTING")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMy_Songs = QtWidgets.QAction(MainWindow)
        self.actionMy_Songs.setObjectName("actionMy_Songs")
        self.actionCreate_Song_List = QtWidgets.QAction(MainWindow)
        self.actionCreate_Song_List.setObjectName("actionCreate_Song_List")
        self.actionShare_Songs = QtWidgets.QAction(MainWindow)
        self.actionShare_Songs.setObjectName("actionShare_Songs")
        self.actionSound_Effect = QtWidgets.QAction(MainWindow)
        self.actionSound_Effect.setObjectName("actionSound_Effect")
        self.actionSong_Speed = QtWidgets.QAction(MainWindow)
        self.actionSong_Speed.setObjectName("actionSong_Speed")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuMENU.addAction(self.actionMy_Songs)
        self.menuMENU.addAction(self.actionCreate_Song_List)
        self.menuMENU.addAction(self.actionShare_Songs)
        self.menuSETTING.addAction(self.actionSound_Effect)
        self.menuSETTING.addAction(self.actionSong_Speed)
        self.menuHELP.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMENU.menuAction())
        self.menubar.addAction(self.menuSETTING.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mysong_btn.setText(_translate("MainWindow", "My Songs "))
        self.recentplayed_btn.setText(_translate("MainWindow", "Recently Played"))
        self.playlist_btn.setText(_translate("MainWindow", "Play List"))
        self.frame_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>uoww jterijt[betj b[tj </p></body></html>"))
        self.playlist_btn02.setText(_translate("MainWindow", "PLAY LIST"))
        self.songs_btn.setText(_translate("MainWindow", "SONGS"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.menuSETTING.setTitle(_translate("MainWindow", "SETTING"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.actionMy_Songs.setText(_translate("MainWindow", "My Songs"))
        self.actionCreate_Song_List.setText(_translate("MainWindow", "Create Song List"))
        self.actionShare_Songs.setText(_translate("MainWindow", "Share Songs"))
        self.actionSound_Effect.setText(_translate("MainWindow", "Sound Effect "))
        self.actionSong_Speed.setText(_translate("MainWindow", "Song Speed"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def song_list(self):
        self.path = 'song'
        self.listofsongs = os.listdir(self.path)
        for self.songs in self.listofsongs:
            self.labelsongs = QtWidgets.QLabel(self.songs, self.frame_3)
            self.labelsongs








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
