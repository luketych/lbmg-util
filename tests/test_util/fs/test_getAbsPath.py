import os

from namespace.util import getAbsPath, getPyprojectRootDir 



def test_absolutePath():
    path = "/a/b/c/d"
    expected = "/a/b/c/d"
    
    result = getAbsPath(path)
    
    assert result == expected
    
def test_relativePath():
    path = "../a/b/c/d"
    expected = os.path.abspath("../a/b/c/d")
    
    result = getAbsPath(path)
    
    assert result == expected
    
def test_projectRelativePath():
    path = "src/pipelines/single_pipelines/system1/config.json"
    expected = os.path.join(getPyprojectRootDir(), path)
    
    result = getAbsPath(path)
    
    assert result == expected