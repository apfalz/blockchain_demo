class Block:
    def __init__(self, prev_hash, transactions):
        self.prev_hash    = prev_hash
        self.transactions = transactions
        self.hash         = hash(str([prev_hash, transactions]))



class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender    = sender
        self.recipient = recipient
        self.amount    = amount




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