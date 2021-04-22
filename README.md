
The data structures provided are:
1. An accounts dictionary
# # accounts = [[id,balance],[id,balance]]
accounts = {1: 5,
            7: 3,
            3: 5} #these are the user accounts, uid 1 has $5, uid 7 has $3 and so on

2. A transactions list
# #transactions = [[from,to,amount],[from,to,amount]]
transactions = [[1,7,2],[1,3,3]]

transactions = [[1,7,2],[3,1,10],[1,3,3]]


The candidate must write proofOfWork function, and also the helper functions that I have written, blockHash and validateTransaction

SHA256 will be provided in the test
