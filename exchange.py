import numpy       as np
import bitcoin_lib as bl








if __name__ == '__main__':

    names  = ['Alice', 'Bob', 'Carly', 'Dave', 'Emma', 'Frank', 'Gwen', 'Henry', 'Iggy', 'James', 'Karen', 'Larry']

    #make a people hash table
    people = bl.People()

    #add people to the table
    for name in names:
        people.add_person(bl.Person(np.random.randint(42), np.random.randint(1000), name))

    for name in names:
        people.lookup()
