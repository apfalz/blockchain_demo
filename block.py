import datetime as dt
from Crypto import Random
from Crypto.PublicKey import RSA

class People:
    def __init__(self):
        self.people = {}

    def add_person(self, person_instance):
        hash_of_address = hash(person_instance.address)
        if hash_of_address in self.people:
            current_person = self.people[hash_of_address]
            while(current_person.next != None):
                print('found collision! traversing...')
                current_person = current_person.next
            current_person.next = person_instance
        else:
            self.people[hash_of_address] = person_instance

    def lookup(self, address, name):
        address_hash = hash(address)
        if address_hash not in self.people:
            print('unknown address! ' + name + ' is not a known person.')
        else:
            bucket = self.people[address_hash]
            if bucket.name == name:
                return bucket
            else:
                print('found collision, traversing...')
                done = False
                while bucket.next != None and done == False:
                    bucket = bucket.next
                    if bucket.name == name:
                        done = True
                    if bucket.next == None and bucket.name != name:
                        print('could not find person.')
                        bucket = None
                return bucket

class Block:
    def __init__(self, prev_hash, transactions):
        self.prev_hash    = prev_hash
        self.transactions = transactions #really this is a merkle root of the transactions
        self.hash         = hash(str([prev_hash, transactions]))
        self.timestamp    = dt.datetime.now()
        self.target       = 3 #number of leading zeros in winning hash
        self.nonce        = 0



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
    def __init__(self, sender_address, sender_name, receiver_address, receiver_name, amount):
        self.sender_address   = sender_address
        self.sender_name      = sender_name
        self.receiver_address = receiver_address
        self.receiver_name    = receiver_name
        self.amount           = amount

class Person:
    def __init__(self, coin_possessed, address, name):
        self.name           = name
        self.coin_possessed = coin_possessed
        self.address        = address
        self.next           = None #for linked list collisions in People hashtable

    def request_trade(self, exchange, recipient_address, amount):
        exchange.receive_request(trade(self.address, self.name, recipient_address, recipient_name,  amount))

    def receive_trade(self, amount):
        self.coin_possessed += amount


class Exchange:
    def __init__(self, name):
        self.name     = name
        self.requests = []

    def receive_request(self, trade_instance):
        self.requests.append(trade_instance)

    def broadcast_requests(self):
        return

class Miner:
    def __init__(self):
        self.transactions = global_transactions


if __name__ == '__main__':
    first_transaction = Transaction('Satoshi', 'Andrew', '2')
    first_hash        = hash('arbitrary string serving as has for genesis block')
    genesis_block     = Block(first_hash, first_transaction)
