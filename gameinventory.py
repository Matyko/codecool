import collections
import csv

#for testing (terminal screen cleaning)
import os
def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_inventory(inventory):
    inv_total = 0
    print('\nInventory:\n')
    for k, v in inventory.items():
        print(v, k)
        inv_total += v
    print('\nTotal number of items:', inv_total)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        n_item = True
        for old_item in list(inventory):
            if item == old_item:
                n_item = False
        if n_item:
            inventory[item] = 1
            added_items.remove(item)
            n_item = False
    for old_item in inventory:
        for item in added_items:
            if old_item == item:
                inventory[old_item] += 1  
    return inventory

def print_table(*args):
    ordered_inv = inv
    inv_total = 0
    if 'count,asc':
        ordered_inv = collections.OrderedDict(sorted(inv.items(), key=lambda x: x[1]))
    if 'count,desc':
        ordered_inv = collections.OrderedDict(sorted(inv.items(), key=lambda x: x[1], reverse=True))
    print('{:>5} {:>10}'.format('Count', 'Item name'), '\n', '-'*15)
    for k, v in ordered_inv.items():
        print('{:>5} {:>10}'.format(v, k))
        inv_total += v
    print('-'*15,'\nTotal number of items:', inv_total )

def load():
    with open('inventory.csv', 'r') as inv_file:
        reader = csv.reader(inv_file)
        global inv
        loaded_inv = dict(reader)
        inv = dict((k,int(v)) for k,v in loaded_inv.items())
        inv_file.close

def save():
    with open('inventory.csv', 'w') as inv_file:
        writer = csv.writer(inv_file)
        for k, v in inv.items():
            writer.writerow([k, v])
        inv_file.close

    
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#Menu for easier testing
while True:        
    print('''
Please choose from the possible commands! (Example inventory already loaded)

1.Load inventory
2.Display inventory
3.Show inventory table
4.Dragonfight (Gain loot)
5.Save
6.Quit
        ''')
    command = input('Enter the number next to the chosen command! ')
    if command == '1':
        clean()
        try:
            load()
            print('\nInventory loaded!')
        except FileNotFoundError:
            print('\nNo saved inventory found! Please save first!')
    if command == '2':
        clean()
        display_inventory(inv)
    if command == '3':
        clean()
        asc_or_desc = input('\nOrganizing options:\n\n1.Random\n2.Ascending\n3.Descending\n\nHow do you want to organize items? ')
        print('\n')
        if asc_or_desc == '1':
            clean()
            print_table()
        if asc_or_desc == '2':
            clean()
            print_table('count,asc')
        if asc_or_desc == '3':
            clean()
            print_table('count,desc')
    if command == '4':
        clean()
        print('\n You defeated the dragon!\n')
        inv = add_to_inventory(inv, dragon_loot)
    if command == '5':
        clean()
        save()
        print('\nInventory saved!')
    if command == '6': 
        quit()        