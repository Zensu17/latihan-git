import re
def alphabet(text):
    """Return a string containing the letters of text in alphabetical order.
    
    Non-letter characters are ignored. The result is in lowercase.
    
    >>> alphabet("Hello, World!")
    'dehllloorw'
    >>> alphabet("Python 3.8")
    'hnopty'
    >>> alphabet("12345")
    ''
    """
    letters = re.findall(r'[a-zA-Z]', text)
    letters = [char.lower() for char in letters]
    letters.sort()
    return ''.join(letters)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(alphabet("Hello, World!")) 
    print(alphabet("Python 3.8"))
    print(alphabet("12345"))