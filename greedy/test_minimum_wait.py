from minimum_wait import minimumWait

def test_minimumWait():
    assert minimumWait([3,2,1,2,6]) == 17
    assert minimumWait([5,1,4]) == 6
    assert minimumWait([1]) == 0