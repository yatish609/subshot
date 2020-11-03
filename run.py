from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import os,webbrowser, time, subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(790, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.rootDir + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputURL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputURL.setGeometry(QtCore.QRect(200, 160, 561, 31))
        self.inputURL.setObjectName("inputURL")
        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(30, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.outputView = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputView.setGeometry(QtCore.QRect(30, 390, 731, 201))
        self.outputView.setObjectName("outputView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 350, 731, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.screenshotCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.screenshotCheckbox.setGeometry(QtCore.QRect(50, 250, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.screenshotCheckbox.setFont(font)
        self.screenshotCheckbox.setObjectName("screenshotCheckbox")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(630, 210, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.chooseDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirectoryButton.setGeometry(QtCore.QRect(520, 210, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.chooseDirectoryButton.setFont(font)
        self.chooseDirectoryButton.setObjectName("chooseDirectoryButton")
        self.customDirectoryCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customDirectoryCheckbox.setGeometry(QtCore.QRect(340, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customDirectoryCheckbox.setFont(font)
        self.customDirectoryCheckbox.setObjectName("customDirectoryCheckbox")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(230, 0, 371, 161))
        font = QtGui.QFont()
        font.setFamily("Parchment")
        font.setPointSize(108)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.probeCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.probeCheckbox.setGeometry(QtCore.QRect(30, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.probeCheckbox.setFont(font)
        self.probeCheckbox.setObjectName("probeCheckbox")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(630, 280, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.multithreadingCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.multithreadingCheckbox.setGeometry(QtCore.QRect(30, 280, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.multithreadingCheckbox.setFont(font)
        self.multithreadingCheckbox.setObjectName("multithreadingCheckbox")
        self.customthreadsCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customthreadsCheckbox.setGeometry(QtCore.QRect(50, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customthreadsCheckbox.setFont(font)
        self.customthreadsCheckbox.setObjectName("customthreadsCheckbox")
        self.inputCustomThreads = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCustomThreads.setGeometry(QtCore.QRect(210, 310, 41, 31))
        self.inputCustomThreads.setAlignment(QtCore.Qt.AlignCenter)
        self.inputCustomThreads.setObjectName("inputCustomThreads")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        self.actionGitHub.setObjectName("actionGitHub")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuAbout.addAction(self.actionGitHub)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ### Custom Modifications

        self.chooseDirectoryButton.setEnabled(False)
        self.customthreadsCheckbox.setEnabled(False)
        self.screenshotCheckbox.setEnabled(False)
        self.inputCustomThreads.setEnabled(False)

        ### Connecting Buttons with respective functions

        self.startButton.clicked.connect(self.startClicked)
        self.actionNew.triggered.connect(self.newWorkspace)
        self.actionExit.triggered.connect(sys.exit)
        self.actionDeveloper.triggered.connect(self.developer_btn_clicked)
        self.actionGitHub.triggered.connect(self.openUrl)
        self.chooseDirectoryButton.clicked.connect(self.dir)
        self.clearButton.clicked.connect(self.newWorkspace)


        ### State Changed Actions
        self.customDirectoryCheckbox.stateChanged.connect(self.customDirectoryCheckboxChanged)
        self.multithreadingCheckbox.stateChanged.connect(self.multithreadingCheckboxChanged)
        self.probeCheckbox.stateChanged.connect(self.probeCheckboxChanged)
        self.customthreadsCheckbox.stateChanged.connect(self.customthreadsCheckboxChanged)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SubShot"))
        self.urlLabel.setText(_translate("MainWindow", "Website URL:"))
        self.screenshotCheckbox.setText(_translate("MainWindow", "Save Subdomains Screenshot"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.chooseDirectoryButton.setText(_translate("MainWindow", "..."))
        self.customDirectoryCheckbox.setText(_translate("MainWindow", "Custom Directory :"))
        self.mainLabel.setText(_translate("MainWindow", "SubShot"))
        self.probeCheckbox.setText(_translate("MainWindow", "Probe Working Domains"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.multithreadingCheckbox.setText(_translate("MainWindow", "Enable Multithreading"))
        self.customthreadsCheckbox.setText(_translate("MainWindow", "Custom Threads:"))
        self.inputCustomThreads.setText(_translate("MainWindow", "6"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

    workingDir = os.path.dirname(os.path.realpath(__file__)) + "/"
    rootDir = os.path.dirname(os.path.realpath(__file__)) + "/"

    def developer_btn_clicked(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("About Developer")
        self.msg.setText("SubShot is developed by yatish609@github, parvbajaj10@github, aritika2000@github \nThis tool is open-source for modifications under GPL-2.0 License.\nWe do not support or endorse any kind of illegal activities.")
        self.msg.exec_()
    
    def dir(self):
	    customDir = str(QFileDialog.getExistingDirectory())
	    self.workingDir = customDir + "/"

    def openUrl(self):
        url = QUrl('https://github.com/yatish609/SubShot')
        QDesktopServices.openUrl(url)
    
    def newWorkspace(self):
        self.outputView.clear()
        self.inputURL.clear()
        self.progressBar.setProperty("value",0)

    def rawSubDomains(self):
        url = self.inputURL.text()
        filepath = self.workingDir + "Subdomains/subdomains.txt"
        self.validatePath(filepath)
        subprocess.run("python -u " + self.rootDir + "subfinder.py -d " + url + " -o " + filepath, shell=True, stdout=subprocess.DEVNULL)

    def validatePath(self,path):
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
    def errorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
                
    def validateURL(self):
        if self.inputURL.text()== "":
            self.errorMessage('URL can not be blank')
            return False
        
        if "." not in self.inputURL.text():
            self.errorMessage('Enter a valid URL!')
            return False
        
        regex = re.compile('[@_!#$^*()<>|}{~]')
        
        if(regex.search(self.inputURL.text()) == None):
            return True
        else:
            self.errorMessage('URL should not contain special characters!')
            return False
                    
    def validateThreadCount(self):
        if self.customthreadsCheckbox.isChecked():
            try: 
                threadcount = self.inputCustomThreads.text()
                a = int(threadcount)
                if len(threadcount) < 3:
                    return True
                else:
                    self.errorMessage('Thread count should be less than 100!')
                    return False
            except ValueError:
                self.errorMessage('Thread count should be an integer!')
                return False
        return True
    
    def rawOutput(self):
        self.rawSubDomains()

        inputPath = self.workingDir + "Subdomains/subdomains.txt"
        self.validatePath(inputPath)
        f = open(inputPath,"r")
        content = f.readlines()
        content = [x.strip() for x in content]

        count = 0
        x = 100/len(content)
        
        for i in content:
            self.outputView.append(i)
            count = count + x
            if count <= 99:
                self.progressBar.setProperty("value",count)
                if len(content) > 10000:
                    time.sleep(0.00001)
                elif len(content) > 1000:
                    time.sleep(0.001)
                elif len(content) > 100:
                    time.sleep(0.01)
                else:
                    time.sleep(0.1)
        
        count = 100
        self.progressBar.setProperty("value",count)
        f.close()
        self.run_to_start()

    def probedOutput(self):
        self.rawSubDomains()

        inputPath = self.workingDir + "Subdomains/subdomains.txt"
        self.validatePath(inputPath)
        f = open(inputPath,"r")
        outputPath = self.workingDir + "Filtered_Subdomains/Filtered_subdomains.txt"
        self.validatePath(outputPath)
        if self.multithreadingCheckbox.isChecked():
            if self.customthreadsCheckbox.isChecked():
                threadcount = self.inputCustomThreads.text()
                subprocess.run("python -u " + self.workingDir + "prober.py -t " + threadcount + " -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
            else:
                subprocess.run("python -u " + self.workingDir + "prober.py -t 6 -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        else:
            subprocess.run("python -u " + self.workingDir + "prober.py -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        
        f.close()

        f1 = open(outputPath,"r")
        content = f1.readlines()
        content = [x.strip() for x in content]

        count = 0
        x = 100/len(content)
        
        for i in content:
            self.outputView.append(i)
            count = count + x
            if count <= 99:
                self.progressBar.setProperty("value",count)
                if len(content) > 10000:
                    time.sleep(0.00001)
                elif len(content) > 1000:
                    time.sleep(0.001)
                elif len(content) > 100:
                    time.sleep(0.01)
                else:
                    time.sleep(0.1)
        
        count = 100
        self.progressBar.setProperty("value",count)
        f1.close()

        
    def customDirectoryCheckboxChanged(self):
        if self.customDirectoryCheckbox.isChecked():
            self.chooseDirectoryButton.setEnabled(True)
        else:
            self.workingDir = self.rootDir
            self.chooseDirectoryButton.setEnabled(False)

    def multithreadingCheckboxChanged(self):
        if self.multithreadingCheckbox.isChecked():
            self.customthreadsCheckbox.setEnabled(True)
        else:
            self.customthreadsCheckbox.setEnabled(False)

    def probeCheckboxChanged(self):
        if self.probeCheckbox.isChecked():
            self.screenshotCheckbox.setEnabled(True)
        else:
            self.screenshotCheckbox.setEnabled(False)

    def customthreadsCheckboxChanged(self):
        if self.customthreadsCheckbox.isChecked():
            self.inputCustomThreads.setEnabled(True)
        else:
            self.inputCustomThreads.setEnabled(False)

    def runshot(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

        with open(self.workingDir + "Filtered_Subdomains/Filtered_subdomains.txt","r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        count = 0
        screenshotDir = self.workingDir + "images/"
        self.validatePath(screenshotDir)
        for i in content:
            url = i
            driver.get(url)
            driver.save_screenshot(self.workingDir + "images/" + str(count) + ".png")
            count = count + 1

    def start_to_run(self):
        self.startButton.setStyleSheet("background-color: green; border:none")
        self.startButton.setText("Running")

    def run_to_start(self):
        self.startButton.setStyleSheet("")
        self.startButton.setText("Start")

    def startClicked(self):
        self.outputView.clear()
        self.progressBar.setProperty("value",0)
        
        ## Validations
        if self.validateURL():
            if self.validateThreadCount():
                self.start_to_run()
                
                if self.probeCheckbox.isChecked():
                    self.probedOutput()
                    if self.screenshotCheckbox.isChecked():
                        self.runshot()
                    self.run_to_start()
                else:
                    self.rawOutput()
                    self.run_to_start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
