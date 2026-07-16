# GitHub username: lopezram503
# Date: 7/15/26
# Description: This code returns a list of names that start with the letter K
# and adds the surname Kardashian to each name.

def add_surname(name_list):

    """ Returns a list of names that start with 'K' with surname Kardashian added."""

    # This line returns names starting with 'K' and with 'Kardashian' added.
    return [name + ' Kardashian' for name in name_list if name[0] == 'K']

