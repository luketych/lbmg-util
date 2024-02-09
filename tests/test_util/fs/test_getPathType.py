from namespace.util import getPathType



def test_absolutePath():
    path = "/a/b/c/d"
    expected = "absolute"
    
    result = getPathType(path)
    
    assert result == expected

def test_relativePath_1():
    path = "../a/b/c/d"
    expected = "relative"
    
    result = getPathType(path)
    
    assert result == expected
    
def test_relativePath2():
    path = "./a/b/c/d"
    expected = "relative"
    
    result = getPathType(path)
    
    assert result == expected

def test_projectRelativePath():
    path = "src/pipelines/single_pipelines/system1/config.json"
    expected = "project-relative"
    
    result = getPathType(path)
    
    assert result == expected
    
def test_projectRelativePathInvalidPath():
    path = "src/pipelines/single_pipelines/system1/not_a_file.json"
    
    try:
        result = getPathType(path)
    except ValueError:
        result = "ValueError"
    
    expected = "ValueError"
    
    assert result == expected
    
def test_invalidPath():
    path = "not_a_path"
    
    try:
        result = getPathType(path)
    except ValueError:
        result = "ValueError"
    
    expected = "ValueError"
    
    assert result == expected