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
        MainWindow.setFixedSize(898, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.rootDir + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputURL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputURL.setGeometry(QtCore.QRect(190, 160, 681, 31))
        self.inputURL.setObjectName("inputURL")
        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(30, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.outputView = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputView.setGeometry(QtCore.QRect(380, 210, 491, 271))
        self.outputView.setAutoFillBackground(False)
        self.outputView.setDocumentTitle("")
        self.outputView.setOpenExternalLinks(True)
        self.outputView.setObjectName("outputView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 510, 491, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.screenshotCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.screenshotCheckbox.setGeometry(QtCore.QRect(60, 250, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.screenshotCheckbox.setFont(font)
        self.screenshotCheckbox.setObjectName("screenshotCheckbox")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(30, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.customBruteFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.customBruteFileButton.setGeometry(QtCore.QRect(220, 330, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.customBruteFileButton.setFont(font)
        self.customBruteFileButton.setObjectName("customBruteFileButton")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(290, 0, 371, 161))
        font = QtGui.QFont()
        font.setFamily("Parchment")
        font.setPointSize(108)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.probeCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.probeCheckbox.setGeometry(QtCore.QRect(30, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.probeCheckbox.setFont(font)
        self.probeCheckbox.setObjectName("probeCheckbox")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(180, 500, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.multithreadingCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.multithreadingCheckbox.setGeometry(QtCore.QRect(30, 370, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.multithreadingCheckbox.setFont(font)
        self.multithreadingCheckbox.setObjectName("multithreadingCheckbox")
        self.customthreadsCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customthreadsCheckbox.setGeometry(QtCore.QRect(60, 400, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customthreadsCheckbox.setFont(font)
        self.customthreadsCheckbox.setObjectName("customthreadsCheckbox")
        self.inputCustomThreads = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCustomThreads.setGeometry(QtCore.QRect(220, 400, 41, 31))
        self.inputCustomThreads.setText("")
        self.inputCustomThreads.setAlignment(QtCore.Qt.AlignCenter)
        self.inputCustomThreads.setObjectName("inputCustomThreads")
        self.bruteForceCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.bruteForceCheckbox.setGeometry(QtCore.QRect(30, 290, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bruteForceCheckbox.setFont(font)
        self.bruteForceCheckbox.setObjectName("bruteForceCheckbox")
        self.customFileCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customFileCheckbox.setGeometry(QtCore.QRect(60, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customFileCheckbox.setFont(font)
        self.customFileCheckbox.setObjectName("customFileCheckbox")
        self.chooseDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirectoryButton.setGeometry(QtCore.QRect(190, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chooseDirectoryButton.setFont(font)
        self.chooseDirectoryButton.setObjectName("chooseDirectoryButton")
        self.customDirectoryCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customDirectoryCheckbox.setGeometry(QtCore.QRect(30, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customDirectoryCheckbox.setFont(font)
        self.customDirectoryCheckbox.setObjectName("customDirectoryCheckbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 20))
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
        self.inputURL.setPlaceholderText(_translate("MainWindow", "Enter URL"))
        self.urlLabel.setText(_translate("MainWindow", "Website URL :"))
        self.outputView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.screenshotCheckbox.setText(_translate("MainWindow", "Save Subdomains Screenshot"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.customBruteFileButton.setText(_translate("MainWindow", "..."))
        self.mainLabel.setText(_translate("MainWindow", "SubShot"))
        self.probeCheckbox.setText(_translate("MainWindow", "Probe Working Domains"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.multithreadingCheckbox.setText(_translate("MainWindow", "Enable Multithreading"))
        self.customthreadsCheckbox.setText(_translate("MainWindow", "Custom Threads:"))
        self.inputCustomThreads.setText(_translate("MainWindow", "6"))
        self.bruteForceCheckbox.setText(_translate("MainWindow", "Bruteforce Subdomains"))
        self.customFileCheckbox.setText(_translate("MainWindow", "Custom input file:"))
        self.chooseDirectoryButton.setText(_translate("MainWindow", "Choose Directory"))
        self.customDirectoryCheckbox.setText(_translate("MainWindow", "Output Directory :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        self.outputView.setStyleSheet("border: 1px solid black;")
        
    
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

    ############################ Global Variables ###########################
    workingDir = os.path.dirname(os.path.realpath(__file__)) + "/"
    rootDir = os.path.dirname(os.path.realpath(__file__)) + "/"
    
    ############################ Button Functions ###########################

    def developer_btn_clicked(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("About Developer")
        self.msg.setText("SubShot is developed by yatish609@github, parvbajaj10@github, aritika2000@github \nThis tool is open-source for modifications under GPL-2.0 License.\nWe do not support or endorse any kind of illegal activities.")
        self.msg.exec_()
    
    def dir(self):
	    customDir = str(QFileDialog.getExistingDirectory())
	    self.workingDir = customDir + "/"
     
    def start_to_run(self):
        self.startButton.setStyleSheet("background-color: green")
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
                    
    def openUrl(self):
        url = QUrl('https://github.com/yatish609/SubShot')
        QDesktopServices.openUrl(url)
        
    ######################## Behavior Functions ###########################
    
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
            
    def newWorkspace(self):
        self.outputView.clear()
        self.inputURL.clear()
        self.progressBar.setProperty("value",0)
        
    def sleepTime(self, content):
        if len(content) > 10000:
            return 0.00001
        elif len(content) > 1000:
            return 0.001
        elif len(content) > 100:
            return 0.01
        else:
            return 0.1
    
    ######################## Validations ###########################
    
    def validatePath(self,path):
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
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
                int(threadcount)
                if len(threadcount) < 3:
                    return True
                else:
                    self.errorMessage('Thread count should be less than 100!')
                    return False
            except ValueError:
                self.errorMessage('Thread count should be an integer!')
                return False
        return True
    
    def errorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
    
    ######################### Main Functionality ###########################

    def rawSubDomains(self):
        url = self.inputURL.text()
        filepath = self.workingDir + "Subdomains/subdomains.txt"
        self.validatePath(filepath)
        subprocess.run("python -u " + self.rootDir + "subfinder.py -d " + url + " -o " + filepath, shell=True, stdout=subprocess.DEVNULL)
        
    def rawOutput(self):
        self.rawSubDomains()

        inputPath = self.workingDir + "Subdomains/subdomains.txt"
        self.validatePath(inputPath)
        f = open(inputPath,"r")
        content = f.readlines()
        content = [x.strip() for x in content]

        progressBarValue = 0
        progressBarIncrementCount = 100/len(content)
        delay = self.sleepTime(content)
        
        for i in content:
            self.outputView.append(i)
            progressBarValue = progressBarValue + progressBarIncrementCount
            self.progressBar.setProperty("value",progressBarValue)
            time.sleep(delay)
        
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
                subprocess.run("python -u " + self.rootDir + "prober.py -t " + threadcount + " -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
            else:
                subprocess.run("python -u " + self.rootDir + "prober.py -t 6 -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        else:
            subprocess.run("python -u " + self.rootDir + "prober.py -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        
        f.close()

        f1 = open(outputPath,"r")
        content = f1.readlines()
        content = [x.strip() for x in content]

        progressBarValue = 0
        progressBarIncrementCount = 100/len(content)
        delay = self.sleepTime(content)
        
        for i in content:
            self.outputView.append(i)
            progressBarValue = progressBarValue + progressBarIncrementCount
            self.progressBar.setProperty("value",progressBarValue)
            time.sleep(delay)
        
        f1.close()

    def runshot(self):
        # Chrome driver options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        
        # Read subdomains from file
        with open(self.workingDir + "Filtered_Subdomains/Filtered_subdomains.txt","r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        screenshotDir = self.workingDir + "images/"
        self.validatePath(screenshotDir)
        
        count = 0
        progressBarValue = 0
        progressBarIncrementCount = 100/len(content)
        delay = self.sleepTime(content)
        
        # Start screenshotting the subdomains
        for i in content:
            url = i
            driver.get(url)
            driver.save_screenshot(self.workingDir + "images/" + str(count) + ".png")
            count = count + 1
            progressBarValue = progressBarValue + progressBarIncrementCount
            self.progressBar.setProperty("value",progressBarValue)
            time.sleep(delay)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
