from traverse_grid import numberOfWaysToTraverseGraph

def testNumberOfWaysToTraverseGraph():
    assert numberOfWaysToTraverseGraph(width=4, height=3) == 10
    assert numberOfWaysToTraverseGraph(width=2, height=3) == 3