import os


''' Given a uri to a file or dir, return the uri to the parent dir
'''
def getParentDirPath(uri):
    return os.path.dirname(uri)