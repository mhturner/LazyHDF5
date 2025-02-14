# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_HdfLoad.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(845, 588)
        Dialog.setStyleSheet("font: 10pt \"Arial\";")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topHL = QtWidgets.QHBoxLayout()
        self.topHL.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.topHL.setObjectName("topHL")
        self.dataSetVL = QtWidgets.QVBoxLayout()
        self.dataSetVL.setObjectName("dataSetVL")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.dataSetVL.addWidget(self.label_1)
        self.comboBoxGroupSelect = QtWidgets.QComboBox(Dialog)
        self.comboBoxGroupSelect.setObjectName("comboBoxGroupSelect")
        self.dataSetVL.addWidget(self.comboBoxGroupSelect)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.dataSetVL.addWidget(self.label_2)
        self.listDataSet = QtWidgets.QListWidget(Dialog)
        self.listDataSet.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listDataSet.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listDataSet.setObjectName("listDataSet")
        self.dataSetVL.addWidget(self.listDataSet)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.dataSetVL.addWidget(self.label_3)
        self.filterIncludeString = QtWidgets.QLineEdit(Dialog)
        self.filterIncludeString.setObjectName("filterIncludeString")
        self.dataSetVL.addWidget(self.filterIncludeString)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.dataSetVL.addWidget(self.label_4)
        self.filterExcludeString = QtWidgets.QLineEdit(Dialog)
        self.filterExcludeString.setObjectName("filterExcludeString")
        self.dataSetVL.addWidget(self.filterExcludeString)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonFilter = QtWidgets.QPushButton(Dialog)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.pushButtonResetFilter = QtWidgets.QPushButton(Dialog)
        self.pushButtonResetFilter.setObjectName("pushButtonResetFilter")
        self.horizontalLayout.addWidget(self.pushButtonResetFilter)
        self.dataSetVL.addLayout(self.horizontalLayout)
        self.topHL.addLayout(self.dataSetVL)
        self.attribVL = QtWidgets.QVBoxLayout()
        self.attribVL.setObjectName("attribVL")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.attribVL.addWidget(self.label_5)
        self.textCurrentDataset = QtWidgets.QTextBrowser(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textCurrentDataset.sizePolicy().hasHeightForWidth())
        self.textCurrentDataset.setSizePolicy(sizePolicy)
        self.textCurrentDataset.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textCurrentDataset.setObjectName("textCurrentDataset")
        self.attribVL.addWidget(self.textCurrentDataset)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.attribVL.addWidget(self.label_6)
        self.tableAttributes = QtWidgets.QTableWidget(Dialog)
        self.tableAttributes.setStyleSheet("")
        self.tableAttributes.setColumnCount(2)
        self.tableAttributes.setObjectName("tableAttributes")
        self.tableAttributes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(121, 121, 121))
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableAttributes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(123, 123, 123))
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableAttributes.setHorizontalHeaderItem(1, item)
        self.tableAttributes.horizontalHeader().setCascadingSectionResizes(True)
        self.tableAttributes.horizontalHeader().setDefaultSectionSize(200)
        self.tableAttributes.horizontalHeader().setHighlightSections(False)
        self.tableAttributes.horizontalHeader().setSortIndicatorShown(True)
        self.tableAttributes.horizontalHeader().setStretchLastSection(True)
        self.tableAttributes.verticalHeader().setVisible(False)
        self.tableAttributes.verticalHeader().setHighlightSections(False)
        self.attribVL.addWidget(self.tableAttributes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.topHL.addLayout(self.attribVL)
        self.verticalLayout.addLayout(self.topHL)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonOk = QtWidgets.QPushButton(Dialog)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_2.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HDF File Inspector"))
        self.label_1.setText(_translate("Dialog", "Groups"))
        self.label_2.setText(_translate("Dialog", "Datasets"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Include</span> Entires with Substring (separate by \',\' [comma])</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Exclude</span> Entires with Substring (separate by \',\' [comma])</p></body></html>"))
        self.pushButtonFilter.setText(_translate("Dialog", "Filter List"))
        self.pushButtonResetFilter.setText(_translate("Dialog", "Reset List"))
        self.label_5.setText(_translate("Dialog", "Current Selection"))
        self.label_6.setText(_translate("Dialog", "Atrribute Table"))
        self.tableAttributes.setSortingEnabled(True)
        item = self.tableAttributes.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Attribute"))
        item = self.tableAttributes.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

