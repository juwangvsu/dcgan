import torch
x = torch.ones(2, 2, requires_grad=True)
y = x + 2

y.backward(torch.ones(2, 2)) # backword will at each node calculate d(Loss)/d(x)Note I do not set retain_graph=True
y.backward(torch.ones(2, 2)) # But it can still work! this will add to existing x.grad
print (x.grad)
y.backward(torch.ones(2, 2)) # But it can still work!
print (x.grad)
