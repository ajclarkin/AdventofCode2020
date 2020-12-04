# Day 1 - Report Repair
## Part 1
Given a list of integers find the two which sum to 2020. Then find the product of those two values.

Last year I avoided using numpy and other libraries. Not this year. Why on earth would you not use numpy?
`np.add.outer` adds every value of two arrays together. Then just find the sum which equals 2020.

```
sum_values = np.add.outer(d1, d1)
loc = np.where(sum_values == 2020)
```


