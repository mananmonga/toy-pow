from blockHash import proofOfWork

def test_1():
    accounts = {1: 5,
                7: 3,
                3: 5}

    transactions = [[1,7,2],[3,1,10],[1,3,3]]
    res = proofOfWork(accounts,transactions,1)

    assert res == ('0000744d9b4e29db5be9ad1b2830578f5fea3d6ac6de855ba98e0cbd8a4a978a', 93765, [[1, 3, 3]])


def test_2():
    accounts = {1: 5,
                7: 3,
                3: 5}
    transactions = [[1,7,2],[1,3,3]]

    res = proofOfWork(accounts, transactions, 2)
    assert res == ('0000b3eb6a11fb54acd6dc1291d757f9c85910f1ecf6544eba4657694eafd342', 15799, [[1, 7, 2], [1, 3, 3]])

def test_3():

    accounts = {1: 10,
                2: 15,
                3: 10}
    transactions = [[1,2,5],[1,3,5],[1,2,10],[3,1,5]]    
    res = proofOfWork(accounts, transactions, 2)
    assert res == ('0000b6887cad1ed110f8447a36c4b3c8713c23a0dc079161abe24245364f5812', 66897, [[3, 1, 5]])