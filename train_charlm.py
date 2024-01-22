# Training the Little Language Model for FizzBuzz
from FizzBuzz import fizzbuzz
import torch
import torch.nn.functional as F
from charlm import CharLSTM, alphabet
import itertools
import sys

DEVICE = sys.argv[1]
SAMPLE_LEN = len('99 FizzBuzz ')

data = [f'{num} {fizzbuzz(num)} ' for num in range(1, 100)]
data = [sample + ' ' * (SAMPLE_LEN - len(sample)) for sample in data]
data = torch.tensor([[alphabet.index(ch) for ch in sample] for sample in data])

model = CharLSTM().to(DEVICE)
data = data.to(DEVICE)

optimizer = torch.optim.AdamW(model.parameters(), amsgrad=True)

try:
    for epoch in itertools.count():
        optimizer.zero_grad()
        logits = model(data[:, :-1])
        loss = F.cross_entropy(logits.transpose(2, 1), data[:, 1:])
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch} loss: {loss.item()}')
finally:
    torch.save(model.state_dict(), 'charlm.pt')