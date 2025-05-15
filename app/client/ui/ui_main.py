# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from . import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size: 14px;\n"
"	\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: black;\n"
"	font-size: 14px;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.App = QWidget(self.centralwidget)
        self.App.setObjectName(u"App")
        self.App.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.App.sizePolicy().hasHeightForWidth())
        self.App.setSizePolicy(sizePolicy1)
        self.App.setMinimumSize(QSize(0, 0))
        self.App.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(self.App)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 8, 8, 8)
        self.LeftSBar = QGroupBox(self.App)
        self.LeftSBar.setObjectName(u"LeftSBar")
        sizePolicy1.setHeightForWidth(self.LeftSBar.sizePolicy().hasHeightForWidth())
        self.LeftSBar.setSizePolicy(sizePolicy1)
        self.LeftSBar.setMinimumSize(QSize(320, 0))
        self.LeftSBar.setMaximumSize(QSize(320, 16777215))
        self.LeftSBar.setStyleSheet(u"#LeftSBar{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	color: black;\n"
"}")
        self.LeftSideBar = QVBoxLayout(self.LeftSBar)
        self.LeftSideBar.setSpacing(0)
        self.LeftSideBar.setObjectName(u"LeftSideBar")
        self.LeftSideBar.setContentsMargins(0, 0, 0, 0)
        self.Content_L = QFrame(self.LeftSBar)
        self.Content_L.setObjectName(u"Content_L")
        sizePolicy1.setHeightForWidth(self.Content_L.sizePolicy().hasHeightForWidth())
        self.Content_L.setSizePolicy(sizePolicy1)
        self.Content_L.setStyleSheet(u"QPushButton {\n"
"	font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: rgb(75, 75, 75);\n"
"    background-color: white;  \n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 0px 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(167, 167, 167);\n"
"  	color: black;\n"
"}\n"
"\n"
"#btns{\n"
"	border-top: 1px solid black;	\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.Content_L)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.LeftSideBar.addWidget(self.Content_L)


        self.horizontalLayout_5.addWidget(self.LeftSBar)

        self.MainBar = QGroupBox(self.App)
        self.MainBar.setObjectName(u"MainBar")
        sizePolicy1.setHeightForWidth(self.MainBar.sizePolicy().hasHeightForWidth())
        self.MainBar.setSizePolicy(sizePolicy1)
        self.MainBar.setMinimumSize(QSize(600, 0))
        self.MainBar.setMaximumSize(QSize(1000, 16777215))
        self.MainBar.setStyleSheet(u"#MainBar {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	color: white;\n"
"}")
        self.MainBar.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.MainBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Content_Main = QFrame(self.MainBar)
        self.Content_Main.setObjectName(u"Content_Main")
        self.Content_M = QVBoxLayout(self.Content_Main)
        self.Content_M.setSpacing(0)
        self.Content_M.setObjectName(u"Content_M")
        self.Content_M.setContentsMargins(0, 0, 0, 0)
        self.crnt_playlist = QFrame(self.Content_Main)
        self.crnt_playlist.setObjectName(u"crnt_playlist")
        self.current_playlist = QHBoxLayout(self.crnt_playlist)
        self.current_playlist.setSpacing(0)
        self.current_playlist.setObjectName(u"current_playlist")
        self.current_playlist.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.crnt_playlist)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"#playlistWidget_frame{\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"#playlistWidget{\n"
