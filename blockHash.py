import hashlib


#sha256 to calculate block hashes
def sha256(prevBlockHash, nonce, transactions):
    sha256 = hashlib.sha256()
    preHash = prevBlockHash + str(nonce) + str(transactions)
    sha256.update(preHash.encode())
    return sha256.hexdigest()

def validTransaction(accounts, transaction):
    if accounts[transaction[0]] >= transaction[2]:
        return True
    else:
        return False

def blockHash(prevBlockHash, transactions):
    blockHash = ""
    nonce = -1
    while blockHash[0:4] != "0000":##this is the proof of work condition
        nonce+=1
        blockHash = sha256(prevBlockHash,nonce,transactions)
        #print(blockHash)
    return blockHash, nonce, transactions



def proofOfWork(accounts, transactions, blockSize):
    currentTransactions = []
    prevBlockHash =  "0"*64 ## this is the initialization vector  


    ##verify that transactions are valid

    while transactions:
        current_transaction  = transactions.pop(0)
        if validTransaction(accounts,current_transaction):
            ##if transaction valid then add it to current transactions and update accounts
            currentTransactions.append(current_transaction)
            accounts[current_transaction[0]] -= current_transaction[2]
            accounts[current_transaction[1]] += current_transaction[2]
        
        if len(currentTransactions) == blockSize:
            block_Hash = blockHash(prevBlockHash, currentTransactions)
            currentTransactions = []
            prevBlockHash = block_Hash[0]
    ## managing the case where there were lesser transactions left than blocksize
    if currentTransactions:
        block_Hash = blockHash(prevBlockHash, currentTransactions)
        currentTransactions = []
        prevBlockHash = block_Hash[0]

    return block_Hash



