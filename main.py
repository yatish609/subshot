from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from takeover import Ui_takeoverWindow
import os,webbrowser, time, subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re, platform, errno


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_takeoverWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        text_file = open(self.rootDir + "Hostile" + self.slash + "url.txt", "w+")
        text_file.write(self.inputURL.text())
        text_file.close()
        self.ui.takeoverOutput()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(922, 712)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.rootDir + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputURL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputURL.setGeometry(QtCore.QRect(200, 160, 691, 31))
        self.inputURL.setObjectName("inputURL")
        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(30, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.outputView = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputView.setGeometry(QtCore.QRect(400, 210, 491, 311))
        self.outputView.setObjectName("outputView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(400, 560, 501, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.screenshotCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.screenshotCheckbox.setGeometry(QtCore.QRect(60, 280, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.screenshotCheckbox.setFont(font)
        self.screenshotCheckbox.setObjectName("screenshotCheckbox")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(30, 540, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(330, 0, 371, 161))
        font = QtGui.QFont()
        font.setFamily("Parchment")
        font.setPointSize(50)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.probeCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.probeCheckbox.setGeometry(QtCore.QRect(40, 220, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.probeCheckbox.setFont(font)
        self.probeCheckbox.setObjectName("probeCheckbox")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(190, 540, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.multithreadingCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.multithreadingCheckbox.setGeometry(QtCore.QRect(40, 330, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.multithreadingCheckbox.setFont(font)
        self.multithreadingCheckbox.setObjectName("multithreadingCheckbox")
        self.customthreadsCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customthreadsCheckbox.setGeometry(QtCore.QRect(60, 380, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customthreadsCheckbox.setFont(font)
        self.customthreadsCheckbox.setObjectName("customthreadsCheckbox")
        self.inputCustomThreads = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCustomThreads.setGeometry(QtCore.QRect(230, 380, 41, 31))
        self.inputCustomThreads.setText("")
        self.inputCustomThreads.setAlignment(QtCore.Qt.AlignCenter)
        self.inputCustomThreads.setObjectName("inputCustomThreads")
        self.chooseDirectoryCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.chooseDirectoryCheckbox.setGeometry(QtCore.QRect(60, 490, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chooseDirectoryCheckbox.setFont(font)
        self.chooseDirectoryCheckbox.setObjectName("chooseDirectoryCheckbox")
        self.chooseDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirectoryButton.setGeometry(QtCore.QRect(230, 490, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.chooseDirectoryButton.setFont(font)
        self.chooseDirectoryButton.setObjectName("chooseDirectoryButton")
        self.customDirectoryCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.customDirectoryCheckbox.setGeometry(QtCore.QRect(40, 440, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customDirectoryCheckbox.setFont(font)
        self.customDirectoryCheckbox.setObjectName("customDirectoryCheckbox")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 610, 301, 48))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 26))
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
        self.commandLinkButton.setEnabled(False)

        ### Connecting Buttons with respective functions

        self.startButton.clicked.connect(self.startClicked)
        self.actionNew.triggered.connect(self.newWorkspace)
        self.actionExit.triggered.connect(sys.exit)
        self.menuAbout.triggered.connect(self.developer_btn_clicked)
        self.actionGitHub.triggered.connect(self.openUrl)
        self.chooseDirectoryButton.clicked.connect(self.dir)
        self.clearButton.clicked.connect(self.newWorkspace)
        self.commandLinkButton.clicked.connect(self.openWindow)


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
        self.mainLabel.setText(_translate("MainWindow", "SubShot"))
        self.probeCheckbox.setText(_translate("MainWindow", "Probe Working Domains"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.multithreadingCheckbox.setText(_translate("MainWindow", "Enable Multithreading"))
        self.customthreadsCheckbox.setText(_translate("MainWindow", "Custom Threads:"))
        self.chooseDirectoryCheckbox.setText(_translate("MainWindow", "Choose Directory"))
        self.chooseDirectoryButton.setText(_translate("MainWindow", "..."))
        self.customDirectoryCheckbox.setText(_translate("MainWindow", "Custom Directory"))
        self.commandLinkButton.setText(_translate("MainWindow", "Check Takeover Possibility"))
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

    ############################ Global Variables ###########################
        
    slash = "\\" if platform.system()=="Windows" else "/"
    workingDir = os.path.dirname(os.path.realpath(__file__)) + slash
    rootDir = os.path.dirname(os.path.realpath(__file__)) + slash
    customBruteFileDir = ""
    
    ############################ Button Functions ###########################

    def developer_btn_clicked(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("About")
        self.msg.setText("SubShot is developed under GPL-2.0 License.")
        self.msg.exec_()
    
    def dir(self):
	    customDir = str(QFileDialog.getExistingDirectory())
	    self.workingDir = customDir + self.slash
    
    def getcustomBruteFileDir(self):
        customDir = str(QFileDialog.getExistingDirectory())
        self.customBruteFileDir = customDir + self.slash
    
    def start_to_run(self):
        self.startButton.setStyleSheet("background-color: green")
        self.startButton.setText("Running")

    def run_to_start(self):
        self.commandLinkButton.setEnabled(True)
        self.startButton.setStyleSheet("")
        self.startButton.setText("Start")
       
        
    def startClicked(self):
        self.outputView.clear()
        self.progressBar.setFormat('%p%')
        self.progressBar.setProperty("value",0)
        
        ## Validations
        if self.validateURL():
            if self.validateThreadCount():
                self.start_to_run()
                
                if self.probeCheckbox.isChecked():
                    self.progressBar.setFormat('Probing - %p%')
                    self.probedOutput()
                    if self.screenshotCheckbox.isChecked():
                        self.progressBar.setFormat('Screenshotting - %p%') 
                        self.runshot()
                    self.run_to_start()
                    self.progressBar.setFormat('Done!')  
                else:
                    self.progressBar.setFormat('Scanning - %p%')
                    self.rawOutput()
                    self.run_to_start()
                    self.progressBar.setFormat('Done!')
                    
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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat('%p%')
        
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
        filepath = self.workingDir + "Subdomains" + self.slash + "subdomains.txt"
        self.validatePath(filepath)
        subprocess.run("python3 -u " + self.rootDir + "subfinder.py -d " + url + " -o " + filepath, shell=True, stdout=subprocess.DEVNULL)
           
    
    def rawOutput(self):
        self.rawSubDomains()

        inputPath = self.workingDir + "Subdomains" + self.slash + "subdomains.txt"
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

        inputPath = self.workingDir + "Subdomains" + self.slash + "subdomains.txt"
        self.validatePath(inputPath)
        f = open(inputPath,"r")
        outputPath = self.workingDir + "Filtered_Subdomains" + self.slash + "Filtered_subdomains.txt"
        self.validatePath(outputPath)
        if self.multithreadingCheckbox.isChecked():
            if self.customthreadsCheckbox.isChecked():
                threadcount = self.inputCustomThreads.text()
                subprocess.run("python3 -u " + self.rootDir + "prober.py -t " + threadcount + " -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
            else:
                subprocess.run("python3 -u " + self.rootDir + "prober.py -t 6 -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        else:
            subprocess.run("python3 -u " + self.rootDir + "prober.py -f " + inputPath + " -s 200,301 -o " + outputPath, shell=True, stdout=subprocess.DEVNULL)
        
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
        with open(self.workingDir + "Filtered_Subdomains" + self.slash + "Filtered_subdomains.txt","r") as f:
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
            driver.save_screenshot(self.workingDir + "images" + self.slash + str(count) + ".png")
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

