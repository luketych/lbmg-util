import os
from termcolor import colored



def extract_path_up_to_str(file_path, str):
    index = file_path.find(str)
    if index != -1:
        return file_path[:index + len(str)]
    else:
        return None  # or an appropriate value if 'tasks' is not found


''' If head=None @returns the file or dir at the end of the given uri
    else @returns the file or dir at the end of the given uri after the head
    ie if uri="/a/b/c/d/e" and head="b/c" or head="a/b/c" then returns "d/e"
'''
def getPathTail(path, head_or_subhead=None):
    if head_or_subhead is None:
        return os.path.basename(path)

    if head_or_subhead not in path:
        print(colored(f"Warn: head '{head_or_subhead}' not in uri '{path}'", "yellow"))

        return None

    
    
    
    # complete the head. If head is just a subset of the entire head, for example tasks/, then get the entire uri, ie a/b/c/d/e/tasks/
    
    path_up_to_head = extract_path_up_to_str(path, head_or_subhead)
    
    
    
    tail = path.replace(path_up_to_head, "", 1)
    
    
  
    tail = tail.lstrip("/")

    
    return tail
  
  
  
  
# uri = '/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/tasks/t4-mutateData/b_add_hash_col.py'
# head_or_subhead = '/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/tasks/'
# #head_or_subhead = 'tasks'

# tail = getPathTail(uri, head_or_subhead)

# print(tail)