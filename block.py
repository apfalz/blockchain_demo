import datetime as dt
from Crypto import Random
from Crypto.PublicKey import RSA


class Block:
    def __init__(self, prev_hash, transactions):
        self.prev_hash    = prev_hash
        self.transactions = transactions #really this is a merkle root of the transactions
        self.hash         = hash(str([prev_hash, transactions]))
        self.timestamp    = dt.datetime.now()
        self.target       = 3 #number of leading zeros in winning hash
        self.nonce        = 0

class Transaction_Input:
    def __init__(self, prev_transaction, index, script_sig):
        self.prev_transaction = prev_transaction #hash of previous transaction
        self.index            = index            #index of output in the previous transaction
        self.script_sig       = script_sig

class Transaction_Output:
    def __init__(self, value, script_public_key):
        self.value             = value
        self.script_public_key = script_public_key

class Script:
    def __init__(self, signature, public_key):
        self.signature  = signature
        self.public_key = public_key

class Transaction:
    def __init__(self, trans_inputs, trans_outputs):
        self.inputs  = trans_inputs #list of inputs
        self.outputs = trans_outputs#list of outputs

class Wallet:
    def __init__(self):
	   self.privatekey = RSA.generate(1024, Random.new().read)
	   self.publickey  = privatekey.publickey()

class Miner:
    def __init__(self):
        self.transactions = global_transactions


if __name__ == '__main__':
    first_transaction = Transaction('Satoshi', 'Andrew', '2')
    first_hash        = hash('arbitrary string serving as has for genesis block')
    genesis_block     = Block(first_hash, first_transaction)

    trans_2           = Transaction('Andrew', 'Alice', '1')
    trans_3           = Transaction('Alice',  'Bob',   '2')
    trans_4           = Transaction('Bob',    'Carly', '2')
    trans_5           = Transaction('Carly',  'Dave',  '1')
    trans_6           = Transaction('Dave',   'Eve',   '3')

    block_1           = Block(genesis_block.hash, [trans_2, trans_3, trans_4, trans_5, trans_6])
    print(block_1.hash)

    trans_7           = Transaction('Eve',    'Frank', '1')
    trans_8           = Transaction('Frank',  'Gayle', '2')
    trans_9           = Transaction('Gayle',  'Henry', '2')
    trans_10          = Transaction('Henry',  'Irina', '1')
    trans_11          = Transaction('Irina',  'Jimmy', '3')

    block_2           = Block(block_1.hash, [trans_7, trans_8, trans_9, trans_10, trans_11])
    print(block_2.hash)
