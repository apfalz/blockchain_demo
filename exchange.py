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
        people.add_person(bl.Person(np.random.randint(1, 20), i, name))

    #make some transactions
    for i in range(200):
        sender    = people.people[names[np.random.randint(len(names))]]
        recipient = people.people[names[np.random.randint(len(names))]]
        amount    = np.random.randint(1, 20)#sender.coin_possessed)
        result    = sender.request_trade(exchange, recipient, amount)#for now allow sending coin to yourself
        posessed  = '/' + str(sender.coin_possessed)
        print(sender.name + ' wants to send ' + str(amount) + posessed + ' to ' + recipient.name)
        if result == True:
            with open(fn, 'a') as f:
                f.write(sender.name + ' ' + recipient.name + ' ' + str(amount) + ' \n')

        time.sleep(np.random.randint(2))
