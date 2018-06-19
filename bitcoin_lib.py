import datetime as dt
import time
import numpy as np
from Crypto import Random
from Crypto.PublicKey import RSA

class People:
    def __init__(self, exchange_instance):
        self.people   = {}
        self.exchange = exchange_instance
        self.names    = ['Alice', 'Bob', 'Carly', 'Dave', 'Emma', 'Frank', 'Gwen', 'Henry', 'Iggy', 'James', 'Karen', 'Larry']
        #add people to the table
        for i, name in enumerate(self.names):
            self.add_person(Person(np.random.randint(1, 20), i, name))

    def add_person(self, person_instance):
        self.people[person_instance.name] = person_instance

    def start_generating_transactions(self):
        for i in range(200):
            sender    = self.people[self.names[np.random.randint(len(self.names))]]
            recipient = self.people[self.names[np.random.randint(len(self.names))]]#for now allow sending coin to yourself
            amount    = np.random.randint(1, 20)
            posessed  = '/' + str(sender.coin_possessed)
            trade     = Trade(sender, recipient, amount)
            print(sender.name + ' wants to send ' + str(amount) + posessed + ' to ' + recipient.name)
            self.exchange.receive_request(trade)


            time.sleep(np.random.randint(2))

class Block:
    def __init__(self, prev_hash, transaction_list):
        self.prev_hash    = prev_hash
        self.transactions = str(transaction_list) #really this is a merkle root of the transactions
        self.nonce        = 0
        self.timestamp    = dt.datetime.now()
        self.target       = 3241 #number of leading zeros in winning hash
        self.verbose      = 2 #2: print everything, 1: print normally, 0: print nothing
        self.print_freq   = 100
        self.hash         = self.create_hash()
        self.solve_puzzle()


    def create_hash(self):
        prev     = sum([ord(i) for i in self.prev_hash])
        trans    = sum([ord(i) for i in self.transactions])
        cur_hash = (prev + trans) - self.nonce
        return cur_hash

    def solve_puzzle(self):
        '''for the time being just pretend to solve a problem'''
        print('beginning to generate new block...')
        time.sleep(np.random.randint(10))
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

class Transaction:
    def __init__(self, transactions):
        self.transactions  = transactions

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
        self.name     = name
        self.connection_to_network = network_instance

    def receive_request(self, trade_instance):
        if trade_instance.amount <= trade_instance.sender.coin_possessed:
            self.broadcast_request(trade_instance)
            trade_instance.sender.coin_possessed -= trade_instance.amount
            return True
        else:
            print('Detected fraudulent transaction!')
            return False

    def broadcast_request(self, trade):
        self.connection_to_network.requested_transactions.append(trade)


class Miner:
    def __init__(self, network_connection):
        self.num_blocks_mined = 0
        self.mined_blocks     = []
        self.network          = network_connection
        self.pending_trades   = None
        self.start_mining()
        self.newest_block     = self.network.newest_block

    def start_mining(self):
        #first get transactions from the network
        self.pending_trades = self.network.requested_transactions




    def find_block(self):
        new_block = Block(str(hash('genesis_block')), str(self.transactions_list))


if __name__ == '__main__':
    network              = Network()
    genesis_block        = Block('genesis_block', 'first_transaction')
    network.newest_block = genesis_block

    demo_exchange        = Exchange('demo_exchange', network)
    people               = People(demo_exchange)
    people.start_generating_transactions()
