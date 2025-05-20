# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QListView, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
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
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size: 14px;\n"
"	\n"
"}")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
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
        self.App.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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
        self.header_pm.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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

        self.horizontalLayout_6.addWidget(self.favicon)

        self.mediateka_lb = QLabel(self.title_pm)
        self.mediateka_lb.setObjectName(u"mediateka_lb")
        sizePolicy2.setHeightForWidth(self.mediateka_lb.sizePolicy().hasHeightForWidth())
        self.mediateka_lb.setSizePolicy(sizePolicy2)
        self.mediateka_lb.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.mediateka_lb)


        self.horizontalLayout_4.addWidget(self.title_pm, 0, Qt.AlignmentFlag.AlignLeft)

        self.header_btn = QFrame(self.header_pm)
        self.header_btn.setObjectName(u"header_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_btn.sizePolicy().hasHeightForWidth())
        self.header_btn.setSizePolicy(sizePolicy3)
        self.header_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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


        self.horizontalLayout_4.addWidget(self.header_btn)


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


        self.verticalLayout_10.addWidget(self.switch_mode, 0, Qt.AlignmentFlag.AlignLeft)

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
        self.playlist_manager.setFrameShape(QFrame.Shape.NoFrame)
        self.playlist_manager.setLineWidth(1)
        self.playlist_manager.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playlist_manager.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.playlist_manager.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.playlist_manager.setIconSize(QSize(48, 48))
        self.playlist_manager.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.playlist_manager.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.playlist_manager.setSpacing(5)
        self.playlist_manager.setViewMode(QListView.ViewMode.ListMode)
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
        self.MainBar.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"}\n"
"\n"
"#MainBar {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	color: white;\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"	padding-top: 0px;\n"
"	padding-bottom: 10px;    \n"
"}\n"
"\n"
"#playlist_Widget{\n"
"	border: none;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
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
"    qproperty-wordWrap: false; /* \u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u0441\u043b\u043e\u0432 */\n"
"    qproperty-indent: 0; /* \u041e\u0442\u0441\u0442\u0443\u043f \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    qproperty-margi"
                        "n: 0; /* \u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"")
        self.MainBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.MainBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.MainBar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u043b\u043e\u0441\u0430 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 \u0432 \u0441\u0442\u0438\u043b\u0435 Spotify */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #121212; /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043a\u0430\u043a \u0432 Spotify */\n"
"    width: 10px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"/* \u0421\u043b\u0430\u0439\u0434\u0435\u0440 (handle) \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar::handle:vertical {\n"
"    background: #535353; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u043a\u0430\u043a \u0443 \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"    min-he"
                        "ight: 30px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 handle */\n"
"    max-height: 40px;\n"
"    border-radius: 5px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"/* \u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #686868; /* \u0421\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #1DB954; /* \u0417\u0435\u043b\u0435\u043d\u044b\u0439 Spotify \u043f\u0440\u0438 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u043c \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0438 */\n"
""
                        "}\n"
"\n"
"/* \u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0438 \u043d\u0438\u0436\u043d\u044f\u044f \u043a\u043d\u043e\u043f\u043a\u0438 (\u0441\u0442\u0440\u0435\u043b\u043a\u0438) - \u0441\u043a\u0440\u044b\u0432\u0430\u0435\u043c */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e \u0441\u0432\u0435\u0440\u0445\u0443 \u0438 \u0441\u043d\u0438\u0437\u0443 */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u043b\u043e\u0441\u0430 - \u0441\u043a\u0440\u044b\u0432\u0430\u0435\u043c */\n"
"QScrollBar:horizontal {\n"
"    height: 0px;\n"
"}")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 608, 594))
        self.scroll_widget.setStyleSheet(u"#scroll_widget {\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.playlist_frame = QFrame(self.scroll_widget)
        self.playlist_frame.setObjectName(u"playlist_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.playlist_frame.sizePolicy().hasHeightForWidth())
        self.playlist_frame.setSizePolicy(sizePolicy4)
        self.playlist_frame.setStyleSheet(u"")
        self.p = QVBoxLayout(self.playlist_frame)
        self.p.setSpacing(5)
        self.p.setObjectName(u"p")
        self.p.setContentsMargins(0, 0, 0, 0)
        self.main_top_frame = QFrame(self.playlist_frame)
        self.main_top_frame.setObjectName(u"main_top_frame")
        sizePolicy2.setHeightForWidth(self.main_top_frame.sizePolicy().hasHeightForWidth())
        self.main_top_frame.setSizePolicy(sizePolicy2)
        self.main_top_frame.setMinimumSize(QSize(0, 200))
        self.main_top_frame.setMaximumSize(QSize(16777215, 200))
        self.main_top_frame.setStyleSheet(u"#main_top_frame{\n"
"	border: 1px solid white;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 52px;\n"
"}")
        self.playlist_cover = QVBoxLayout(self.main_top_frame)
        self.playlist_cover.setSpacing(0)
        self.playlist_cover.setObjectName(u"playlist_cover")
        self.playlist_cover.setContentsMargins(0, 0, 0, 0)
        self.main_top = QFrame(self.main_top_frame)
        self.main_top.setObjectName(u"main_top")
        self.main_top.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.main_top)
        self.horizontalLayout_15.setSpacing(8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.playlist_cov = QLabel(self.main_top)
        self.playlist_cov.setObjectName(u"playlist_cov")
        sizePolicy3.setHeightForWidth(self.playlist_cov.sizePolicy().hasHeightForWidth())
        self.playlist_cov.setSizePolicy(sizePolicy3)
        self.playlist_cov.setMinimumSize(QSize(130, 130))
        self.playlist_cov.setPixmap(QPixmap(u":/icon/icons/music_info.png"))
        self.playlist_cov.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.playlist_cov)

        self.playlist_name = QLabel(self.main_top)
        self.playlist_name.setObjectName(u"playlist_name")
        font = QFont()
        font.setFamilies([u"Onest ExtraBold"])
        font.setWeight(QFont.ExtraBold)
        self.playlist_name.setFont(font)

        self.horizontalLayout_15.addWidget(self.playlist_name)


        self.playlist_cover.addWidget(self.main_top)


        self.p.addWidget(self.main_top_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.list_control = QFrame(self.playlist_frame)
        self.list_control.setObjectName(u"list_control")
        sizePolicy2.setHeightForWidth(self.list_control.sizePolicy().hasHeightForWidth())
        self.list_control.setSizePolicy(sizePolicy2)
        self.list_control.setMinimumSize(QSize(0, 52))
        self.list_control.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.list_control.setStyleSheet(u"#list_control{\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding-: 0px;\n"
"	margin: 0px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#sort_list:hover, #shuffle_btn_list:hover{\n"
"    background-color: rgba(56, 56, 56, 240); \n"
"}")
        self.l = QHBoxLayout(self.list_control)
        self.l.setSpacing(0)
        self.l.setObjectName(u"l")
        self.l.setContentsMargins(0, 5, 0, 0)
        self.playback_controls = QFrame(self.list_control)
        self.playback_controls.setObjectName(u"playback_controls")
        sizePolicy3.setHeightForWidth(self.playback_controls.sizePolicy().hasHeightForWidth())
        self.playback_controls.setSizePolicy(sizePolicy3)
        self.playback_controls.setMinimumSize(QSize(0, 0))
        self.playback_controls.setStyleSheet(u"")
        self.horizontalLayout_19 = QHBoxLayout(self.playback_controls)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.playback_btn_list = QPushButton(self.playback_controls)
        self.playback_btn_list.setObjectName(u"playback_btn_list")
        sizePolicy3.setHeightForWidth(self.playback_btn_list.sizePolicy().hasHeightForWidth())
        self.playback_btn_list.setSizePolicy(sizePolicy3)
        self.playback_btn_list.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/play_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icon/icons/pause_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.playback_btn_list.setIcon(icon1)
        self.playback_btn_list.setIconSize(QSize(60, 60))
        self.playback_btn_list.setCheckable(True)

        self.horizontalLayout_19.addWidget(self.playback_btn_list)

        self.shuffle_btn_list = QPushButton(self.playback_controls)
        self.shuffle_btn_list.setObjectName(u"shuffle_btn_list")
        sizePolicy3.setHeightForWidth(self.shuffle_btn_list.sizePolicy().hasHeightForWidth())
        self.shuffle_btn_list.setSizePolicy(sizePolicy3)
        self.shuffle_btn_list.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"D:/Downloads/shuffle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffle_btn_list.setIcon(icon2)
        self.shuffle_btn_list.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.shuffle_btn_list)


        self.l.addWidget(self.playback_controls, 0, Qt.AlignmentFlag.AlignLeft)

        self.list_params = QFrame(self.list_control)
        self.list_params.setObjectName(u"list_params")
        sizePolicy3.setHeightForWidth(self.list_params.sizePolicy().hasHeightForWidth())
        self.list_params.setSizePolicy(sizePolicy3)
        self.list_params.setMinimumSize(QSize(0, 50))
        self.list_params.setStyleSheet(u"QComboBox{\n"
"	font: 700 10pt \"Onest\";\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.list_params)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.add_music_btn = QPushButton(self.list_params)
        self.add_music_btn.setObjectName(u"add_music_btn")
        sizePolicy3.setHeightForWidth(self.add_music_btn.sizePolicy().hasHeightForWidth())
        self.add_music_btn.setSizePolicy(sizePolicy3)
        self.add_music_btn.setMinimumSize(QSize(0, 0))
        self.add_music_btn.setMaximumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_music_btn.setIcon(icon3)
        self.add_music_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_16.addWidget(self.add_music_btn)

        self.sort_list = QPushButton(self.list_params)
        self.sort_list.setObjectName(u"sort_list")
        sizePolicy3.setHeightForWidth(self.sort_list.sizePolicy().hasHeightForWidth())
        self.sort_list.setSizePolicy(sizePolicy3)
        self.sort_list.setMaximumSize(QSize(30, 30))
        self.sort_list.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/sort-desc.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icon/icons/sort-asc.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.sort_list.setIcon(icon4)
        self.sort_list.setIconSize(QSize(30, 30))
        self.sort_list.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.sort_list)


        self.l.addWidget(self.list_params, 0, Qt.AlignmentFlag.AlignRight)


        self.p.addWidget(self.list_control, 0, Qt.AlignmentFlag.AlignTop)

        self.playlist_widget_frame = QFrame(self.playlist_frame)
        self.playlist_widget_frame.setObjectName(u"playlist_widget_frame")
        sizePolicy2.setHeightForWidth(self.playlist_widget_frame.sizePolicy().hasHeightForWidth())
        self.playlist_widget_frame.setSizePolicy(sizePolicy2)
        self.verticalLayout_18 = QVBoxLayout(self.playlist_widget_frame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.playlist_Widget = QTableWidget(self.playlist_widget_frame)
        if (self.playlist_Widget.columnCount() < 3):
            self.playlist_Widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.playlist_Widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.playlist_Widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.playlist_Widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.playlist_Widget.setObjectName(u"playlist_Widget")
        sizePolicy2.setHeightForWidth(self.playlist_Widget.sizePolicy().hasHeightForWidth())
        self.playlist_Widget.setSizePolicy(sizePolicy2)
        self.playlist_Widget.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Onest ExtraBold"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.playlist_Widget.setFont(font1)
        self.playlist_Widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.playlist_Widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.playlist_Widget.setAutoFillBackground(False)
        self.playlist_Widget.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QTableWidget {\n"
"    background-color: rgb(18, 18, 18);\n"
"    color: white;\n"
"    gridline-color: rgba(255, 255, 255, 30%);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0435 \u043b\u0438\u043d\u0438\u0438 */\n"
"	border: none;\n"
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
"    border-bottom: 1px"
                        " solid rgba(255, 255, 255, 20%);\n"
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
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"/* \u0423\u0433\u043b\u043e\u0432\u043e\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 */\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(18, 18, 18);\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 20%);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u044f\u0447\u0435\u0435\u043a *"
                        "/\n"
"QTableWidget::item {\n"
"    padding: 8px 15px;\n"
"}\n"
"\n"
"/* \u0412\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255, 255, 255, 10%);\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u043e\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 */\n"
"QTableWidget::item:focus {\n"
"    outline: none;\n"
"}")
        self.playlist_Widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playlist_Widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playlist_Widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.playlist_Widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.playlist_Widget.setTabKeyNavigation(False)
        self.playlist_Widget.setProperty(u"showDropIndicator", False)
        self.playlist_Widget.setDragDropOverwriteMode(False)
        self.playlist_Widget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.playlist_Widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.playlist_Widget.setIconSize(QSize(0, 0))
        self.playlist_Widget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.playlist_Widget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.playlist_Widget.setShowGrid(False)
        self.playlist_Widget.setGridStyle(Qt.PenStyle.NoPen)
        self.playlist_Widget.setSortingEnabled(False)
        self.playlist_Widget.setWordWrap(True)
        self.playlist_Widget.setCornerButtonEnabled(True)
        self.playlist_Widget.setRowCount(0)
        self.playlist_Widget.setColumnCount(3)
        self.playlist_Widget.horizontalHeader().setVisible(True)
        self.playlist_Widget.horizontalHeader().setMinimumSectionSize(50)
        self.playlist_Widget.horizontalHeader().setDefaultSectionSize(160)
        self.playlist_Widget.horizontalHeader().setStretchLastSection(True)
        self.playlist_Widget.verticalHeader().setMinimumSectionSize(30)
        self.playlist_Widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_18.addWidget(self.playlist_Widget, 0, Qt.AlignmentFlag.AlignTop)


        self.p.addWidget(self.playlist_widget_frame)


        self.verticalLayout_20.addWidget(self.playlist_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scroll_widget)

        self.verticalLayout_4.addWidget(self.scrollArea)


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
        self.RightSideBar.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.RightSideBar.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.RightSideBar)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Content_R = QFrame(self.RightSideBar)
        self.Content_R.setObjectName(u"Content_R")
        sizePolicy1.setHeightForWidth(self.Content_R.sizePolicy().hasHeightForWidth())
        self.Content_R.setSizePolicy(sizePolicy1)
        self.Content_R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/file_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SelectAudioBtn.setIcon(icon5)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.song_lb.sizePolicy().hasHeightForWidth())
        self.song_lb.setSizePolicy(sizePolicy5)
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
        self.horizontalFrame_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalFrame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/audio_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.CurrentFile_lb = QLabel(self.horizontalFrame_2)
        self.CurrentFile_lb.setObjectName(u"CurrentFile_lb")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.CurrentFile_lb.sizePolicy().hasHeightForWidth())
        self.CurrentFile_lb.setSizePolicy(sizePolicy6)
        self.CurrentFile_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.CurrentFile.setWordWrap(False)

        self.CurrentSong_name.addWidget(self.CurrentFile)


        self.verticalLayout_8.addWidget(self.frame)


        self.horizontalLayout_10.addWidget(self.song_lb)


        self.verticalLayout_5.addWidget(self.CurrentSong)


        self.verticalLayout_7.addWidget(self.Content_R)


        self.horizontalLayout_5.addWidget(self.RightSideBar)


        self.verticalLayout.addWidget(self.App)

        self.Playback = QGroupBox(self.centralwidget)
        self.Playback.setObjectName(u"Playback")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Playback.sizePolicy().hasHeightForWidth())
        self.Playback.setSizePolicy(sizePolicy7)
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
        self.control_panel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
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
        self.right_panel = QFrame(self.control_panel)
        self.right_panel.setObjectName(u"right_panel")
        self.right_panel.setMinimumSize(QSize(350, 0))
        self.right_panel.setMaximumSize(QSize(350, 16777215))
        self.right_panel.setStyleSheet(u"QLabel{\n"
"    font-family: \"Onest ExtraBold\";\n"
"    font-weight: 800; /* Extra Bold */\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.right_panel)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(self.right_panel)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.horizontalFrame.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.volume_settings = QFrame(self.horizontalFrame)
        self.volume_settings.setObjectName(u"volume_settings")
        sizePolicy3.setHeightForWidth(self.volume_settings.sizePolicy().hasHeightForWidth())
        self.volume_settings.setSizePolicy(sizePolicy3)
        self.volume_settings.setStyleSheet(u"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0433\u043e QSlider (\u0433\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c) \u043a\u0430\u043a \u0432 Spotify */\n"
"QSlider {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"}\n"
"\n"
"/* \u0424\u043e\u043d\u043e\u0432\u0430\u044f \u0434\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    background: #535353;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u0434\u043e\u0440\u043e\u0436\u043a\u0438 */\n"
"QSlider::sub-page:horizontal {\n"
"    height: 4px;\n"
"    background: #FFF; \n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* \u041c\u0435\u043d\u044f\u0435\u0442 \u0446\u0432\u0435\u0442 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442"
                        "\u0438\u0438 */\n"
"QSlider::sub-page:horizontal:hover {\n"
"    background: #1DB954;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e) */\n"
"QSlider::handle:horizontal {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -4px 0;  /* \u0446\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438 */\n"
"    background: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 */\n"
"QSlider:disabled {\n"
"    opacity: 0.3;\n"
"}")
        self.vol = QHBoxLayout(self.volume_settings)
        self.vol.setSpacing(10)
        self.vol.setObjectName(u"vol")
        self.vol.setContentsMargins(0, 0, 0, 0)
        self.volume_slider = QSlider(self.volume_settings)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy)
        self.volume_slider.setMinimumSize(QSize(100, 24))
        self.volume_slider.setMaximumSize(QSize(16777215, 24))
        self.volume_slider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.volume_slider.setValue(99)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.vol.addWidget(self.volume_slider)

        self.vol_icon = QLabel(self.volume_settings)
        self.vol_icon.setObjectName(u"vol_icon")
        self.vol_icon.setMinimumSize(QSize(0, 0))
        self.vol_icon.setMaximumSize(QSize(35, 35))
        self.vol_icon.setPixmap(QPixmap(u":/icon/icons/volume_up.svg"))
        self.vol_icon.setScaledContents(True)
        self.vol_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vol.addWidget(self.vol_icon)


        self.horizontalLayout_11.addWidget(self.volume_settings)


        self.verticalLayout_14.addWidget(self.horizontalFrame)


        self.horizontalLayout.addWidget(self.right_panel)

        self.playback_panel = QFrame(self.control_panel)
        self.playback_panel.setObjectName(u"playback_panel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.playback_panel.sizePolicy().hasHeightForWidth())
        self.playback_panel.setSizePolicy(sizePolicy8)
        self.playback_panel.setMinimumSize(QSize(580, 0))
        self.playback_panel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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
"    color: white;\n"
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
        sizePolicy3.setHeightForWidth(self.dj.sizePolicy().hasHeightForWidth())
        self.dj.setSizePolicy(sizePolicy3)
        self.horizontalLayout_12 = QHBoxLayout(self.dj)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.skip_previous = QPushButton(self.dj)
        self.skip_previous.setObjectName(u"skip_previous")
        sizePolicy3.setHeightForWidth(self.skip_previous.sizePolicy().hasHeightForWidth())
        self.skip_previous.setSizePolicy(sizePolicy3)
        self.skip_previous.setMinimumSize(QSize(30, 30))
        self.skip_previous.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/skip_previous.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.skip_previous.setIcon(icon7)
        self.skip_previous.setIconSize(QSize(45, 45))

        self.horizontalLayout_12.addWidget(self.skip_previous)

        self.playback_btn = QPushButton(self.dj)
        self.playback_btn.setObjectName(u"playback_btn")
        sizePolicy3.setHeightForWidth(self.playback_btn.sizePolicy().hasHeightForWidth())
        self.playback_btn.setSizePolicy(sizePolicy3)
        self.playback_btn.setMinimumSize(QSize(45, 45))
        self.playback_btn.setMaximumSize(QSize(45, 45))
        self.playback_btn.setAutoFillBackground(False)
        self.playback_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icon/icons/pause1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.playback_btn.setIcon(icon8)
        self.playback_btn.setIconSize(QSize(35, 35))
        self.playback_btn.setCheckable(True)
        self.playback_btn.setChecked(False)
        self.playback_btn.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.playback_btn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.skip_next = QPushButton(self.dj)
        self.skip_next.setObjectName(u"skip_next")
        sizePolicy3.setHeightForWidth(self.skip_next.sizePolicy().hasHeightForWidth())
        self.skip_next.setSizePolicy(sizePolicy3)
        self.skip_next.setMinimumSize(QSize(30, 30))
        self.skip_next.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/skip_next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.skip_next.setIcon(icon9)
        self.skip_next.setIconSize(QSize(45, 45))

        self.horizontalLayout_12.addWidget(self.skip_next)


        self.verticalLayout_2.addWidget(self.dj, 0, Qt.AlignmentFlag.AlignHCenter)

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
        self.CurrentTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.SeekBar.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_13.addWidget(self.SeekBar)

        self.EndTime = QLabel(self.slider)
        self.EndTime.setObjectName(u"EndTime")
        sizePolicy3.setHeightForWidth(self.EndTime.sizePolicy().hasHeightForWidth())
        self.EndTime.setSizePolicy(sizePolicy3)
        self.EndTime.setTextFormat(Qt.TextFormat.AutoText)
        self.EndTime.setScaledContents(False)
        self.EndTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.EndTime)


        self.verticalLayout_2.addWidget(self.slider)


        self.horizontalLayout.addWidget(self.playback_panel)

        self.left_panel = QFrame(self.control_panel)
        self.left_panel.setObjectName(u"left_panel")
        sizePolicy8.setHeightForWidth(self.left_panel.sizePolicy().hasHeightForWidth())
        self.left_panel.setSizePolicy(sizePolicy8)
        self.left_panel.setMinimumSize(QSize(350, 0))
        self.left_panel.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.left_panel)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.left_panel)


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
        self.playlist_cov.setText("")
        self.playlist_name.setText(QCoreApplication.translate("MainWindow", u"\u041b\u044e\u0431\u0438\u043c\u044b\u0435 \u0442\u0440\u0435\u043a\u0438", None))
        self.playback_btn_list.setText("")
        self.shuffle_btn_list.setText("")
        self.add_music_btn.setText("")
        self.sort_list.setText("")
        ___qtablewidgetitem = self.playlist_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.playlist_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0431\u043e\u043c", None));
        ___qtablewidgetitem2 = self.playlist_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None));
        self.SelectAudioLb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b", None))
        self.SelectAudioBtn.setText("")
        self.MetaData_lb.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.TrackInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0442\u0440\u0435\u043a\u0435 \u0431\u0443\u0434\u0435\u0442 \u0442\u0443\u0442...", None))
        self.pushButton.setText("")
        self.CurrentFile_lb.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.CurrentFile.setText("")
        self.vol_icon.setText("")
        self.skip_previous.setText("")
        self.skip_next.setText("")
        self.CurrentTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.EndTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
    # retranslateUi

