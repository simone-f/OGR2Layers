# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OGR2Layers.ui'
#
# Created: Fri Dec 23 00:00:56 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OGR2Layers(object):
    def setupUi(self, OGR2Layers):
        OGR2Layers.setObjectName("OGR2Layers")
        OGR2Layers.resize(567, 435)
        self.verticalLayout_3 = QtGui.QVBoxLayout(OGR2Layers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(OGR2Layers)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/plugins/OGR2Layers/icongui.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(OGR2Layers)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(OGR2Layers)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(OGR2Layers)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(OGR2Layers)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 541, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.label_29 = QtGui.QLabel(self.layoutWidget)
        self.label_29.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_10.addWidget(self.label_29)
        self.outputFormCombo = QtGui.QComboBox(self.layoutWidget)
        self.outputFormCombo.setObjectName("outputFormCombo")
        self.outputFormCombo.addItem("")
        self.outputFormCombo.addItem("")
        self.horizontalLayout_10.addWidget(self.outputFormCombo)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.LayerList = QtGui.QListWidget(self.layoutWidget)
        self.LayerList.setObjectName("LayerList")
        self.gridLayout.addWidget(self.LayerList, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setEnabled(False)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.label_30 = QtGui.QLabel(self.layoutWidget)
        self.label_30.setEnabled(False)
        self.label_30.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_11.addWidget(self.label_30)
        self.outputRasterCombo = QtGui.QComboBox(self.layoutWidget)
        self.outputRasterCombo.setEnabled(False)
        self.outputRasterCombo.setObjectName("outputRasterCombo")
        self.outputRasterCombo.addItem("")
        self.outputRasterCombo.addItem("")
        self.horizontalLayout_11.addWidget(self.outputRasterCombo)
        self.gridLayout.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kmldirpath = QtGui.QLineEdit(self.layoutWidget)
        self.kmldirpath.setObjectName("kmldirpath")
        self.horizontalLayout_3.addWidget(self.kmldirpath)
        self.browseButton = QtGui.QPushButton(self.layoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_3.addWidget(self.browseButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.RasterList = QtGui.QListWidget(self.layoutWidget)
        self.RasterList.setEnabled(False)
        self.RasterList.setObjectName("RasterList")
        self.gridLayout.addWidget(self.RasterList, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(-1, 3, 541, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.mapTitle = QtGui.QLineEdit(self.layoutWidget1)
        self.mapTitle.setObjectName("mapTitle")
        self.verticalLayout_5.addWidget(self.mapTitle)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.mapBaseLayer = QtGui.QComboBox(self.layoutWidget1)
        self.mapBaseLayer.setObjectName("mapBaseLayer")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.verticalLayout_7.addWidget(self.mapBaseLayer)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.mapSize = QtGui.QComboBox(self.layoutWidget1)
        self.mapSize.setObjectName("mapSize")
        self.mapSize.addItem("")
        self.mapSize.addItem("")
        self.mapSize.addItem("")
        self.verticalLayout_6.addWidget(self.mapSize)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtGui.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.layerSwitcherActive = QtGui.QComboBox(self.layoutWidget1)
        self.layerSwitcherActive.setObjectName("layerSwitcherActive")
        self.layerSwitcherActive.addItem("")
        self.layerSwitcherActive.addItem("")
        self.verticalLayout_8.addWidget(self.layerSwitcherActive)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_13.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_13.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_13.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_13.addWidget(self.lineEdit_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.maxExtent = QtGui.QCheckBox(self.layoutWidget1)
        self.maxExtent.setEnabled(True)
        self.maxExtent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxExtent.setObjectName("maxExtent")
        self.verticalLayout_9.addWidget(self.maxExtent)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 491, 221))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtGui.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mousepos = QtGui.QCheckBox(self.layoutWidget2)
        self.mousepos.setObjectName("mousepos")
        self.gridLayout_2.addWidget(self.mousepos, 0, 0, 1, 1)
        self.scale = QtGui.QCheckBox(self.layoutWidget2)
        self.scale.setObjectName("scale")
        self.gridLayout_2.addWidget(self.scale, 0, 1, 1, 1)
        self.copyr = QtGui.QCheckBox(self.layoutWidget2)
        self.copyr.setObjectName("copyr")
        self.gridLayout_2.addWidget(self.copyr, 0, 2, 1, 1)
        self.zoomBar = QtGui.QCheckBox(self.layoutWidget2)
        self.zoomBar.setObjectName("zoomBar")
        self.gridLayout_2.addWidget(self.zoomBar, 1, 0, 1, 1)
        self.navi = QtGui.QCheckBox(self.layoutWidget2)
        self.navi.setObjectName("navi")
        self.gridLayout_2.addWidget(self.navi, 1, 1, 1, 1)
        self.permalink = QtGui.QCheckBox(self.layoutWidget2)
        self.permalink.setObjectName("permalink")
        self.gridLayout_2.addWidget(self.permalink, 1, 2, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_12)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.defaultRender = QtGui.QRadioButton(self.groupBox)
        self.defaultRender.setObjectName("defaultRender")
        self.horizontalLayout_14.addWidget(self.defaultRender)
        self.qgisRender = QtGui.QRadioButton(self.groupBox)
        self.qgisRender.setEnabled(True)
        self.qgisRender.setObjectName("qgisRender")
        self.horizontalLayout_14.addWidget(self.qgisRender)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 360, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.query = QtGui.QRadioButton(self.layoutWidget3)
        self.query.setObjectName("query")
        self.horizontalLayout_15.addWidget(self.query)
        self.query_2 = QtGui.QRadioButton(self.layoutWidget3)
        self.query_2.setEnabled(True)
        self.query_2.setObjectName("query_2")
        self.horizontalLayout_15.addWidget(self.query_2)
        self.query_3 = QtGui.QRadioButton(self.layoutWidget3)
        self.query_3.setObjectName("query_3")
        self.horizontalLayout_15.addWidget(self.query_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget4 = QtGui.QWidget(self.tab_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 541, 281))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtGui.QLabel(self.layoutWidget4)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.textBrowserLayer = QtGui.QTextBrowser(self.layoutWidget4)
        self.textBrowserLayer.setObjectName("textBrowserLayer")
        self.verticalLayout_11.addWidget(self.textBrowserLayer)
        self.label_14 = QtGui.QLabel(self.layoutWidget4)
        self.label_14.setEnabled(False)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_11.addWidget(self.label_14)
        self.textBrowserRaster = QtGui.QTextBrowser(self.layoutWidget4)
        self.textBrowserRaster.setEnabled(False)
        self.textBrowserRaster.setObjectName("textBrowserRaster")
        self.verticalLayout_11.addWidget(self.textBrowserRaster)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtGui.QProgressBar(OGR2Layers)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(OGR2Layers)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.helpButton = QtGui.QPushButton(OGR2Layers)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_2.addWidget(self.helpButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(OGR2Layers)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), OGR2Layers.reject)
        QtCore.QMetaObject.connectSlotsByName(OGR2Layers)

    def retranslateUi(self, OGR2Layers):
        OGR2Layers.setWindowTitle(QtGui.QApplication.translate("OGR2Layers", "OGR2Layers Plugin: Export to OpenLayers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OGR2Layers", "OGR2Layers Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OGR2Layers", "This plugin will export active OGR layers to an OpenLayers HTML Map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OGR2Layers", "Be careful, the heavier OGR Layers are, the slower the OL Map will be !", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OGR2Layers", "OGR active layers :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("OGR2Layers", "OGR output format", None, QtGui.QApplication.UnicodeUTF8))
        self.outputFormCombo.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "GeoJSON", None, QtGui.QApplication.UnicodeUTF8))
        self.outputFormCombo.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "GML", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("OGR2Layers", "GDAL active layers :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("OGR2Layers", "GDAL output format", None, QtGui.QApplication.UnicodeUTF8))
        self.outputRasterCombo.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "PNG", None, QtGui.QApplication.UnicodeUTF8))
        self.outputRasterCombo.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "JPEG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OGR2Layers", "Output directory", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("OGR2Layers", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("OGR2Layers", "QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("OGR2Layers", "Map Title :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OGR2Layers", "Map Base Layer :", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (Mapnik)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (OSMarender)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(2, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (Cycleway)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(3, QtGui.QApplication.translate("OGR2Layers", "OpenLayers WMS", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(4, QtGui.QApplication.translate("OGR2Layers", "Google Streets", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(5, QtGui.QApplication.translate("OGR2Layers", "Google Physical", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(6, QtGui.QApplication.translate("OGR2Layers", "Google Hybrid", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(7, QtGui.QApplication.translate("OGR2Layers", "Google Satellite", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(8, QtGui.QApplication.translate("OGR2Layers", "Demis WMS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("OGR2Layers", "Map Size :", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "400 x 400", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "800 x 600", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(2, QtGui.QApplication.translate("OGR2Layers", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("OGR2Layers", "Layer Switcher active ?", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSwitcherActive.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSwitcherActive.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "no", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("OGR2Layers", "Default Map Extent :", None, QtGui.QApplication.UnicodeUTF8))
        self.maxExtent.setText(QtGui.QApplication.translate("OGR2Layers", "Click here if you want use this bounding box as max extent of the map", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("OGR2Layers", "OpenLayers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("OGR2Layers", "Choose other map controls", None, QtGui.QApplication.UnicodeUTF8))
        self.mousepos.setText(QtGui.QApplication.translate("OGR2Layers", "mouseposition", None, QtGui.QApplication.UnicodeUTF8))
        self.scale.setText(QtGui.QApplication.translate("OGR2Layers", "scale bar", None, QtGui.QApplication.UnicodeUTF8))
        self.copyr.setText(QtGui.QApplication.translate("OGR2Layers", "attribution", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomBar.setText(QtGui.QApplication.translate("OGR2Layers", "panZoomBar", None, QtGui.QApplication.UnicodeUTF8))
        self.navi.setText(QtGui.QApplication.translate("OGR2Layers", "overview map", None, QtGui.QApplication.UnicodeUTF8))
        self.permalink.setText(QtGui.QApplication.translate("OGR2Layers", "permalink", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("OGR2Layers", "Render option", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultRender.setText(QtGui.QApplication.translate("OGR2Layers", "default OpenLayers render", None, QtGui.QApplication.UnicodeUTF8))
        self.qgisRender.setText(QtGui.QApplication.translate("OGR2Layers", "QGIS render", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("OGR2Layers", "Query option", None, QtGui.QApplication.UnicodeUTF8))
        self.query.setText(QtGui.QApplication.translate("OGR2Layers", "query one feature", None, QtGui.QApplication.UnicodeUTF8))
        self.query_2.setText(QtGui.QApplication.translate("OGR2Layers", "query more features ", None, QtGui.QApplication.UnicodeUTF8))
        self.query_3.setText(QtGui.QApplication.translate("OGR2Layers", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("OGR2Layers", "Optional", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("OGR2Layers", "Vector proiection trasformation information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("OGR2Layers", "Raster proiection trasformation information", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("OGR2Layers", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setText(QtGui.QApplication.translate("OGR2Layers", "About - Help", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
