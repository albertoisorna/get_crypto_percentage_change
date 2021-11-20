# get_crypto_percentage_change
what is the probability to see a drop of Bitcoin of 10% in one day? 

## 1 -- get probability of a percentage change in an interval
### example: what is the prbability that bitcoin drops 10% in 1day?
a = get_pchange(letter='BTC-USD', value=-10, interval="1d")
print(a)

## 2 -- get probability of a percentage change
### example: what is the prbability that bitcoin drops 10%?
b = get_all_intervals(letter='BTC-USD', value=-10)
print(b)

## 3 -- get matrix of probability
### example: what are probabilities of changes for Bitcoin?
c = get_matrix_change('BTC-USD')
print(c)
