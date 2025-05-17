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
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
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
"	color: white;\n"
"}")
        self.LeftSideBar = QVBoxLayout(self.LeftSBar)
        self.LeftSideBar.setSpacing(0)
        self.LeftSideBar.setObjectName(u"LeftSideBar")
        self.LeftSideBar.setContentsMargins(0, 0, 0, 0)
        self.Content_L = QFrame(self.LeftSBar)
        self.Content_L.setObjectName(u"Content_L")
        sizePolicy1.setHeightForWidth(self.Content_L.sizePolicy().hasHeightForWidth())
        self.Content_L.setSizePolicy(sizePolicy1)
        self.Content_L.setStyleSheet(u"#Content_L{\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	padding-top: 20px;\n"
"	padding-bottom: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"  	color: white;\n"
"	font: 63 10pt \"Alexandria\";\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.Content_L)
        self.verticalLayout_10.setSpacing(16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.playlist_manager_top = QFrame(self.Content_L)
        self.playlist_manager_top.setObjectName(u"playlist_manager_top")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.playlist_manager_top.sizePolicy().hasHeightForWidth())
        self.playlist_manager_top.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.playlist_manager_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_pm = QFrame(self.playlist_manager_top)
        self.header_pm.setObjectName(u"header_pm")
        sizePolicy2.setHeightForWidth(self.header_pm.sizePolicy().hasHeightForWidth())
        self.header_pm.setSizePolicy(sizePolicy2)
        self.header_pm.setLayoutDirection(Qt.LeftToRight)
        self.header_pm.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;  \n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(158, 158, 158, 110)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(223, 223, 223, 110)\n"
"}\n"
"\n"
"QLabel{\n"
"    font-family: \"Onest ExtraBold\";\n"
"    font-weight: 800; /* Extra Bold */\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    qproperty-alignment: 'AlignCenter'; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    qproperty-wordWrap: false; /* \u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u0441\u043b\u043e\u0432 */\n"
"    qproperty-indent: 0; /* \u041e\u0442\u0441\u0442\u0443\u043f \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    qproperty-margin: 0; /* \u0412\u043d\u0435\u0448\u043d"
                        "\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.header_pm)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title_pm = QFrame(self.header_pm)
        self.title_pm.setObjectName(u"title_pm")
        sizePolicy.setHeightForWidth(self.title_pm.sizePolicy().hasHeightForWidth())
        self.title_pm.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.title_pm)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.favicon = QLabel(self.title_pm)
        self.favicon.setObjectName(u"favicon")
        sizePolicy2.setHeightForWidth(self.favicon.sizePolicy().hasHeightForWidth())
        self.favicon.setSizePolicy(sizePolicy2)
        self.favicon.setMinimumSize(QSize(40, 40))
        self.favicon.setMaximumSize(QSize(40, 40))
        self.favicon.setPixmap(QPixmap(u":/icon/icons/open_lib.png"))
        self.favicon.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.favicon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mediateka_lb = QLabel(self.title_pm)
        self.mediateka_lb.setObjectName(u"mediateka_lb")
        sizePolicy2.setHeightForWidth(self.mediateka_lb.sizePolicy().hasHeightForWidth())
        self.mediateka_lb.setSizePolicy(sizePolicy2)
        self.mediateka_lb.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.mediateka_lb, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.title_pm, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.header_btn = QFrame(self.header_pm)
        self.header_btn.setObjectName(u"header_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_btn.sizePolicy().hasHeightForWidth())
        self.header_btn.setSizePolicy(sizePolicy3)
        self.header_btn.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_14 = QHBoxLayout(self.header_btn)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 6, 0, 0)
        self.add_obj_btn = QPushButton(self.header_btn)
        self.add_obj_btn.setObjectName(u"add_obj_btn")
        self.add_obj_btn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icons/playlist_add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_obj_btn.setIcon(icon)
        self.add_obj_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_14.addWidget(self.add_obj_btn)


        self.horizontalLayout_4.addWidget(self.header_btn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.header_pm)


        self.verticalLayout_10.addWidget(self.playlist_manager_top)

        self.switch_mode = QFrame(self.Content_L)
        self.switch_mode.setObjectName(u"switch_mode")
        sizePolicy2.setHeightForWidth(self.switch_mode.sizePolicy().hasHeightForWidth())
        self.switch_mode.setSizePolicy(sizePolicy2)
        self.switch_mode.setMinimumSize(QSize(0, 0))
        self.switch_mode.setStyleSheet(u"QPushButton {\n"
"    background-color: #2A2A2A;\n"
"	color: white;  \n"
"    border: none;\n"
"    border-radius: 16px;\n"
"	padding: 0px, 3px, 0px, 0px;\n"
"	font: 75 15px \"Onest\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(158, 158, 158, 110)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(255, 255, 255);\n"
"	color: rgb(18, 18, 18);\n"
"}")
        self.mode_switcher = QHBoxLayout(self.switch_mode)
        self.mode_switcher.setSpacing(8)
        self.mode_switcher.setObjectName(u"mode_switcher")
        self.mode_switcher.setContentsMargins(0, 0, 0, 0)
        self.radio_mode = QPushButton(self.switch_mode)
        self.radio_mode.setObjectName(u"radio_mode")
        sizePolicy3.setHeightForWidth(self.radio_mode.sizePolicy().hasHeightForWidth())
        self.radio_mode.setSizePolicy(sizePolicy3)
        self.radio_mode.setMinimumSize(QSize(105, 32))
        self.radio_mode.setMaximumSize(QSize(16777215, 16777215))
        self.radio_mode.setCheckable(True)
        self.radio_mode.setChecked(True)
        self.radio_mode.setFlat(False)

        self.mode_switcher.addWidget(self.radio_mode)

        self.playlist_mode = QPushButton(self.switch_mode)
        self.playlist_mode.setObjectName(u"playlist_mode")
        sizePolicy3.setHeightForWidth(self.playlist_mode.sizePolicy().hasHeightForWidth())
        self.playlist_mode.setSizePolicy(sizePolicy3)
        self.playlist_mode.setMinimumSize(QSize(65, 32))
        self.playlist_mode.setMaximumSize(QSize(16777215, 16777215))
        self.playlist_mode.setCheckable(True)

        self.mode_switcher.addWidget(self.playlist_mode)


        self.verticalLayout_10.addWidget(self.switch_mode, 0, Qt.AlignLeft)

        self.pm_controls = QFrame(self.Content_L)
        self.pm_controls.setObjectName(u"pm_controls")
        sizePolicy2.setHeightForWidth(self.pm_controls.sizePolicy().hasHeightForWidth())
        self.pm_controls.setSizePolicy(sizePolicy2)
        self.horizontalLayout_17 = QHBoxLayout(self.pm_controls)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.pm_controls)

        self.pm_frame = QFrame(self.Content_L)
        self.pm_frame.setObjectName(u"pm_frame")
        self.pm_frame.setStyleSheet(u"QListView{\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: none;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.pm_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.playlist_manager = QListView(self.pm_frame)
        self.playlist_manager.setObjectName(u"playlist_manager")
        self.playlist_manager.setFrameShape(QFrame.NoFrame)
        self.playlist_manager.setLineWidth(1)
        self.playlist_manager.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.playlist_manager.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playlist_manager.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.playlist_manager.setIconSize(QSize(48, 48))
        self.playlist_manager.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.playlist_manager.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.playlist_manager.setSpacing(5)
        self.playlist_manager.setViewMode(QListView.ListMode)
        self.playlist_manager.setUniformItemSizes(True)
        self.playlist_manager.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.playlist_manager)


        self.verticalLayout_10.addWidget(self.pm_frame)


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
        self.Content_Main.setStyleSheet(u"QLabel{\n"
"    font-family: \"Onest ExtraBold\";\n"
"    font-weight: 800; /* Extra Bold */\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    qproperty-wordWrap: false; /* \u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u0441\u043b\u043e\u0432 */\n"
"    qproperty-indent: 0; /* \u041e\u0442\u0441\u0442\u0443\u043f \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    qproperty-margin: 0; /* \u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}")
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
"\n"
"QLabel {\n"
"  	color: white;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.list_cover = QLabel(self.content)
        self.list_cover.setObjectName(u"list_cover")
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
"    font-size: 14px; \n"
"	font-family: \"Onest ExtraBold\";\n"
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
"    border-bottom: "
                        "1px solid rgba(255, 255, 255, 20%);\n"
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
"    pad"
                        "ding: 8px 15px;\n"
