from string import ascii_letters

# Code that makes text funny
def funny(t: str, d: bool=False):

    # Things to make it funny
    f, n, i = '', '', 1

    # Make text funny
    for c in t:
        i += 1

        # Skip if non ascii char
        if c not in ascii_letters:
            i -= 1
            f += c
            continue

        # Make char funny
        if i % 2 == 0:
            n = c.upper()
        else:
            n = c.lower()
        
        # Show debug
        if d:
            print(i, c, n)
        
        # Add funny char
        f += n
    
    # Return funny text
    return f
