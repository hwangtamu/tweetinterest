# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IrProjectDemo.ui'
#
# Created: Sat Apr 27 14:27:26 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import account_to_news
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(691, 616)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 20, 71, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Search = QtGui.QLineEdit(Dialog)
        self.Search.setGeometry(QtCore.QRect(110, 20, 311, 21))
        self.Search.setObjectName(_fromUtf8("Search"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(350, 80, 301, 471))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 80, 301, 471))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 60, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(480, 60, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(160, 570, 491, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 570, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.connect(self.pushButton,SIGNAL("clicked()"),self.run)
        self.retranslateUi(Dialog)
		
		#pic
        '''
        #jpeg=QtGui.QPixmap(self).scaled(Dialog.size())
		#jpeg.load("./2.jpg")
        self.palette1 = QtGui.QPalette(Dialog)
        self.palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./2.jpg").scaled(Dialog.size()))
        self.widget = QtGui.QWidget(Dialog)
        #self.widget = setGeometry(QtCore.QRect(0, 0, 691, 616))
        self.widget.setPalette(self.palette1);
        self.widget.setAutoFillBackground(True)
        '''
        #self.setPixmap(QPixmap('./1.jpg'));
        #self.setStyleSheet("QLabel {font-size : 1600px; color : blue;}");
        '''
        pic = QtGui.QLabel(Dialog)
        pic.setGeometry(0, 0, 691, 616)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "./1.jpg"))
        '''
        #Dialog.palette().background().setColor(Qt.blue)
        '''
        self.background_pixmap = './1.jpg'
        painter = QPainter()
        #painter.begin(self.viewport())
        painter.drawPixmap(0, 0, 691, 616, self.background_pixmap)
        '''
        QtCore.QMetaObject.connectSlotsByName(Dialog)
		
    def run(self):
		text = self.Search.text()
		news_list,interest_list,tweet_string=account_to_news.account_to_news(str(text))
		news_str = account_to_news.news_result(news_list)
		interest_str = account_to_news.interest_result(interest_list)
		if len(news_str) == 0:
			news_str = 'Sorry! You don\'t have specific interest!'
		if len(interest_str) == 0:
			interest_str = 'Hey! You need to show your interest in tweet!'
		self.textBrowser_3.setText(tweet_string)
		self.textBrowser_2.setText(str(news_str))
		self.textBrowser.setText(str(interest_str))
		
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Small Fresh", None))
        self.pushButton.setText(_translate("Dialog", "Search", None))
        self.label.setText(_translate("Dialog", " Tweet", None))
        self.label_2.setText(_translate("Dialog", "News", None))
        self.label_3.setText(_translate("Dialog", "Interests", None))

