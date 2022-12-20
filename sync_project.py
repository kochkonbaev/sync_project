import os
import shutil
import time
from datetime import datetime
from dirsync import sync


def syncing(interval, source, replica):
    # This method is used to sync both source and target folder one-way every time interval you choose.

    try:
        text = sync(source, replica, 'sync')
        deleteDifferencesFromPath(replica, source)
        time.sleep(interval)
        return text
    except:
        print(f"One of the path are invalid! Please try again!")


def deleteDifferencesFromPath(pathFolder1, pathFolder2):
    '''
    This method is used to delete differences between Folder1 and Folder2.
    If there is something inside Folder1 and that's not present in Folder2 it will be deleted.
    '''

    listOfDifferences = compareFilesInFolders(pathFolder1, pathFolder2)
    for file in listOfDifferences:
        file = pathFolder2 + file
        deleteFilesAndFoldersFromPath(file)


def compareFilesInFolders(pathFolder1, pathFolder2):
    # Returns a list of differences. What is in Folder1 but isn't in Folder2

    listOfDifferences = []
    for file in os.listdir(pathFolder1):
        if file not in os.listdir(pathFolder2):
            listOfDifferences.append(file)
    return listOfDifferences


def deleteFilesAndFoldersFromPath(path):
    # This method is used to delete a file if you give its path

    try:
        shutil.rmtree(path)
    except:
        os.remove(path)


def createReport(pathToFolder1, pathToFolder2):
    # This method creates the report to be printed or write.

    filesCreated = compareFilesInFolders(pathToFolder1, pathToFolder2)
    filesCreated_text = f"List of files created: {filesCreated}"
    filesToRemove = compareFilesInFolders(pathToFolder2, pathToFolder1)
    filesToRemove_text = f"List of files remove: {filesToRemove}"
    return [filesCreated_text, filesToRemove_text]


def writeFileReport(text, path):
    # This method writes the file report to a text file.

    with open(path, 'a') as fileReport:
        fileReport.write(str(datetime.now()))
        fileReport.write(text)
        fileReport.close()


def mainLoop(source, replica, interval, pathToReport):
    # This is the main method that starts the program.

    fileReportName = "fileReport.txt"
    pathToReport = f"{pathToReport}{fileReportName}"

    while True:
        try:
            interval = int(interval)
        except:
            print("The interval that you typed should be an integer! Please try again.")
            return

        filesRemoved, fileCreated = createReport(source, replica)
        status = syncing(interval, source, replica)
        textForReport = f'''
                            {filesRemoved}
                            {fileCreated}
                        '''
        writeFileReport(textForReport, pathToReport)
        if status == False:
            print("The program will stop!")
            return
"""
Exemple:
Be sure you will use this "/" not this "\"
sourceFolderPath = '/home/abdimusa/Desktop/test_src/'
replicaFolderPath = '/home/abdimusa/Desktop/test_dst/'
fileReportPath = '/home/abdimusa/Desktop/'
setInterval = 10 (sec.)
"""            
if __name__ =="__main__":

    sourceFolderPath = input("Input your source path: ")
    replicaFolderPath = input("input your replica path: ")
    fileReportPath = input("Input where should be stored fileReport.txt:  ")
    setInterval = input("Enter the syncing interval in integer: ")

    mainLoop(sourceFolderPath, replicaFolderPath, setInterval, fileReportPath)
