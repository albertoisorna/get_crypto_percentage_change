# get_crypto_percentage_change
what is the probability to see a drop of Bitcoin of 10% in one day? 

```
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from utils import get_matrix_change

# make the calculus
letter = 'BTC-USD'
df = get_matrix_change(letter)

# plot
plt.figure()
plt.title(f"% Changes of {letter} probability")

plot_conf = {
    "vmin":0, 
    "vmax":100, 
    "annot":True, 
    "linewidths":.5, 
    "cmap":"YlGnBu"
}

sns.heatmap(df, **plot_conf)
```

![image](https://user-images.githubusercontent.com/23259650/142741554-f6ff81e6-0cd2-4d27-b4c0-fa3902018e13.png)

## The probability is of 1% (36 times in 366 days)
