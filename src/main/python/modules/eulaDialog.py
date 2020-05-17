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
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import json
import sys

def openEula(parent,appContext):
    eulaWindow = QDialog(parent = parent)
    eulaWindow.setMinimumWidth(600)
    eulaWindow.setMinimumHeight(300)
    eulaWindow.setMaximumHeight(320)
    eulaWindow.setMaximumWidth(650)
    mainLayout = QVBoxLayout()
    labelLayout = QHBoxLayout()
    checkboxLayout = QVBoxLayout()
    buttonLayout = QHBoxLayout()
    eulaLabel = QLabel("License Agreement")
    eulaText = QTextEdit()
    eulaText.setText(getEulaText(appContext))
    agree = QCheckBox("I accept the license conditions")
    submitButton = QPushButton("Submit")
    cancelButton = QPushButton("Cancel")
    eulaText.setAlignment(Qt.AlignCenter)
    eulaText.setReadOnly(True)
    eulaLabel.setStyleSheet("font-size:20px;font-weight:bold;")
    eulaText.setMaximumHeight(400)
    agree.setChecked(False)
    eulaText.wordWrapMode()
    eulaText.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    buttonLayout.addWidget(cancelButton)
    buttonLayout.addWidget(submitButton)
    buttonLayout.setAlignment(Qt.AlignRight)
    checkboxLayout.addWidget(agree)
    checkboxLayout.setAlignment(Qt.AlignLeft)
    labelLayout.setAlignment(Qt.AlignCenter)
    mainLayout.setAlignment(Qt.AlignCenter)
    labelLayout.addWidget(eulaLabel)
    mainLayout.addLayout(labelLayout)
    mainLayout.addWidget(eulaText)
    mainLayout.addLayout(checkboxLayout)
    mainLayout.addLayout(buttonLayout)
    mainLayout.addStretch()
    eulaWindow.setLayout(mainLayout)
    cancelButton.clicked.connect(lambda: cancelButtonClicked(eulaWindow))
    submitButton.clicked.connect(lambda: submitButtonClicked(parent,eulaWindow,agree,appContext))
    eulaWindow.show()


def getEulaText(appContext):
    with open(appContext.get_resource('license/eula.txt'),'r')as r_file:
        return r_file.read()

def cancelButtonClicked(window):
    message = QMessageBox.question(window,"Confirm","Are you sure? You will not able to use the application.\n\n'No' to continue setup\n'Yes' to quit setup",buttons=QMessageBox.No | QMessageBox.Yes)

    if(message == QMessageBox.No):
        pass
    elif(message == QMessageBox.Yes):
        sys.exit(0)
    else:
        pass
def submitButtonClicked(parent,window,checkbox,appContext):
    if(checkbox.isChecked()):
        window.close()
        configFileLocation =appContext.get_resource('config/config.json')
        with open(configFileLocation,'r')as r_file:
            data = r_file.read()
            dataDict = json.loads(data)
            dataDict['Eula']= True
            saveData(dataDict,configFileLocation)
        parent.__init__()
    else:
        message = QMessageBox.information(window,"Requirement","To use this software, you must agree with the Licensing conditions.",buttons=QMessageBox.Ok)
        

def saveData(data,fileLocation):
    wdata = json.dumps(data)
    with open(fileLocation,'w')as w_file:
        w_file.write(wdata)