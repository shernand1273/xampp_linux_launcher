#     Copyright (C) 2020, Steven Hernandez#     
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

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget
import sys
import json

def addButtonCLicked(parentObj):
    file = QFileDialog()
    path = file.getOpenFileName()[0]
    
    
    if(len(path)==0):
        pass
    else:
        parentObj.pathInput.setText(path)
        parentObj.pathInput.setStyleSheet("""
                                            background-color:white;
                                            color:black;
                                        """)

def cancelButtonClicked(parent):
    message = QMessageBox.question(parent,
                                    "Quit",
                                    "Are you sure you want to cancel the setup?\n\nYou will not be able to use this application.",
                                    buttons=QMessageBox.No | QMessageBox.Yes,
                                    defaultButton=QMessageBox.No
                                    )
    if(message == QMessageBox.No):
        pass
    elif(message == QMessageBox.Yes):
        sys.exit(None)

def finalizeButtonClicked(parent,context):
    if(parent.pathInput.text()== '.run file location'):
        msg = QMessageBox.information(parent,"File Missing",".run file has not been added, select it beofore finalizing",buttons=QMessageBox.Ok,defaultButton=QMessageBox.Ok)
        if(msg == QMessageBox.Ok):
            pass
    else:
        runFilePath = parent.pathInput.text()
        if(parent.validRunFile(runFilePath)):
            try:
                jsonFileData = json.load(open(context.get_resource('config/config.json')))
            except Exception as error:
                message = QMessageBox.information(none,"Error","There seems to be a problem with your configuration file.  Try reinstalling this application.",buttons = QMessageBox.OK)
        
            else:
                jsonFileData['runFile']=runFilePath
                strToWrite = json.dumps(jsonFileData)
                with open(context.get_resource('config/config.json'),'w')as w_file:
                    w_file.write(strToWrite)
                    w_file.close()
                parent.feedback.show()
                parent.feedback.setStyleSheet("color:green;font-size:14px;font-family:serif;")
                parent.cancelButton.hide()
                parent.finalizeButton.setText("Close")
                parent.finalizeButton.clicked.connect(lambda: closeButtonClicked())
                 
        else:
            msgBox = QMessageBox.information(parent,"Invalid File","The file you selected is invalid, ensure it is the xampp .run file",buttons=QMessageBox.Ok,defaultButton=QMessageBox.Ok)
            if(msgBox == QMessageBox.Ok):
                pass

def closeButtonClicked():
    sys.exit(None)