# Training the Little Language Model for FizzBuzz
from FizzBuzz import fizzbuzz
import torch
import torch.nn.functional as F
import string
import itertools

SAMPLE_LEN = len('99 FizzBuzz ')
DEVICE = 'mps'
SIZE = 10

alphabet = ' ' + string.digits + string.ascii_lowercase + string.ascii_uppercase

data = [f'{num} {fizzbuzz(num)} ' for num in range(1, 100)]
data = [sample + ' ' * (SAMPLE_LEN - len(sample)) for sample in data]
data = torch.tensor([[alphabet.index(ch) for ch in sample] for sample in data])

class OnlyOutputsPlease(torch.nn.Module):
    def forward(self, x): # I can't believe I have to do this
        outputs, (h, c) = x
        return outputs

try:
    model = torch.load('charlm.pt')
except FileNotFoundError:
    model = torch.nn.Sequential(
        torch.nn.Embedding(len(alphabet), SIZE),
        torch.nn.LSTM(input_size=SIZE, 
                      hidden_size=SIZE, batch_first=True),
        OnlyOutputsPlease(),
        torch.nn.Linear(SIZE, len(alphabet))
    )

optimizer = torch.optim.AdamW(model.parameters(), amsgrad=True)
model = model.to(DEVICE)
data = data.to(DEVICE)

try:
    for epoch in itertools.count():
        optimizer.zero_grad()
        logits = model(data[:, :-1])
        loss = F.cross_entropy(logits.transpose(2, 1), data[:, 1:])
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch} loss: {loss.item()}')
finally:
    torch.save(model, 'charlm.pt')