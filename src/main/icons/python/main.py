from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import os
import sys
import json



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300,200,300,300)
        self.setWindowTitle("This is a test")
        self.UI()
        
        

    def UI(self):
        #first thing to do is check that we have a configuration file setup
        if(os.path.exists(appctxt.get_resource('config/config.txt'))):
            
            fileData = None
            dataDict = None
            #This means that the config file exists.

            #we need to read the data to make sure that the config file has data written to it
            with open(appctxt.get_resource('config/config.txt'),'r')as r_file:
                fileData = r_file.read()
                #this data should come in the fom of a dictionary
                dataDict = json.loads(fileData)
                print("file red")

            #Maybe some more work: feedback, error logging, etc
            if(dataDict is not None and "configuration" in dataDict):
                kys = dataDict['configuration'].keys()
                if("runFilePath" in kys):
                    #final check is to make sure that the path is not empy for some reason
                    runFile = dataDict['configuration']['runFilePath']
                    #another check to make sure everything is fine is to check the lengh and the suffix
                    if(len(runFile)>0 and runFile.endswith('.run')):
                        os.system("sudo {}".format(runFile))
                        #sys.exit(None)
                    else:
                        print("There is something wrong with your file path its either missing or not in the right format")
                else:
                    print("Missing the run file path")
                
            else:
                print("There is some problem here")
                
        else:
           self.initialSetup()
    
        #self.show()

    def initialSetup(self):
        #call a setup function for the initial configuration file setup
        message= "To successfully setup this application, you must select your xampp .run file in the next step"
        subMessage ="\n\nClick 'Ok' to select file\nClick 'Cancel' to abort and exit setup"
        msgBox =QMessageBox.information(self,"Setup","{}{}".format(message,subMessage),buttons =QMessageBox.Ok| QMessageBox.Cancel,defaultButton=QMessageBox.Ok)
        if(msgBox == QMessageBox.Cancel):
            confirm =QMessageBox.warning(self,"Confirm","Are you sure you want to cancel?\n\nYou will not be able to use this tool until the Setup is complete.",buttons=QMessageBox.Yes | QMessageBox.No)
            if(confirm == QMessageBox.Yes):
                sys.exit(None)
            elif(confirm == QMessageBox.No):
                self.initialSetup()
        elif(msgBox == QMessageBox.Ok):
            #this is where we bring up the fileSelector dialog
            filePath = QFileDialog(self)
            file = filePath.getOpenFileName(self)[0]
            #now that we have the file, we need to make sure that it is a .run file
            if(self.validFile(file)):
                #the file seems to be valid
                #this is where we are going to write the file
                tempDictionary = {"configuration":{}}
                tempDictionary["configuration"].__setitem__("runFilePath",file)
                st = json.dumps(tempDictionary)
                #we are now write new config file
                self.writeConfigFile(st)

                

            else:
                #let the user know that the file seems to be invalid, it requires a .run file
                print("Not cool")

    def validFile(self,fileName):
        return fileName.endswith('.run')

    def writeConfigFile(self,data):
        try:
            with open("{}/{}".format(appctxt.get_resource('config'),'config.txt'),"w+")as w_file:
                w_file.write(data)


        except Exception as error:
            print("There was an errror writing this file")
            print(error)

        else:
            #read teh file data to make sure it is the same
            readBackData = open(appctxt.get_resource('config/config.txt')).read()
            if(readBackData == data):
                #we are going to let the user know that all went well
                msg = QMessageBox(self)
                msg.information(self,"Setup","SUCCESS\n\nNext time you open this application, it will launch xampp.",buttons=QMessageBox.Ok,defaultButton=QMessageBox.Ok)
                if(msg == QMessageBox.Ok):
                    sys.exit(None)
            else:
                print("There was a problem creating your configuration")
    
    

if __name__ == '__main__':
    appctxt = ApplicationContext()       
    window = Window()
    exit_code = appctxt.app.exec_()      
    sys.exit(exit_code)
