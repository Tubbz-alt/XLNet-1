import numpy as np 
max_gram = 5
ngrams = np.arange(1, max_gram + 1, dtype=np.int64)
pvals = 1. / np.arange(1, max_gram + 1)
# pvals /= pvals.sum(keepdims=True)

# print(ngrams)
# print(pvals)

print(pvals.sum(keepdims = True))