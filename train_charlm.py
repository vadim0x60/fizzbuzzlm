# Training the Little Language Model for FizzBuzz
from FizzBuzz import fizzbuzz
import torch
import torch.nn.functional as F
import string

SAMPLE_LEN = len('99 FizzBuzz ')
EPOCHS = 300000
DEVICE = 'mps'
SIZE = 10

alphabet = ' ' + string.digits + string.ascii_lowercase + string.ascii_uppercase

data = [f'{num} {fizzbuzz(num)} ' for num in range(1, 100)]
data = [sample + ' ' * (SAMPLE_LEN - len(sample)) for sample in data]
data = torch.tensor([[alphabet.index(ch) for ch in sample] for sample in data])

model = torch.nn.LSTM(input_size=SIZE, 
                      hidden_size=SIZE, batch_first=True)
embedding = torch.nn.Embedding(len(alphabet), SIZE)
optimizer = torch.optim.AdamW(model.parameters(), amsgrad=True)

model, embedding, data = [t.to(DEVICE) for t in [model, embedding, data]]

for epoch in range(EPOCHS):
    model.zero_grad()
    output, _ = model(embedding(data[:, :-1]))
    loss = F.cross_entropy(output.transpose(2, 1), data[:, 1:])
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch} loss: {loss.item()}')

torch.save(model, 'charlm.pt')
torch.save(embedding, 'embedding.pt')

