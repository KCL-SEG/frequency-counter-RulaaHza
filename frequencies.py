"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for a in items:
        count=0
        for b in items:
            if str(b) == str(a):
                count+=1
            frequencies[str(a)] = count

    return frequencies
