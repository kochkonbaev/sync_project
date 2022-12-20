# Syncing two folders
### Test Task
#### The problem:
Implement a program that synchronizes two folders: source and replica.
The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:
- Synchronization must be one-way: after the synchronization content of the replica folder
should be modified to exactly match content of the source folder;
- Synchronization should be performed periodically;
- File creation/copying/removal operations should be logged to a file and to the console output;
- Folder paths, synchronization interval and log file path should be provided using the command line arguments.
> How to Run:
```python
# copy repository
$ git clone https://github.com/Kochkonbaev/sync_project.git

# create environment
python3 -m venv env

# activate env
source env/bin/activate

# installing the required dependensies
pip3 install -r requirements.txt

# runing file
python3 sync_project.py
```
#### Exemple:
> - Be sure you will use this "/" not this "\"
> - sourceFolderPath = '/home/abdimusa/Desktop/test_src/'
> - replicaFolderPath = '/home/abdimusa/Desktop/test_dst/'
> - fileReportPath = '/home/abdimusa/Desktop/'
> - setInterval = 10

### Thank you for your time :)
![Медведи](https://pbs.twimg.com/media/DQNtydoX0AAIAWb.jpg:small)
