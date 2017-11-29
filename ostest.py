import os, logging, send2trash
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.NOTSET)
logging.debug(os.getcwd())
logging.debug('Start of program')
logging.info('CWD: ' + os.getcwd())
root = os.getcwd() + '/'
#gives absolute path!
for folderName, subfolders, files in os.walk(os.getcwd()):
	logging.debug('FolderName: %s', folderName)
	logging.debug('subfolders: ' + str(subfolders))
	logging.debug('files: ' + str(files))
	if folderName.endswith('__'):
		logging.critical('trashing ' + folderName)
		send2trash.send2trash(folderName)

 

