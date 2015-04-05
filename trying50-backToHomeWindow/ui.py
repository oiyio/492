# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Dec 22 03:46:19 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from cache_search import *
from functools import partial
import apt
import sys
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(945, 592)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(945, 592))
        #MainWindow.setMaximumSize(QtCore.QSize(945, 592))
	self.history = []
        self.index = -1
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

##search icin lineedit'e girilen text field##
        self.search = QtGui.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(820, 0, 113, 27))
        self.search.setObjectName(_fromUtf8("search"))
        self.HasEverInvokedPushButtonOK = 0  ##sadece ilk giriste ekrani temizlemek icin
        self.search.returnPressed.connect(self.pushButtonOK)
#############################################



        self.createFramesCategoryAndTopRated(1)




        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 0, 41, 27))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.backButton.setEnabled(False)
        self.backButton.clicked.connect(self.goBack)

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(50, 0, 41, 27))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.nextButton.setEnabled(False)
        self.nextButton.clicked.connect(self.goNext)

        self.backToMain = QtGui.QPushButton(self.centralwidget)
        self.backToMain.setGeometry(QtCore.QRect(90, 0, 41, 27))
        self.backToMain.setObjectName(_fromUtf8("backToMain"))
        self.backToMain.setEnabled(True)
	#self.ui2 = Ui_MainWindow()
        #self.backToMain.clicked.connect(MainWindow.setupUi(self))
	#self.backToMain.clicked.connect(self.setupUi(self,MainWindow))
	self.backToMain.clicked.connect( partial( self.setupUi, MainWindow=MainWindow) )        
#self.backToMain.clicked.connect( partial( self.createFramesCategoryAndTopRated, isThisFirstCreation=0) )
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    



    def createFramesCategoryAndTopRated(self,isThisFirstCreation):
        print "inside createFramesCategoryAndTopRated "
	#solda category'leri icermesi icin bir frame create ediliyor#
        self.category_frame = QtGui.QFrame(self.centralwidget)
        self.category_frame.setGeometry(QtCore.QRect(10, 30, 201, 501))
        self.category_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.category_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.category_frame.setObjectName(_fromUtf8("category_frame"))

	##yukarida category frame create edilmisti, burada bu frame icine verticalLayoutWidget isimli bir widget ekliyoruz
        self.verticalLayoutWidget = QtGui.QWidget(self.category_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 501)) ##frame'in (0,0) koordinatindan baslayacak widgetimiz.
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget")) #widget'in object name'i veriliyor.

	##verticalLaoyoutWidget'e, category_list isimli widget'i ekliyoruz.
        self.category_list = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.category_list.setMargin(0)
        self.category_list.setObjectName(_fromUtf8("category_list")) ## object'e isim verdik.

	######vertical layout widget'i icindeki category_list widget'ine push button'lar ekliyoruz#####
        self.category_label = QtGui.QLabel(self.verticalLayoutWidget) ## verticalLayout widget'imize bir isim-label-veriyoruz.
        self.category_label.setAlignment(QtCore.Qt.AlignCenter) ## bu label'i ortaliyoruz
        self.category_label.setObjectName(_fromUtf8("category_label")) # label'a object ismini veriyoruz.
        self.category_list.addWidget(self.category_label) # category_list'e ,category_label'i ekliyoruz.
        self.accessories = QtGui.QPushButton(self.verticalLayoutWidget)
        self.accessories.setObjectName(_fromUtf8("accessories"))
        self.category_list.addWidget(self.accessories)
        self.books_mags = QtGui.QPushButton(self.verticalLayoutWidget)
        self.books_mags.setObjectName(_fromUtf8("books_mags"))
        self.category_list.addWidget(self.books_mags)
        self.dev_tools = QtGui.QPushButton(self.verticalLayoutWidget)
        self.dev_tools.setObjectName(_fromUtf8("dev_tools"))
        self.category_list.addWidget(self.dev_tools)
        self.education = QtGui.QPushButton(self.verticalLayoutWidget)
        self.education.setObjectName(_fromUtf8("education"))
        self.category_list.addWidget(self.education)
        self.fonts = QtGui.QPushButton(self.verticalLayoutWidget)
        self.fonts.setObjectName(_fromUtf8("fonts"))
        self.category_list.addWidget(self.fonts)
        self.games = QtGui.QPushButton(self.verticalLayoutWidget)
        self.games.setObjectName(_fromUtf8("games"))
        self.category_list.addWidget(self.games)
        self.graphics = QtGui.QPushButton(self.verticalLayoutWidget)
        self.graphics.setObjectName(_fromUtf8("graphics"))
        self.category_list.addWidget(self.graphics)
        self.internet = QtGui.QPushButton(self.verticalLayoutWidget)
        self.internet.setObjectName(_fromUtf8("internet"))
        self.category_list.addWidget(self.internet)
        self.office = QtGui.QPushButton(self.verticalLayoutWidget)
        self.office.setObjectName(_fromUtf8("office"))
        self.category_list.addWidget(self.office)
        self.science_eng = QtGui.QPushButton(self.verticalLayoutWidget)
        self.science_eng.setObjectName(_fromUtf8("science_eng"))
        self.category_list.addWidget(self.science_eng)
        self.sound_video = QtGui.QPushButton(self.verticalLayoutWidget)
        self.sound_video.setObjectName(_fromUtf8("sound_video"))
        self.category_list.addWidget(self.sound_video)
        self.system = QtGui.QPushButton(self.verticalLayoutWidget)
        self.system.setObjectName(_fromUtf8("system"))
        self.category_list.addWidget(self.system)


	if isThisFirstCreation:
        ### search sonucunda cikan text'leri koyacagimiz frame'i create ediyoruz burada ###
		self.app_frame = QtGui.QFrame(self.centralwidget)
		self.app_frame.setGeometry(QtCore.QRect(230, 30, 701, 101))
		self.app_frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.app_frame.setFrameShadow(QtGui.QFrame.Raised)
		self.app_frame.setObjectName(_fromUtf8("app_frame"))

		self.verticalLayoutWidget_2 = QtGui.QWidget(self.app_frame)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 741, 501))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))

		self.app_list = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.app_list.setMargin(0)
		self.app_list.setObjectName(_fromUtf8("app_list"))

		self.app_names = QtGui.QTextEdit(self.verticalLayoutWidget_2)
		self.app_names.setObjectName(_fromUtf8("app_names"))
		self.app_list.addWidget(self.app_names)
		### search sonucunda cikan text'leri koyacagimiz frame'i create ediyoruz burada ###

	###top-rated apps'lari buraya koyacagiz , install remove islemleri yapilabilecek ####################
        self.topRatedAppsFrame=QtGui.QFrame(self.centralwidget)
        self.topRatedAppsFrame.setGeometry(QtCore.QRect(230, 150, 701, 101))
        self.topRatedAppsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topRatedAppsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.topRatedAppsFrame.setObjectName(_fromUtf8("topRatedAppsFrame"))

        self.horFortopRatedApps = QtGui.QWidget(self.topRatedAppsFrame)
        self.horFortopRatedApps.setGeometry(QtCore.QRect(0, 0, 450, 100))
        self.horFortopRatedApps.setObjectName(_fromUtf8("horFortopRatedApps"))

        self.topRatedAppsList = QtGui.QGridLayout(self.horFortopRatedApps)
        self.topRatedAppsList.setMargin(1)
        self.topRatedAppsList.setObjectName(_fromUtf8("topRatedAppsList"))

        self.createPushButtonsForTopRatedApps(0)

    def retranslateUi(self, MainWindow):
