import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from modules import setupActions
import os
import json
import signal

class Window(QWidget):
    def __init__(self):
        super().__init__()
       
        self.UI()
    

    def UI(self):
        if(self.__checkConfig()):
            runFileDirectory = self.__readConfig()
            os.system("gnome-terminal -- sudo {};read line".format(runFileDirectory))
            exit(0)       
            
        else:
            
            message ="To run this application, you need to add the .run file for xampp in the next step.\n\nClick 'Ok' to continue\nClick 'Cancel' to exit setup"
            msgBox = QMessageBox.information(self,
                                            "Setup",
                                            message,
                                            buttons= QMessageBox.Ok | QMessageBox.Cancel,defaultButton=QMessageBox.Ok
                                            )
            if(msgBox == QMessageBox.Cancel):
                sys.exit(None)
            elif(msgBox == QMessageBox.Ok):
                #UI initial setup / initial layout declarations
                self.setWindowTitle("xamp_launcher")
                self.setGeometry(50,50,400,300)
                self.setMinimumHeight(200)
                self.setMinimumWidth(400)
                self.setMaximumWidth(500)
                self.setMaximumHeight(350)
                mainLayout = QVBoxLayout()
                topLayout = QHBoxLayout()
                middleLayout = QHBoxLayout()
                bottomLayout = QHBoxLayout()
                mainLayout.addLayout(topLayout)
                mainLayout.addLayout(middleLayout)

                #controls
                self.feedback = QLabel("SUCCESS...Next time you run this application, xampp will launch.")
                self.feedback.setWordWrap(True)
                self.feedback.hide()
                self.instructions = QLabel("Add xampp .run file path below.")
                self.pathInput = QLineEdit(".run file location")
                self.pathInput.setMinimumWidth(360)
                self.pathInput.setDisabled(True)
                self.addButton = QPushButton("...")
                self.cancelButton = QPushButton("Cancel")
                self.finalizeButton = QPushButton("Finalize")
                self.importantLabel = QLabel("IMPORTANT")
                self.importantLabel.setStyleSheet("color:#e35f5f;font-weight:bold;text-decoration:underline;font-family:serif;")
                self.warning = QLabel("Make sure the file path is correct before you 'Finalize', otherwise this application does not guarantee proper behavior.")
                self.warning.setWordWrap(True)
               

                #layout
                topLayout.addWidget(self.instructions)
                middleLayout.addWidget(self.pathInput)
                middleLayout.addWidget(self.addButton)
                middleLayout.addStretch()
                mainLayout.addWidget(self.importantLabel)
                mainLayout.addWidget(self.warning)
                mainLayout.addStretch()
                mainLayout.addWidget(self.feedback)
                mainLayout.addStretch()
                bottomLayout.addStretch()
                bottomLayout.addWidget(self.cancelButton)
                bottomLayout.addWidget(self.finalizeButton)
                mainLayout.addLayout(bottomLayout)
                

                #signals and slots
                self.addButton.clicked.connect(lambda: setupActions.addButtonCLicked(self))
                self.cancelButton.clicked.connect(lambda: setupActions.cancelButtonClicked(self))
                self.finalizeButton.clicked.connect(lambda: setupActions.finalizeButtonClicked(self,appctxt))

                self.setLayout(mainLayout)
                self.show()

               
    def __checkConfig(self):
        #check the config.json file and see if there is a value.  If this is the first time, then the value should be empty
        runFile = None
        try:
            runFile = json.load(open(appctxt.get_resource('config/config.json')))
        except Exception as error:#this is where we need to add some error logging
            print(error)

        else:
            #check if the file is empty
            if(len(runFile['runFile'])==0):
                return False
            elif(len(runFile['runFile'])>0):
                #validate that this path is a .run file
                if(self.validRunFile(runFile['runFile'])):
                    return True
                else:
                    #show a message and error log
                    return False
            


    #this is the only check it will run, its up to the user to select the right run file
    def validRunFile(self,filePath):
        return filePath.endswith('.run')

    def __readConfig(self):
        runPath = None
        with open(appctxt.get_resource('config/config.json'),'r') as r_file:
            #read the data from the file 
            data = r_file.read()
            dataDictionary = json.loads(data)
            runPath = dataDictionary['runFile']

        return runPath
   

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)