import datetime as dt
import time
import numpy as np
import threading
from Crypto import Random
from Crypto.PublicKey import RSA

class People:
    def __init__(self, exchange_instance):
        self.people   = {}
        self.exchange = exchange_instance
        self.names    = ['Alice', 'Bob', 'Carly', 'Dave', 'Emma', 'Frank', 'Gwen', 'Henry', 'Iggy', 'James', 'Karen', 'Larry']
        self.verbose  = 2

        #add people to the table
        for i, name in enumerate(self.names):
            self.add_person(Person(np.random.randint(1, 20), i, name))

        self.transaction_thread = threading.Thread(target=self.start_generating_transactions)
        self.transaction_thread.start()

    def add_person(self, person_instance):
        self.people[person_instance.name] = person_instance

    def start_generating_transactions(self):
        for i in range(200):
            sender    = self.people[self.names[np.random.randint(len(self.names))]]
            recipient = self.people[self.names[np.random.randint(len(self.names))]]#for now allow sending coin to yourself
            amount    = np.random.randint(1, 20)
            posessed  = '/' + str(sender.coin_possessed)
            trade     = Trade(sender, recipient, amount)
            if self.verbose >= 2:
                print(sender.name + ' wants to send ' + str(amount) + posessed + ' to ' + recipient.name)
            self.exchange.receive_request(trade)


            time.sleep(np.random.randint(2))

class Block:
    def __init__(self, prev_hash, transaction_list):
        self.prev_hash    = prev_hash
        self.transactions = transaction_list#Not accurate for now, really this is a merkle root of the transactions
        self.nonce        = 0
        self.timestamp    = dt.datetime.now()
        self.target       = 10 #for now this is the delay to wait before successfully creating block
        self.verbose      = 2 #2: print everything, 1: print normally, 0: print nothing
        self.print_freq   = 100
        self.hash         = self.create_hash()
        #self.solve_puzzle()


    def create_hash(self):
        prev     = sum([ord(i) for i in str(self.prev_hash)])
        trans    = sum([ord(i) for i in str(self.transactions)])
        cur_hash = (prev + trans) - self.nonce
        return cur_hash

    def solve_puzzle(self):
        '''for the time being just pretend to solve a problem'''
        print('beginning to generate new block...')
        value        = 0
        while value != self.target and self.interrupt == False:
            time.sleep(np.random.randint(10))
            value += 1
        print('created new block!')

        return hash(str(self.prev_hash) + str(self.transactions) + str(self.nonce))


    def future_solve_puzzle(self):
        cur_hash = self.create_hash()
        while cur_hash >= self.target:
            self.nonce += 1
            cur_hash    = self.create_hash()
            if self.verbose >= 2:
                if num_attempts % self.print_freq == 0:
                    print(str(num_attempts) + ' attempts so far.')#, end='')
        return cur_hash


class Network:
    def __init__(self):
        self.newest_block           = None
        self.requested_transactions = []
        self.connected_miners       = []
        self.verbose                = 2
        self.list_of_mined_blocks   = []

    def establish_connection(self, miner):
        print('\n Received new connection from ' + miner.name + '\n')
        self.connected_miners.append(miner)

    def receive_new_block(self, block, miner_name):
        print("Network received a new block! Broadcasting to all miners on network")
        self.newest_block = block
        self.list_of_mined_blocks.append(block)
        for miner in self.connected_miners:
            if miner.name != miner_name:
                miner.receive_new_block(self)



class Transaction:
    def __init__(self, transactions):
        self.transactions  = transactions
        self.verbose       = 2

    def receive_request(self, trade):
        self.transactions.append(trade)

    def verify_request(self, trade_instance):
        sender   = People.lookup(trade_instance.sender_address,   trade_instance.sender_name)
        receiver = People.lookup(trade_instance.receiver_address, trade_instance.receiver_name)

        if sender and receiver and sender.coin_possessed >= trade_instance.amount:
            return True
        else:
            print('Dectected fraudulent transaction attempt!')
            return False

class Trade:
    def __init__(self,  sender_instance,  receiver_instance, amount):
        self.sender   = sender_instance
        self.receiver = receiver_instance
        self.amount   = amount

class Person:
    def __init__(self, coin_possessed, address, name):
        self.name           = name
        self.coin_possessed = coin_possessed
        self.address        = address
        self.next           = None #for linked list collisions in People hashtable

    def request_trade(self, exchange, recipient, amount):
        self.coin_possessed -= amount


    def receive_trade(self, amount):
        self.coin_possessed += amount

class Exchange:
    def __init__(self, name, network_instance):
        self.name                  = name
        self.verbose               = 2
        self.connection_to_network = network_instance

    def receive_request(self, trade_instance):
        if trade_instance.amount <= trade_instance.sender.coin_possessed:
            self.broadcast_request(trade_instance)
            trade_instance.sender.coin_possessed -= trade_instance.amount
            return True
        else:
            if self.verbose >= 2:
                print('Detected fraudulent transaction!')
            return False

    def broadcast_request(self, trade):
        self.connection_to_network.requested_transactions.append(trade)


class Miner:
    def __init__(self, name, network_connection):
        self.name             = name
        self.num_blocks_mined = 0
        self.mined_blocks     = []
        self.network          = network_connection
        self.network.establish_connection(self)
        self.pending_trades   = None
        self.newest_block     = self.network.newest_block
        self.interrupt        = False
        self.newest_block     = network.newest_block
        self.verbose          = 2
        self.mining_thread    = threading.Thread(target=self.start_mining)
        self.mining_thread.start()


    def start_mining(self):
        #first get transactions from the network
        self.pending_trades = self.network.requested_transactions
        last_block          = self.network.newest_block
        value               = 0
        target              = 10
        if self.verbose >= 2:
            print(self.name + ': Begin mining for new block')

        #keep working until you receive interrupt or until you find a new block
        while self.interrupt == False and value != target:
            time.sleep(np.random.randint(5))
            value += 1

        #if you found a new block, broadcast it and start working on next block
        if value == target:
            print(self.name + ': I found a new block! Letting network know about it.')
            new_block = Block(hash(str(last_block)), self.pending_trades)
            self.broadcast_new_block(new_block)
            self.start_mining()

        #if someone else found the block before you, update your state, then start working on next block.
        elif self.interrupt == True and value != target:
            print(self.name + ': Someone else found a block. Starting over.')
            #updating state is handled at beginning of function, so just make recursive call
            self.interrupt = False
            self.start_mining()



    def broadcast_new_block(self, block):
        self.network.receive_new_block(block, self.name)

    def receive_new_block(self, block):
        self.interrupt = True











if __name__ == '__main__':
    print('creating network')
    network              = Network()
    genesis_block        = Block('genesis_block', 'first_transaction')
    network.newest_block = genesis_block

    print('creating exchange')
    demo_exchange        = Exchange('demo_exchange', network)
    demo_exchange.verbose = 1

    print('creating people')
    people               = People(demo_exchange)
    people.verbose       = 1

    print('creating miners')
    miner_0              = Miner('miner_0', network)
    miner_1              = Miner('miner_1', network)
