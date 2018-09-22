accounts = {}


def add_account(name, password):
    """Function enables user to create an account"""
    if not name.isalpha():
        return "A name should only consist alphabetical characters!",False

        accounts[password] = name

def login(name, password):
    """
    Returns True if the name and the corresponding password 
    exists in the accounts dictionary
    """

    if accounts.get(password):
        if accounts[password] is name:
            return True
        return False
    return False       
    """"verrifying the user's credentials""" 