"}\n"
"\n"
"/* \u0412\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 */\n"
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
        self.playlistWidget.setRowCount(0)
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
        self.Content_R.setStyleSheet(u"QLabel{\n"
"    font-family: \"Onest ExtraBold\";\n"
"    font-weight: 800; /* Extra Bold */\n"
"    font-size: 14px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    qproperty-wordWrap: false; /* \u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u0441\u043b\u043e\u0432 */\n"
"    qproperty-indent: 0; /* \u041e\u0442\u0441\u0442\u0443\u043f \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    qproperty-margin: 0; /* \u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}")
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
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.SelectSong = QFrame(self.SongSelect)
        self.SelectSong.setObjectName(u"SelectSong")
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
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SelectAudioLb = QLabel(self.SelectSong)
        self.SelectAudioLb.setObjectName(u"SelectAudioLb")
        sizePolicy3.setHeightForWidth(self.SelectAudioLb.sizePolicy().hasHeightForWidth())
        self.SelectAudioLb.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.SelectAudioLb)

        self.SelectAudioBtn = QPushButton(self.SelectSong)
        self.SelectAudioBtn.setObjectName(u"SelectAudioBtn")
        sizePolicy3.setHeightForWidth(self.SelectAudioBtn.sizePolicy().hasHeightForWidth())
        self.SelectAudioBtn.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/file_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectAudioBtn.setIcon(icon1)
        self.SelectAudioBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.SelectAudioBtn)


        self.horizontalLayout_7.addWidget(self.SelectSong)


        self.verticalLayout_5.addWidget(self.SongSelect)

        self.MetaData = QFrame(self.Content_R)
        self.MetaData.setObjectName(u"MetaData")
        sizePolicy2.setHeightForWidth(self.MetaData.sizePolicy().hasHeightForWidth())
        self.MetaData.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.MetaData)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/audio_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
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
        self.CurrentFile.setWordWrap(True)

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
"\n"
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
        self.playback_panel.setStyleSheet(u"#playback_btn{\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 1px;\n"
"	border-radius: 22.4px;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-family: \"Onest ExtraBold\";\n"
"    font-weight: 800; /* Extra Bold */\n"
"    font-size: 14px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
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
        self.playback_btn.setMinimumSize(QSize(45, 45))
        self.playback_btn.setMaximumSize(QSize(45, 45))
        self.playback_btn.setAutoFillBackground(False)
        self.playback_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icon/icons/pause1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.playback_btn.setIcon(icon3)
        self.playback_btn.setIconSize(QSize(40, 35))
        self.playback_btn.setCheckable(True)
        self.playback_btn.setChecked(False)
        self.playback_btn.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.playback_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.dj)

        self.slider = QFrame(self.playback_panel)
        self.slider.setObjectName(u"slider")
        sizePolicy2.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy2)
        self.slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    background: #535353; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u043e\u0432\u043e\u0439 \u0434\u043e\u0440\u043e\u0436\u043a\u0438 */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 4px;\n"