###### tum object'lere text giriyorum ######
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.search.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.category_label.setText(_translate("MainWindow", "CATEGORIES", None))
        self.accessories.setText(_translate("MainWindow", "Accessories", None))
        self.books_mags.setText(_translate("MainWindow", "Books && Magazines", None))
        self.dev_tools.setText(_translate("MainWindow", "Developer Tools", None))
        self.education.setText(_translate("MainWindow", "Education", None))
        self.fonts.setText(_translate("MainWindow", "Fonts", None))
        self.games.setText(_translate("MainWindow", "Games", None))
        self.graphics.setText(_translate("MainWindow", "Graphics", None))
        self.internet.setText(_translate("MainWindow", "Internet", None))
        self.office.setText(_translate("MainWindow", "Office", None))
        self.science_eng.setText(_translate("MainWindow", "Science && Engineering", None))
        self.sound_video.setText(_translate("MainWindow", "Sound && Video", None))
        self.system.setText(_translate("MainWindow", "System", None))

      
        #self.app3Icon.setText(_translate("MainWindow", "app3Icon", None))
        self.backButton.setText(_translate("MainWindow", "Back", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.backToMain.setText(_translate("MainWindow", "Home", None))


#yeni bir uygulama eklemek icin yapilmasi gereken 3 sey var. icon'un adresini girmek,button'a settext ile yazi girmek ve
#pkg_name_param'a ilgili parametreyi vermek     
    def createPushButtonsForTopRatedApps(self,deleteButtonsInsRem):

        if (deleteButtonsInsRem == 1) :
            self.clearPushButtonsInstallRemoveAndBack()

        self.app1 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app1.setObjectName(_fromUtf8("app1"))
        self.app1.setIcon(QtGui.QIcon("iconsOfApps/kwordquiz.png"))
        self.app1.setIconSize(QtCore.QSize(36,36))
        self.app1.setText(_translate("MainWindow", "kwordquiz", None))
        self.app1.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='kwordquiz') )
        self.topRatedAppsList.addWidget(self.app1,0,0)

        self.app2 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app2.setObjectName(_fromUtf8("app2"))
        self.app2.setIcon(QtGui.QIcon("iconsOfApps/geany.png"))
        self.app2.setIconSize(QtCore.QSize(36,36))
        self.app2.setText(_translate("MainWindow", "Geany", None))
        self.app2.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='geany') )
        self.topRatedAppsList.addWidget(self.app2,0,1)

        self.app3 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app3.setObjectName(_fromUtf8("app3"))
        self.app3.setIcon(QtGui.QIcon("iconsOfApps/vlcmediaplayer.png"))
        self.app3.setIconSize(QtCore.QSize(36,36))
        self.app3.setText(_translate("MainWindow", "VLC media\n player", None))
        self.app3.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='vlc') )
        self.topRatedAppsList.addWidget(self.app3,0,2)

        self.app4 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app4.setObjectName(_fromUtf8("app4"))
        self.app4.setIcon(QtGui.QIcon("iconsOfApps/filezilla.png"))
        self.app4.setIconSize(QtCore.QSize(36,36))
        self.app4.setText(_translate("MainWindow", "Filezilla", None))
        self.app4.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='filezilla') )
        self.topRatedAppsList.addWidget(self.app4,1,0)

        self.app5 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app5.setObjectName(_fromUtf8("app5"))
        self.app5.setIcon(QtGui.QIcon("iconsOfApps/drpython.png"))
        self.app5.setIconSize(QtCore.QSize(36,36))
        self.app5.setText(_translate("MainWindow", "DrPython", None))
        self.app5.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='drpython') )
        self.topRatedAppsList.addWidget(self.app5,1,1)

        self.app6 = QtGui.QPushButton(self.horFortopRatedApps)
        self.app6.setObjectName(_fromUtf8("app6"))
        self.app6.setIcon(QtGui.QIcon("iconsOfApps/ninja-ide.png"))
        self.app6.setIconSize(QtCore.QSize(36,36))
        self.app6.setText(_translate("MainWindow", "Ninja IDE", None))
        self.app6.clicked.connect( partial( self.createPushButtonsInstallAndRemove, pkg_name_param='ninja-ide') )
        self.topRatedAppsList.addWidget(self.app6,1,2)

    def createPushButtonsInstallAndRemove(self,pkg_name_param):
        self.clearTopRatedArea()

        installName = "Install " + pkg_name_param
        removeName = "Remove " + pkg_name_param

        self.installPushButton = QtGui.QPushButton(self.horFortopRatedApps)
        self.installPushButton.setObjectName(_fromUtf8("installPushButton"))
        self.installPushButton.clicked.connect( partial( self.installPackage, pkg_name=pkg_name_param) )
        self.installPushButton.setText(_translate("MainWindow", installName, None))
        self.topRatedAppsList.addWidget(self.installPushButton,0,0)

        self.removePushButton = QtGui.QPushButton(self.horFortopRatedApps)
        self.removePushButton.setObjectName(_fromUtf8("removePushButton"))
        self.removePushButton.clicked.connect( partial( self.removePackage, pkg_name=pkg_name_param) )
        self.removePushButton.setText(_translate("MainWindow", removeName, None))
        self.topRatedAppsList.addWidget(self.removePushButton,0,1)

        self.backToTopRatedAppsButton = QtGui.QPushButton(self.horFortopRatedApps)
        self.backToTopRatedAppsButton.setObjectName(_fromUtf8("backToTopRatedAppsButton"))
        self.backToTopRatedAppsButton.clicked.connect( partial( self.createPushButtonsForTopRatedApps,deleteButtonsInsRem=1) )
        self.backToTopRatedAppsButton.setText(_translate("MainWindow", "Back to to top rated apps", None))
        self.topRatedAppsList.addWidget(self.backToTopRatedAppsButton,0,2)


    def clearTopRatedArea(self):
        self.topRatedAppsList.removeWidget(self.app1)
        self.app1.deleteLater()
        self.app1 = None
        self.topRatedAppsList.removeWidget(self.app2)
        self.app2.deleteLater()
        self.app2 = None 
        self.topRatedAppsList.removeWidget(self.app3)
        self.app3.deleteLater()
        self.app3 = None 
        self.topRatedAppsList.removeWidget(self.app4)
        self.app4.deleteLater()
        self.app4 = None
        self.topRatedAppsList.removeWidget(self.app5)
        self.app5.deleteLater()
        self.app5 = None
        self.topRatedAppsList.removeWidget(self.app6)
        self.app6.deleteLater()
        self.app6 = None

    def clearPushButtonsInstallRemoveAndBack(self):
        self.topRatedAppsList.removeWidget(self.installPushButton)
        self.installPushButton.deleteLater()
        self.installPushButton = None
        self.topRatedAppsList.removeWidget(self.removePushButton)
        self.removePushButton.deleteLater()
        self.removePushButton = None 
        self.topRatedAppsList.removeWidget(self.backToTopRatedAppsButton)
        self.backToTopRatedAppsButton.deleteLater()
        self.backToTopRatedAppsButton = None

