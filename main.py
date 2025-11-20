from tinygrad import Tensor, Context
a = Tensor.empty(4,4)
b = Tensor.empty(4,4)

print((a+b).tolist())
print((a*b).tolist())
print((a.sum(0)).tolist())