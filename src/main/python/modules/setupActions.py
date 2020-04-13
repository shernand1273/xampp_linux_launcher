from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget
import sys
import json

#opens up the file dialog widget for the user to select the .run file
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

    
#closes the program when the user confirms
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


# function checks that th user selected the .run file, 
# makes sure that the input is not empty, 
# writes the file path to the json configuration file
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
                print(error)#TODO --- Tell the user theere was a problem
        
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