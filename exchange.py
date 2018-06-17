import numpy       as np
import bitcoin_lib as bl
import time








if __name__ == '__main__':
    exchange = bl.Exchange('demo_exchange')
    fn       = 'transactions.txt'
    with open(fn, 'w') as f:
        f.write('')

    names  = ['Alice', 'Bob', 'Carly', 'Dave', 'Emma', 'Frank', 'Gwen', 'Henry', 'Iggy', 'James', 'Karen', 'Larry']

    #make a people hash table
    people = bl.People()

    #add people to the table
    for i, name in enumerate(names):
        people.add_person(bl.Person(np.random.randint(42), i, name))

    #make some transactions
    for i in range(10):
        sender    = people.people[names[np.random.randint(len(names))]]
        recipient = people.people[names[np.random.randint(len(names))]]
        amount    = np.random.randint(sender.coin_possessed)
        sender.request_trade(exchange, recipient, amount)#for now allow sending coin to yourself
        print(sender.name + ' wants to send ' + str(amount) + ' to ' + recipient.name)
        with open(fn, 'a') as f:
            f.write(sender.name + ' ' + recipient.name + str(amount) + ' \n')
        time.sleep(np.random.randint(10))
