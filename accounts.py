accounts = {}


def add_account(name, password):
    """Function enables user to create an account"""
    if not name.isalpha():
        return "A name should only consist alphabetical characters!",False

        accounts[password] = name
       
