import torch
from torch import nn
import string

SIZE = 10

alphabet = ' ' + string.digits + string.ascii_lowercase + string.ascii_uppercase

def CharLSTM():
    lstm = nn.LSTM(input_size=SIZE, hidden_size=SIZE, batch_first=True)
    lstm.register_forward_hook(lambda module, i, o: o[0])

    model = nn.Sequential(
        nn.Embedding(len(alphabet), SIZE),
        lstm,
        nn.Linear(SIZE, len(alphabet))
    )

    try:
        model.load_state_dict(torch.load('charlm.pt'))
    except FileNotFoundError:
        pass  

    return model