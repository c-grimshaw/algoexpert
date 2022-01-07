from power_sets import powerset

def testPowerset():
    output = powerset([1,2,3])
    for answer in output:
        assert answer in [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    
    output = powerset([1,2])
    for answer in output:
        assert answer in [[], [1], [2], [1,2]]
    
    output = powerset([1])
    for answer in output:
        assert answer in [[], [1]]
    