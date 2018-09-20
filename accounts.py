accounts = {}


def add_account(name, password):
    """Function enables user to create an account"""
    if not name.isalpha():
        print("A name should only consist alphabetical characters!")
    else:
        accounts[password] = name
        print( "{} is registered. Proceed and login".format(accounts[password]))
        return accounts


def login(name, password):
    """Function enables user to login into their account"""
    for key in accounts:
        if key == accounts[password]:
            return True
            return False
    """ Accepting credentials"""