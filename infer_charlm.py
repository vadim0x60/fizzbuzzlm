import torch
import string
import sys
import numpy as np
from charlm import CharLSTM

DEVICE = sys.argv[1]
SAMPLE_LEN = len('99 FizzBuzz ')

alphabet = ' ' + string.digits + string.ascii_lowercase + string.ascii_uppercase

model = CharLSTM().to(DEVICE)

def sample(text):    
    offset = len(text)
    intensor = torch.tensor([[alphabet.index(ch) for ch in text]]).to(DEVICE)
    while len(text) < SAMPLE_LEN:
        outtensor = model(intensor)
        pred = outtensor[0,-1].argmax()
        intensor = torch.hstack([intensor, pred.reshape((1, 1))])
        text += alphabet[outtensor[0,-1].argmax()]

    return text[offset:]

if __name__ == '__main__':
    for i in range(1, 100):
        print(sample(f'{i} '))