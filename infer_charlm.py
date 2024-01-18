import torch
import string

DEVICE = 'mps'
SAMPLE_LEN = len('99 FizzBuzz ')

alphabet = ' ' + string.digits + string.ascii_lowercase + string.ascii_uppercase

model = torch.load('charllm.pt')
embedding = torch.load('embedding.pt')

model, embedding = [t.to(DEVICE) for t in [model, embedding]]

def sample(context):
    context = torch.tensor([[alphabet.index(ch) for ch in context]])
    text = ''
    
    for _ in range(SAMPLE_LEN - len(context)):
        output, _ = model(embedding(context.to(DEVICE)))
        output = torch.argmax(output, dim=2)
        text += alphabet[output[0,-1]]

    return text

if __name__ == '__main__':
    for i in range(1, 100):
        print(sample(str(i)))