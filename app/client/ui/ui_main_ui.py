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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 500))
        MainWindow.setMaximumSize(QSize(1280, 650))
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
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size: 14px;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
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
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 0, 4, 0)
        self.LeftSBar = QGroupBox(self.App)
        self.LeftSBar.setObjectName(u"LeftSBar")
        sizePolicy1.setHeightForWidth(self.LeftSBar.sizePolicy().hasHeightForWidth())
        self.LeftSBar.setSizePolicy(sizePolicy1)
        self.LeftSBar.setMinimumSize(QSize(0, 0))
        self.LeftSBar.setMaximumSize(QSize(352, 16777215))
        self.LeftSBar.setStyleSheet(u"#LeftSBar{\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
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
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 3, 0, 3)
        self.ChooseFile = QFrame(self.Content_L)
        self.ChooseFile.setObjectName(u"ChooseFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ChooseFile.sizePolicy().hasHeightForWidth())
        self.ChooseFile.setSizePolicy(sizePolicy2)
        self.ChooseFile.setLayoutDirection(Qt.LeftToRight)
        self.ChooseFile.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 0, 0);  \n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 2px 5px;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(86, 86, 86);  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 18px;\n"
"	color: black; \n"
"	margin: 0px 1px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.ChooseFile)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.ChooseFile)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ChooseFile_lb = QLabel(self.verticalFrame)
        self.ChooseFile_lb.setObjectName(u"ChooseFile_lb")
        font = QFont()
        self.ChooseFile_lb.setFont(font)
        self.ChooseFile_lb.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.ChooseFile_lb)

        self.horizontalFrame = QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.SelectFile_btn = QPushButton(self.horizontalFrame)
        self.SelectFile_btn.setObjectName(u"SelectFile_btn")
        sizePolicy3.setHeightForWidth(self.SelectFile_btn.sizePolicy().hasHeightForWidth())
        self.SelectFile_btn.setSizePolicy(sizePolicy3)
        self.SelectFile_btn.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icon/icons/file_open_50dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectFile_btn.setIcon(icon)
        self.SelectFile_btn.setIconSize(QSize(20, 20))
        self.SelectFile_btn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.SelectFile_btn)

        self.Copy_btn = QPushButton(self.horizontalFrame)
        self.Copy_btn.setObjectName(u"Copy_btn")
        sizePolicy3.setHeightForWidth(self.Copy_btn.sizePolicy().hasHeightForWidth())
        self.Copy_btn.setSizePolicy(sizePolicy3)
        self.Copy_btn.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/content_copy_50dp_E3E3E3_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Copy_btn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.Copy_btn)


        self.verticalLayout_9.addWidget(self.horizontalFrame)


        self.horizontalLayout_2.addWidget(self.verticalFrame)


        self.verticalLayout_10.addWidget(self.ChooseFile)

        self.FilesList = QTableWidget(self.Content_L)
        if (self.FilesList.columnCount() < 3):
            self.FilesList.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.FilesList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.FilesList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.FilesList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.FilesList.setObjectName(u"FilesList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.FilesList.sizePolicy().hasHeightForWidth())
        self.FilesList.setSizePolicy(sizePolicy4)
        self.FilesList.setMinimumSize(QSize(350, 0))
        self.FilesList.setLayoutDirection(Qt.LeftToRight)
        self.FilesList.setStyleSheet(u"QWidget { \n"
"    background-color: white; \n"
"	font: 8pt \"Yu Gothic UI Semibold\";\n"
"	border: none;\n"
"}\n"
"\n"
" QTableWidget QHeaderView::section { \n"
"	background-color: white;\n"
"    border: 1px solid rgb(58, 58, 58);\n"
"	color: black;\n"
"	font-size: 18px;\n"
"	font: 10pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QTableCornerButton::section { \n"
"	background-color: white;\n"
"    border: 1px solid rgb(58, 58, 58);\n"
"}\n"
"\n"
"QHeaderView::section:vertical{\n"
"	font-size: 15px;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"    border: 1px solid rgb(58, 58, 58);/* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"	padding-left: 6px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: rgb(58, 58, 58);              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-size: 15px;                     /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430"
                        " */\n"
"    border: 1px solid rgb(58, 58, 58);/* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 0px;                        /* \u041e\u0442\u0441\u0442\u0443\u043f \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    margin: 0px;                         /* \u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: rgb(206, 206, 206);             \n"
"}")
        self.FilesList.setFrameShape(QFrame.Box)
        self.FilesList.setAutoScroll(True)
        self.FilesList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.FilesList.setTabKeyNavigation(True)
        self.FilesList.setAlternatingRowColors(False)
        self.FilesList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.FilesList.setGridStyle(Qt.SolidLine)
        self.FilesList.setSortingEnabled(False)
        self.FilesList.setWordWrap(True)
        self.FilesList.setCornerButtonEnabled(False)
        self.FilesList.setRowCount(0)
        self.FilesList.setColumnCount(3)
        self.FilesList.horizontalHeader().setVisible(True)
        self.FilesList.horizontalHeader().setCascadingSectionResizes(False)
        self.FilesList.horizontalHeader().setMinimumSectionSize(50)
        self.FilesList.horizontalHeader().setDefaultSectionSize(90)
        self.FilesList.horizontalHeader().setHighlightSections(True)
        self.FilesList.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.FilesList.horizontalHeader().setStretchLastSection(True)
        self.FilesList.verticalHeader().setVisible(True)
        self.FilesList.verticalHeader().setCascadingSectionResizes(False)
        self.FilesList.verticalHeader().setMinimumSectionSize(30)
        self.FilesList.verticalHeader().setDefaultSectionSize(35)
        self.FilesList.verticalHeader().setHighlightSections(True)
        self.FilesList.verticalHeader().setProperty(u"showSortIndicator", False)
        self.FilesList.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_10.addWidget(self.FilesList)

        self.btns = QFrame(self.Content_L)
        self.btns.setObjectName(u"btns")
        sizePolicy.setHeightForWidth(self.btns.sizePolicy().hasHeightForWidth())
        self.btns.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.btns)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.SaveBtn = QPushButton(self.btns)
        self.SaveBtn.setObjectName(u"SaveBtn")
        sizePolicy3.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/save_50dp_000000_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SaveBtn.setIcon(icon2)
        self.SaveBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.SaveBtn)

        self.SelectAll = QPushButton(self.btns)
        self.SelectAll.setObjectName(u"SelectAll")
        sizePolicy3.setHeightForWidth(self.SelectAll.sizePolicy().hasHeightForWidth())
        self.SelectAll.setSizePolicy(sizePolicy3)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/select_all_50dp_000000_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectAll.setIcon(icon3)
        self.SelectAll.setIconSize(QSize(25, 25))
        self.SelectAll.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.SelectAll)

        self.DeleteBtn = QPushButton(self.btns)
        self.DeleteBtn.setObjectName(u"DeleteBtn")
        sizePolicy3.setHeightForWidth(self.DeleteBtn.sizePolicy().hasHeightForWidth())
        self.DeleteBtn.setSizePolicy(sizePolicy3)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/delete_50dp_000000_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DeleteBtn.setIcon(icon4)
        self.DeleteBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.DeleteBtn)


        self.verticalLayout_10.addWidget(self.btns)


        self.LeftSideBar.addWidget(self.Content_L)


        self.horizontalLayout_5.addWidget(self.LeftSBar)

        self.MainBar = QGroupBox(self.App)
        self.MainBar.setObjectName(u"MainBar")
        sizePolicy1.setHeightForWidth(self.MainBar.sizePolicy().hasHeightForWidth())
        self.MainBar.setSizePolicy(sizePolicy1)
        self.MainBar.setMinimumSize(QSize(0, 0))
        self.MainBar.setStyleSheet(u"#MainBar {\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.playlistWidget = QTableWidget(self.content)
        if (self.playlistWidget.columnCount() < 4):
            self.playlistWidget.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.playlistWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.playlistWidget.setObjectName(u"playlistWidget")

        self.verticalLayout_3.addWidget(self.playlistWidget)


        self.current_playlist.addWidget(self.content)


        self.Content_M.addWidget(self.crnt_playlist)

        self.control_panel = QFrame(self.Content_Main)
        self.control_panel.setObjectName(u"control_panel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.control_panel.sizePolicy().hasHeightForWidth())
        self.control_panel.setSizePolicy(sizePolicy5)
        self.control_panel.setMinimumSize(QSize(546, 92))
        self.control_panel.setMaximumSize(QSize(16777215, 100))
        self.control_panel.setStyleSheet(u"#control_panel{\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: black;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;  \n"
"    color: white;\n"
"    background-color: rgb(0, 0, 0);  \n"
"    border: none;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(0, 0, 0);  \n"
"}")
        self.horizontalLayout = QHBoxLayout(self.control_panel)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 6)
        self.verticalFrame1 = QFrame(self.control_panel)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.verticalFrame1.sizePolicy().hasHeightForWidth())
        self.verticalFrame1.setSizePolicy(sizePolicy6)
        self.verticalFrame1.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_3 = QFrame(self.verticalFrame1)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Playback_btn = QPushButton(self.horizontalFrame_3)
        self.Playback_btn.setObjectName(u"Playback_btn")
        sizePolicy3.setHeightForWidth(self.Playback_btn.sizePolicy().hasHeightForWidth())
        self.Playback_btn.setSizePolicy(sizePolicy3)
        self.Playback_btn.setMinimumSize(QSize(0, 0))
        self.Playback_btn.setMaximumSize(QSize(16777215, 16777215))
        self.Playback_btn.setAutoFillBackground(False)
        self.Playback_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icon/icons/pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Playback_btn.setIcon(icon5)
        self.Playback_btn.setIconSize(QSize(30, 30))
        self.Playback_btn.setCheckable(True)
        self.Playback_btn.setChecked(False)
        self.Playback_btn.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.Playback_btn)


        self.verticalLayout_2.addWidget(self.horizontalFrame_3)

        self.horizontalFrame1 = QFrame(self.verticalFrame1)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        sizePolicy2.setHeightForWidth(self.horizontalFrame1.sizePolicy().hasHeightForWidth())
        self.horizontalFrame1.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.CurrentTime = QLabel(self.horizontalFrame1)
        self.CurrentTime.setObjectName(u"CurrentTime")
        self.CurrentTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.CurrentTime)

        self.SeekBar = QSlider(self.horizontalFrame1)
        self.SeekBar.setObjectName(u"SeekBar")
        self.SeekBar.setMinimumSize(QSize(0, 24))
        self.SeekBar.setMaximumSize(QSize(400, 24))
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

        self.EndTime = QLabel(self.horizontalFrame1)
        self.EndTime.setObjectName(u"EndTime")
        self.EndTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.EndTime)


        self.verticalLayout_2.addWidget(self.horizontalFrame1)


        self.horizontalLayout.addWidget(self.verticalFrame1)


        self.Content_M.addWidget(self.control_panel)


        self.verticalLayout_4.addWidget(self.Content_Main)


        self.horizontalLayout_5.addWidget(self.MainBar)

        self.RightSideBar = QGroupBox(self.App)
        self.RightSideBar.setObjectName(u"RightSideBar")
        sizePolicy1.setHeightForWidth(self.RightSideBar.sizePolicy().hasHeightForWidth())
        self.RightSideBar.setSizePolicy(sizePolicy1)
        self.RightSideBar.setMinimumSize(QSize(0, 0))
        self.RightSideBar.setMaximumSize(QSize(354, 16777215))
        self.RightSideBar.setStyleSheet(u"#RightSideBar{\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}")
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
        sizePolicy3.setHeightForWidth(self.SelectSong.sizePolicy().hasHeightForWidth())
        self.SelectSong.setSizePolicy(sizePolicy3)
        self.SelectSong.setStyleSheet(u"QLabel{\n"
"	font-size: 18px;\n"
"	color: black; \n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 214, 214);\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/file_open_50dp_000000_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectAudioBtn.setIcon(icon6)
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
        self.SongInfo.setStyleSheet(u"QLabel{\n"
"	font-size: 18px;\n"
"	color: black; \n"
"}\n"
"\n"
"QTextEdit{\n"
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
        self.TrackInfo.setMinimumSize(QSize(300, 250))
        self.TrackInfo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.TrackInfo)


        self.horizontalLayout_8.addWidget(self.SongInfo)


        self.verticalLayout_5.addWidget(self.MetaData)

        self.CurrentSong = QFrame(self.Content_R)
        self.CurrentSong.setObjectName(u"CurrentSong")
        sizePolicy2.setHeightForWidth(self.CurrentSong.sizePolicy().hasHeightForWidth())
        self.CurrentSong.setSizePolicy(sizePolicy2)
        self.CurrentSong.setStyleSheet(u"QLabel{\n"
"	font-size: 18px;\n"
"	color: black; \n"
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
        self.CS = QFrame(self.CurrentSong)
        self.CS.setObjectName(u"CS")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.CS.sizePolicy().hasHeightForWidth())
        self.CS.setSizePolicy(sizePolicy7)
        self.verticalLayout_8 = QVBoxLayout(self.CS)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.crnt_sng = QFrame(self.CS)
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
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/audio_file_50dp_000000_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.CurrentFile_lb = QLabel(self.horizontalFrame_2)
        self.CurrentFile_lb.setObjectName(u"CurrentFile_lb")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.CurrentFile_lb.sizePolicy().hasHeightForWidth())
        self.CurrentFile_lb.setSizePolicy(sizePolicy8)
        self.CurrentFile_lb.setAlignment(Qt.AlignCenter)
        self.CurrentFile_lb.setIndent(0)

        self.horizontalLayout_3.addWidget(self.CurrentFile_lb)


        self.Label.addWidget(self.horizontalFrame_2)


        self.verticalLayout_8.addWidget(self.crnt_sng)

        self.frame = QFrame(self.CS)
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


        self.horizontalLayout_10.addWidget(self.CS)


        self.verticalLayout_5.addWidget(self.CurrentSong)


        self.verticalLayout_7.addWidget(self.Content_R)


        self.horizontalLayout_5.addWidget(self.RightSideBar)


        self.verticalLayout.addWidget(self.App)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ChooseFile_lb.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.SelectFile_btn.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.Copy_btn.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        ___qtablewidgetitem = self.FilesList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File", None));
        ___qtablewidgetitem1 = self.FilesList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.FilesList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Dir", None));
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.SelectAll.setText(QCoreApplication.translate("MainWindow", u" \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.DeleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem3 = self.playlistWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem4 = self.playlistWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qtablewidgetitem5 = self.playlistWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Album", None));
        ___qtablewidgetitem6 = self.playlistWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        self.Playback_btn.setText("")
        self.CurrentTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.EndTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.SelectAudioLb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b", None))
        self.SelectAudioBtn.setText("")
        self.MetaData_lb.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.TrackInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0442\u0440\u0435\u043a\u0435 \u0431\u0443\u0434\u0435\u0442 \u0442\u0443\u0442...", None))
        self.pushButton.setText("")
        self.CurrentFile_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.CurrentFile.setText("")
    # retranslateUi