#####################installation of a package############################
    def installPackage(self,pkg_name):

        cache = apt.cache.Cache()
        cache.update()   # error is in this line

        pkg = cache[pkg_name]
        if pkg.is_installed:
            print "{pkg_name} is already installed. Invalid request! ".format(pkg_name=pkg_name)
        else:
            print "{pkg_name} is not installed".format(pkg_name=pkg_name)
            print "Now you are installing ..."
            print pkg.section
            pkg.mark_install()

            try:
                cache.commit()
            except Exception, arg:
                print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
            print "DONE."
#####################################################################    
        
#####################removal of a package############################
    def removePackage(self,pkg_name):

        cache = apt.cache.Cache()
        cache.update()   # error is in this line

        pkg = cache[pkg_name]
        if pkg.is_installed:
            print "{pkg_name} already installed".format(pkg_name=pkg_name)
            print "Now you are deleting ..."
            pkg.mark_delete()

            try:
                cache.commit()
            except Exception, arg:
                print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
            print "DONE."

        else:
            print "{pkg_name} is not installed. Invalid request!".format(pkg_name=pkg_name)
#####################################################################             


    def pushButtonOK(self):

        if (self.HasEverInvokedPushButtonOK == 0):
        
		self.clearTopRatedArea()
		self.topRatedAppsList.deleteLater()
		self.topRatedAppsList = None
		self.horFortopRatedApps.deleteLater()
		self.horFortopRatedApps = None
		self.topRatedAppsFrame.deleteLater()
		self.topRatedAppsFrame = None



		self.category_frame.deleteLater()
		self.category_frame = None





		self.app_frame.setGeometry(QtCore.QRect(130, 30, 701, 101))

                self.HasEverInvokedPushButtonOK = self.HasEverInvokedPushButtonOK + 1

        


        key = self.search.text()  # search alanina girilen kelime
        self.history.append(str(key)) # 
        self.index = self.index + 1
        if len(self.history) == 2:
            self.backButton.setEnabled(True)
        call_sh(str(key))  #call_sh function(inside cache_search.py) is called. It calls : system("./cache_search.sh " + key)
        parse_file(str(key)) 
        f_names = open('name_list.txt', 'r')
        matches = ''

        for line in f_names:
            matches = matches+'\n' +line

        if matches == '': self.app_names.setText('Aradiginiz Uygulama Bulunamamaktadir')
        else: self.app_names.setText(matches)
        f_names.close()
        open("cache_list.txt", "w").close()
        open("name_list.txt", "w").close()
        open("other_list.txt", "w").close()

    def goBack(self):
        key = self.history[self.index-1]
        self.index = self.index - 1
        if(self.index == 0):
            self.backButton.setEnabled(False)
        if len(self.history) - 1 > self.index:
            self.nextButton.setEnabled(True)
        call_sh(str(key))
        parse_file(str(key))
        f_names = open('name_list.txt', 'r')
        matches = ''

        for line in f_names:
            matches = matches+'\n' +line

        if matches == '': self.app_names.setText('Aradiginiz Uygulama Bulunamamaktadir')
        else: self.app_names.setText(matches)
        f_names.close()
        open("cache_list.txt", "w").close()
        open("name_list.txt", "w").close()
        open("other_list.txt", "w").close()

    def goNext(self):
        
        key = self.history[self.index+1]
        self.index = self.index + 1
        if(self.index == len(self.history) -1):
            self.nextButton.setEnabled(False)
        if(self.index >= 0):
            self.backButton.setEnabled(True)
        call_sh(str(key))
        parse_file(str(key))
        f_names = open('name_list.txt', 'r')
        matches = ''

        for line in f_names:
            matches = matches+'\n' +line

        if matches == '': self.app_names.setText('Aradiginiz Uygulama Bulunamamaktadir')
        else: self.app_names.setText(matches)
        f_names.close()
        open("cache_list.txt", "w").close()
        open("name_list.txt", "w").close()
        open("other_list.txt", "w").close()

