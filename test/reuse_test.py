import torch
data = torch.rand(1, 10)
print(data)
reuse_len = 3
seq_len = 3
i = 0
data_len = data.shape[1]
while i + seq_len <= data_len:
	inp = data[0, i : i + reuse_len]
	print(inp)
	i += reuse_len