"	border: none;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.list_cover = QLabel(self.content)
        self.list_cover.setObjectName(u"list_cover")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_cover.sizePolicy().hasHeightForWidth())
        self.list_cover.setSizePolicy(sizePolicy2)
        self.list_cover.setMinimumSize(QSize(0, 202))
        self.list_cover.setMaximumSize(QSize(16777215, 202))

        self.verticalLayout_3.addWidget(self.list_cover)

        self.list_controls = QLabel(self.content)
        self.list_controls.setObjectName(u"list_controls")
        sizePolicy2.setHeightForWidth(self.list_controls.sizePolicy().hasHeightForWidth())
        self.list_controls.setSizePolicy(sizePolicy2)
        self.list_controls.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.list_controls)

        self.playlistWidget_frame = QFrame(self.content)
        self.playlistWidget_frame.setObjectName(u"playlistWidget_frame")
        self.playlistWidget_frame.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QTableWidget {\n"
"    background-color: rgb(18, 18, 18);\n"
"    color: white;\n"
"    gridline-color: rgba(255, 255, 255, 30%);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0435 \u043b\u0438\u043d\u0438\u0438 */\n"
"    border: none;\n"
"    outline: none;  /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043a\u0443\u0441\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(18, 18, 18);\n"
"    color: white;\n"
"    padding: 10px 15px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 20%);\n"
""
                        "    font-weight: bold;\n"
"}\n"
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 (\u0432\u0435\u0440\u0445\u043d\u0438\u0435) */\n"
"QHeaderView::section:horizontal {\n"
"    border-right: none;\n"
"}\n"
"\n"
"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 (\u0431\u043e\u043a\u043e\u0432\u044b\u0435) */\n"
"QHeaderView::section:vertical {\n"
"    border-right: none;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u043e\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 */\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 20%);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u044f\u0447\u0435\u0435\u043a */\n"
"QTableWidget::item {\n"
"    padding: 8px 15px;\n"
"}\n"
"\n"
"/* \u0412"
                        "\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255, 255, 255, 10%);\n"
"}\n"
"\n"
"/* \u042d\u0444\u0444\u0435\u043a\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(255, 255, 255, 5%);\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u043e\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 */\n"
"QTableWidget::item:focus {\n"
"    outline: none;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.playlistWidget_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.playlistWidget = QTableWidget(self.playlistWidget_frame)
        if (self.playlistWidget.columnCount() < 4):
            self.playlistWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.playlistWidget.rowCount() < 7):
            self.playlistWidget.setRowCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.playlistWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.playlistWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.playlistWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.playlistWidget.setObjectName(u"playlistWidget")
        sizePolicy1.setHeightForWidth(self.playlistWidget.sizePolicy().hasHeightForWidth())
        self.playlistWidget.setSizePolicy(sizePolicy1)
        self.playlistWidget.setLayoutDirection(Qt.LeftToRight)
        self.playlistWidget.setStyleSheet(u"")
        self.playlistWidget.setFrameShape(QFrame.StyledPanel)
        self.playlistWidget.setLineWidth(1)
        self.playlistWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.playlistWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.playlistWidget.setAutoScroll(False)
        self.playlistWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playlistWidget.setTabKeyNavigation(True)
        self.playlistWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlistWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.playlistWidget.setTextElideMode(Qt.ElideRight)
        self.playlistWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.playlistWidget.setShowGrid(False)
        self.playlistWidget.setGridStyle(Qt.NoPen)
        self.playlistWidget.setWordWrap(True)
        self.playlistWidget.setCornerButtonEnabled(False)
        self.playlistWidget.setRowCount(7)
        self.playlistWidget.setColumnCount(4)
        self.playlistWidget.horizontalHeader().setVisible(True)
        self.playlistWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.playlistWidget.horizontalHeader().setHighlightSections(False)
        self.playlistWidget.horizontalHeader().setStretchLastSection(True)
        self.playlistWidget.verticalHeader().setVisible(True)
        self.playlistWidget.verticalHeader().setCascadingSectionResizes(False)
        self.playlistWidget.verticalHeader().setHighlightSections(False)
        self.playlistWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.playlistWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.playlistWidget)


        self.verticalLayout_3.addWidget(self.playlistWidget_frame)


        self.current_playlist.addWidget(self.content)


        self.Content_M.addWidget(self.crnt_playlist)


        self.verticalLayout_4.addWidget(self.Content_Main)


        self.horizontalLayout_5.addWidget(self.MainBar)

        self.RightSideBar = QGroupBox(self.App)
        self.RightSideBar.setObjectName(u"RightSideBar")
        sizePolicy1.setHeightForWidth(self.RightSideBar.sizePolicy().hasHeightForWidth())
        self.RightSideBar.setSizePolicy(sizePolicy1)
        self.RightSideBar.setMinimumSize(QSize(320, 0))
        self.RightSideBar.setMaximumSize(QSize(320, 16777215))
        self.RightSideBar.setStyleSheet(u"#RightSideBar{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	color: white;\n"
"}\n"
"")
        self.RightSideBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.RightSideBar.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.RightSideBar)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Content_R = QFrame(self.RightSideBar)
        self.Content_R.setObjectName(u"Content_R")
        self.Content_R.setLayoutDirection(Qt.LeftToRight)
        self.Content_R.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.Content_R)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SongSelect = QFrame(self.Content_R)
        self.SongSelect.setObjectName(u"SongSelect")
        sizePolicy.setHeightForWidth(self.SongSelect.sizePolicy().hasHeightForWidth())
        self.SongSelect.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.SongSelect)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SelectSong = QFrame(self.SongSelect)
        self.SelectSong.setObjectName(u"SelectSong")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SelectSong.sizePolicy().hasHeightForWidth())
        self.SelectSong.setSizePolicy(sizePolicy3)
        self.SelectSong.setStyleSheet(u"#SelectAudioLb{\n"
"	font-size: 18px;\n"
"	color: white; \n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(107, 107, 107);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.SelectSong)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.SelectAudioLb = QLabel(self.SelectSong)
        self.SelectAudioLb.setObjectName(u"SelectAudioLb")
        sizePolicy3.setHeightForWidth(self.SelectAudioLb.sizePolicy().hasHeightForWidth())
        self.SelectAudioLb.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.SelectAudioLb)

        self.SelectAudioBtn = QPushButton(self.SelectSong)
        self.SelectAudioBtn.setObjectName(u"SelectAudioBtn")
        sizePolicy3.setHeightForWidth(self.SelectAudioBtn.sizePolicy().hasHeightForWidth())
        self.SelectAudioBtn.setSizePolicy(sizePolicy3)
        icon = QIcon()
        icon.addFile(u":/icon/icons/file_open_50dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectAudioBtn.setIcon(icon)
        self.SelectAudioBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.SelectAudioBtn)


        self.horizontalLayout_7.addWidget(self.SelectSong)


        self.verticalLayout_5.addWidget(self.SongSelect)

        self.MetaData = QFrame(self.Content_R)
        self.MetaData.setObjectName(u"MetaData")
        sizePolicy2.setHeightForWidth(self.MetaData.sizePolicy().hasHeightForWidth())
        self.MetaData.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.MetaData)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.SongInfo = QFrame(self.MetaData)
        self.SongInfo.setObjectName(u"SongInfo")
        sizePolicy3.setHeightForWidth(self.SongInfo.sizePolicy().hasHeightForWidth())
        self.SongInfo.setSizePolicy(sizePolicy3)
        self.SongInfo.setStyleSheet(u"#MetaData_lb{\n"
"	font-size: 18px;\n"
"	color: white; \n"
"}\n"
"\n"
"#TrackInfo{\n"
"	color: black;\n"
"	font-size: 16px;\n"
"	background-color: white;\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.SongInfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MetaData_lb = QLabel(self.SongInfo)
        self.MetaData_lb.setObjectName(u"MetaData_lb")

        self.verticalLayout_6.addWidget(self.MetaData_lb)

        self.TrackInfo = QTextEdit(self.SongInfo)
        self.TrackInfo.setObjectName(u"TrackInfo")
        self.TrackInfo.setMinimumSize(QSize(0, 0))
        self.TrackInfo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.TrackInfo)


        self.horizontalLayout_8.addWidget(self.SongInfo)


        self.verticalLayout_5.addWidget(self.MetaData)

        self.CurrentSong = QFrame(self.Content_R)
        self.CurrentSong.setObjectName(u"CurrentSong")
        sizePolicy2.setHeightForWidth(self.CurrentSong.sizePolicy().hasHeightForWidth())
        self.CurrentSong.setSizePolicy(sizePolicy2)
        self.CurrentSong.setStyleSheet(u"#CurrentFile_lb{\n"
"	font-size: 18px;\n"
"	color: white; \n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.CurrentSong)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.song_lb = QFrame(self.CurrentSong)
        self.song_lb.setObjectName(u"song_lb")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.song_lb.sizePolicy().hasHeightForWidth())
        self.song_lb.setSizePolicy(sizePolicy4)
        self.verticalLayout_8 = QVBoxLayout(self.song_lb)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.crnt_sng = QFrame(self.song_lb)
        self.crnt_sng.setObjectName(u"crnt_sng")
        self.Label = QHBoxLayout(self.crnt_sng)
        self.Label.setSpacing(0)
        self.Label.setObjectName(u"Label")
        self.Label.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_2 = QFrame(self.crnt_sng)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy3.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy3)
        self.horizontalFrame_2.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalFrame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/audio_file_50dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.CurrentFile_lb = QLabel(self.horizontalFrame_2)
        self.CurrentFile_lb.setObjectName(u"CurrentFile_lb")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.CurrentFile_lb.sizePolicy().hasHeightForWidth())
        self.CurrentFile_lb.setSizePolicy(sizePolicy5)
        self.CurrentFile_lb.setAlignment(Qt.AlignCenter)
        self.CurrentFile_lb.setIndent(0)

        self.horizontalLayout_3.addWidget(self.CurrentFile_lb)


        self.Label.addWidget(self.horizontalFrame_2)


        self.verticalLayout_8.addWidget(self.crnt_sng)

        self.frame = QFrame(self.song_lb)
        self.frame.setObjectName(u"frame")
        self.CurrentSong_name = QHBoxLayout(self.frame)
        self.CurrentSong_name.setSpacing(0)
        self.CurrentSong_name.setObjectName(u"CurrentSong_name")
        self.CurrentSong_name.setContentsMargins(0, 0, 0, 0)
        self.CurrentFile = QLabel(self.frame)
        self.CurrentFile.setObjectName(u"CurrentFile")
        sizePolicy3.setHeightForWidth(self.CurrentFile.sizePolicy().hasHeightForWidth())
        self.CurrentFile.setSizePolicy(sizePolicy3)

        self.CurrentSong_name.addWidget(self.CurrentFile)


        self.verticalLayout_8.addWidget(self.frame)


        self.horizontalLayout_10.addWidget(self.song_lb)


        self.verticalLayout_5.addWidget(self.CurrentSong)


        self.verticalLayout_7.addWidget(self.Content_R)


        self.horizontalLayout_5.addWidget(self.RightSideBar)


        self.verticalLayout.addWidget(self.App)

        self.Playback = QGroupBox(self.centralwidget)
        self.Playback.setObjectName(u"Playback")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Playback.sizePolicy().hasHeightForWidth())
        self.Playback.setSizePolicy(sizePolicy6)
        self.Playback.setMinimumSize(QSize(100, 0))
        self.Playback.setMaximumSize(QSize(16777215, 100))
        self.Playback.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border: none;")
        self.verticalLayout_11 = QVBoxLayout(self.Playback)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.control_panel = QFrame(self.Playback)
        self.control_panel.setObjectName(u"control_panel")
        sizePolicy1.setHeightForWidth(self.control_panel.sizePolicy().hasHeightForWidth())
        self.control_panel.setSizePolicy(sizePolicy1)
        self.control_panel.setMinimumSize(QSize(0, 0))
        self.control_panel.setMaximumSize(QSize(16777215, 16777215))
        self.control_panel.setLayoutDirection(Qt.RightToLeft)
        self.control_panel.setStyleSheet(u"#control_panel{\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.control_panel)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.control_panel)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(350, 0))
        self.verticalFrame.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.verticalFrame)

        self.playback_panel = QFrame(self.control_panel)
        self.playback_panel.setObjectName(u"playback_panel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.playback_panel.sizePolicy().hasHeightForWidth())
        self.playback_panel.setSizePolicy(sizePolicy7)
        self.playback_panel.setMinimumSize(QSize(580, 0))
        self.playback_panel.setLayoutDirection(Qt.LeftToRight)
        self.playback_panel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"#playback_btn {\n"
"	width: 50px;\n"
"	height: 50px;  \n"
"    color: white;\n"
"    background-color: rgb(255, 255, 255);  \n"
"    border: none;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"#playback_btn:hover {\n"
"	background-color: rgb(190, 190, 190);\n"
"}\n"
"\n"
"#playback_btn:checked {\n"
"	\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.playback_panel)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dj = QFrame(self.playback_panel)
        self.dj.setObjectName(u"dj")
        sizePolicy.setHeightForWidth(self.dj.sizePolicy().hasHeightForWidth())
        self.dj.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.dj)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.playback_btn = QPushButton(self.dj)
        self.playback_btn.setObjectName(u"playback_btn")
        sizePolicy3.setHeightForWidth(self.playback_btn.sizePolicy().hasHeightForWidth())
        self.playback_btn.setSizePolicy(sizePolicy3)
        self.playback_btn.setMinimumSize(QSize(0, 0))
        self.playback_btn.setMaximumSize(QSize(16777215, 16777215))
        self.playback_btn.setAutoFillBackground(False)
        self.playback_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/play_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icon/icons/pause_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.playback_btn.setIcon(icon2)
        self.playback_btn.setIconSize(QSize(40, 40))
        self.playback_btn.setCheckable(True)
        self.playback_btn.setChecked(False)
        self.playback_btn.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.playback_btn)


        self.verticalLayout_2.addWidget(self.dj)

        self.slider = QFrame(self.playback_panel)
        self.slider.setObjectName(u"slider")
        sizePolicy2.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.slider)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.CurrentTime = QLabel(self.slider)
        self.CurrentTime.setObjectName(u"CurrentTime")
        sizePolicy5.setHeightForWidth(self.CurrentTime.sizePolicy().hasHeightForWidth())
        self.CurrentTime.setSizePolicy(sizePolicy5)
        self.CurrentTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.CurrentTime)

        self.SeekBar = QSlider(self.slider)
        self.SeekBar.setObjectName(u"SeekBar")
        self.SeekBar.setMinimumSize(QSize(0, 24))
        self.SeekBar.setMaximumSize(QSize(450, 24))
        self.SeekBar.setStyleSheet(u"QSlider {\n"
"    background-color: transparent; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0442\u0440\u0435\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0442\u0440\u0435\u043a\u0430 */\n"
"    background: #ddd; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0442\u0440\u0435\u043a\u0430 */\n"
"    border-radius: 4px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #000; /* \u0426\u0432\u0435\u0442 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
""
                        "/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u0443\u0441\u0442\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 */\n"
"QSlider::add-page:horizontal {\n"
"    background: #ccc; /* \u0426\u0432\u0435\u0442 \u043f\u0443\u0441\u0442\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"QSlider::handle:horizontal {\n"
"    width: 17px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    background: #ffffff; /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 (\u0431\u0435\u043b\u044b\u0439) */\n"
"    margin: -6px 0; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u0446\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438"
                        "\u044f */\n"
"    border: 1px solid #000; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 (\u0447\u0435\u0440\u043d\u0430\u044f) */\n"
"    border-radius: 9px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 (\u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u043e\u0442 \u0440\u0430\u0437\u043c\u0435\u0440\u0430) */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0434\u0435\u043b\u0435\u043d\u0438\u0439 */\n"
"QSlider::tick-mark:horizontal {\n"
"    background: #888; /* \u0426\u0432\u0435\u0442 \u0434\u0435\u043b\u0435\u043d\u0438\u0439 */\n"
"    height: 4px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0434\u0435\u043b\u0435\u043d\u0438\u0439 */\n"
"    width: 2px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0434\u0435\u043b\u0435\u043d\u0438\u0439 */\n"
"}")
        self.SeekBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.SeekBar)

        self.EndTime = QLabel(self.slider)
        self.EndTime.setObjectName(u"EndTime")
        sizePolicy5.setHeightForWidth(self.EndTime.sizePolicy().hasHeightForWidth())
        self.EndTime.setSizePolicy(sizePolicy5)
        self.EndTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.EndTime)


        self.verticalLayout_2.addWidget(self.slider)


        self.horizontalLayout.addWidget(self.playback_panel)

        self.verticalFrame_2 = QFrame(self.control_panel)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        sizePolicy7.setHeightForWidth(self.verticalFrame_2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_2.setSizePolicy(sizePolicy7)
        self.verticalFrame_2.setMinimumSize(QSize(350, 0))
        self.verticalFrame_2.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.verticalFrame_2)


        self.verticalLayout_11.addWidget(self.control_panel)


        self.verticalLayout.addWidget(self.Playback)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.list_cover.setText(QCoreApplication.translate("MainWindow", u"Current playlist", None))
        self.list_controls.setText(QCoreApplication.translate("MainWindow", u"Nav bar", None))
        ___qtablewidgetitem = self.playlistWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.playlistWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qtablewidgetitem2 = self.playlistWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Album", None));
        ___qtablewidgetitem3 = self.playlistWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem4 = self.playlistWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.playlistWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.playlistWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        self.SelectAudioLb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b", None))
        self.SelectAudioBtn.setText("")
        self.MetaData_lb.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.TrackInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0442\u0440\u0435\u043a\u0435 \u0431\u0443\u0434\u0435\u0442 \u0442\u0443\u0442...", None))
        self.pushButton.setText("")
        self.CurrentFile_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.CurrentFile.setText("")
        self.CurrentTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.EndTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
    # retranslateUi

