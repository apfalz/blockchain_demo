import datetime as dt
import time
import numpy as np
from Crypto import Random
from Crypto.PublicKey import RSA

class People:
    def __init__(self):
        self.people = {}

    def add_person(self, person_instance):
        self.people[person_instance.name] = person_instance

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
        result               = exchange.receive_request(Trade(self,
                                                              recipient,
                                                              amount))
        return result

    def receive_trade(self, amount):
        self.coin_possessed += amount

class Exchange:
    def __init__(self, name):
        self.name     = name
        self.requests = []

    def receive_request(self, trade_instance):
        if trade_instance.amount <= trade_instance.sender.coin_possessed:
            self.requests.append(trade_instance)
            return True
        else:
            print('Detected fraudulent transaction!')
            return False

    def broadcast_requests(self):
        return

class Miner:
    def __init__(self):
        self.num_blocks_mined = 0
        self.minded_blocks    = []
        with open('transactions.txt', 'r') as f:
            self.transactions_list = f.readlines()

    def find_block(self):
        new_block = Block(str(hash('sdf')), str(self.transactions_list))


if __name__ == '__main__':
    first_hash        = hash('arbitrary string serving as has for genesis block')
    genesis_block     = Block(str(first_hash), 'first_transaction')

    genesis_block.solve_puzzle()
