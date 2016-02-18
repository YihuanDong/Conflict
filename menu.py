import sys, os
from git import Repo
repo = Repo('/Users/ray/Documents/Project/Conflict')

menu_actions = {}
def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Choose:"
    print "1.Check Git Status"
    print "2.Check Git Log"
    print "\n0. Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)
    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid slection, please try again.\n"
            menu_actions['main_menu']()
    return

def menu1():
    print "check git status"
    print "untacked files:"
    print repo.untracked_files
    #print repo.index.diff(repo.head)
    print "9.Back"
    print "0.Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)
    return

def menu2():
    print "check git log"
    head = repo.head
    master = head.reference
    master.commit
    log  = master.log()
    print log
    print "9.Back"
    print "0.Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)
    return

def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()

menu_actions = {
        'main_menu': main_menu,
        '1': menu1,
        '2': menu2,
        '9': back,
        '0': exit,
}

if __name__ == "__main__":
    main_menu()
