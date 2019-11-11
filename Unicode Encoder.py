# Encoder.py

def encode():
    print("This program turns your simple statement into a super secret code")
    state = input("Please enter your statement: ")
    for ch in state:
        print(ord(ch), end=' ')
encode()