"    background: #FFF; /* \u0426\u0432\u0435\u0442 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -4px 0;\n"
"    background: white;\n"
"    border-radius: 6px;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.slider)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.CurrentTime = QLabel(self.slider)
        self.CurrentTime.setObjectName(u"CurrentTime")
        sizePolicy3.setHeightForWidth(self.CurrentTime.sizePolicy().hasHeightForWidth())
        self.CurrentTime.setSizePolicy(sizePolicy3)
        self.CurrentTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.CurrentTime)

        self.SeekBar = QSlider(self.slider)
        self.SeekBar.setObjectName(u"SeekBar")
        sizePolicy.setHeightForWidth(self.SeekBar.sizePolicy().hasHeightForWidth())
        self.SeekBar.setSizePolicy(sizePolicy)
        self.SeekBar.setMinimumSize(QSize(0, 30))
        self.SeekBar.setMaximumSize(QSize(450, 16777215))
        self.SeekBar.setStyleSheet(u"")
        self.SeekBar.setSingleStep(1)
        self.SeekBar.setPageStep(10)
        self.SeekBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.SeekBar)

        self.EndTime = QLabel(self.slider)
        self.EndTime.setObjectName(u"EndTime")
        sizePolicy3.setHeightForWidth(self.EndTime.sizePolicy().hasHeightForWidth())
        self.EndTime.setSizePolicy(sizePolicy3)
        self.EndTime.setTextFormat(Qt.AutoText)
        self.EndTime.setScaledContents(False)
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
        self.favicon.setText("")
        self.mediateka_lb.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u044f \u043c\u0435\u0434\u0438\u0430\u0442\u0435\u043a\u0430", None))
        self.add_obj_btn.setText("")
        self.radio_mode.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0435\u0439\u043b\u0438\u0441\u0442\u044b", None))
        self.playlist_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u043e", None))
#if QT_CONFIG(whatsthis)
        self.playlist_manager.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
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

