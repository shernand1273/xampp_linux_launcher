#xampp_launcher links a dockable and executable icon to the xampp .run file
#     Copyright (C) 2020, Steven Hernandez
#     This file is part of xampp_launcher.

#     xampp_launcher is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     xampp_launcher is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from modules import setupActions
import os
import json
import signal
from modules import eulaDialog as ed

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.eulaAccepted = self.checkEula()
        if(self.eulaAccepted):
            self.UI()
        else:
            ed.openEula(self,appctxt)

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
                self.addButton.clicked.connect(lambda: setupActions.addButtonCLicked(self))
                self.cancelButton.clicked.connect(lambda: setupActions.cancelButtonClicked(self))
                self.finalizeButton.clicked.connect(lambda: setupActions.finalizeButtonClicked(self,appctxt))
                self.setLayout(mainLayout)
                self.show()

               
    def __checkConfig(self):
        runFile = None
        try:
            runFile = json.load(open(appctxt.get_resource('config/config.json')))
        except Exception as error:
            print(error)

        else:
            if(len(runFile['runFile'])==0):
                return False
            elif(len(runFile['runFile'])>0):
                if(self.validRunFile(runFile['runFile'])):
                    return True
                else:
                    return False
            

    def validRunFile(self,filePath):
        return filePath.endswith('.run')

    def __readConfig(self):
        runPath = None
        with open(appctxt.get_resource('config/config.json'),'r') as r_file:
            data = r_file.read()
            dataDictionary = json.loads(data)
            runPath = dataDictionary['runFile']

        return runPath

    def checkEula(self):
        import json
        with open(appctxt.get_resource('config/config.json'),'r')as r_file:
            data = r_file.read()
            dataDict = json.loads(data)
            return dataDict['Eula']
   

if __name__ == '__main__':
    appctxt = ApplicationContext()       
    window = Window()
    exit_code = appctxt.app.exec_()      
    sys.exit(exit_code)