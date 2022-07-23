#1. What does an empty dictionary's code look like?
     D = {}


#2. What is the value of a dictionary value with the key 'foo' and the value 42?
     Dict = {“foo” : 42}


#3.What is the most significant distinction between a dictionary and a list?
    """•	
    List values can be extracted with the indices, example: L[2] = 5
    Dictionary value can be extracted using key/value pair.
    Example: dict[“foo”]. The output value is  42.
    """


# 4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?
    """
    This will give a Keyerror : foo
    """

# 5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
    """
    No difference
    “cat” in spam.keys() and the expression checks whether “cat” is the key in the dictionary.
    """

#6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
    """“cat” in spam checks whether cat is a key
    “cat” in Spam.values() whether it is a value"""

#7.What is a shortcut for the following code?
    """
    if 'color' not in spam:
    spam['color'] = 'black'
    
    Shortcut code:
        spam.setdefault("color", "Black")"""


#8.How do you "pretty print" dictionary values using which module and function?
    """
    import pprint
    
    D = {'no': [1, 2, 3], "name": "Sejal"}
    pprint.pprint(D, indent=2, depth=1, width=10)"""
