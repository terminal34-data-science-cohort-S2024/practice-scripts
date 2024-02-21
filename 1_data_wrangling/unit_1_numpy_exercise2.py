"""
Exercise: Analyzing Monthly Sales Data with NumPy

Objective: You are given a dataset containing monthly sales data (in thousands of units) for a retail store across two years, for three different products. Your task is to use advanced NumPy techniques to analyze this data.

Data:

Sales data format: A 2D NumPy array where rows represent months (first row is January of the first year, last row is December of the second year), and columns represent products (first column is Product A, second is Product B, and third is Product C).

```plaintext
[[120, 135, 145],
[130, 140, 135],
[150, 160, 145],
[170, 165, 155],
[160, 155, 150],
[180, 170, 165],
[190, 180, 175],
[210, 200, 190],
[200, 195, 180],
[220, 210, 205],
[230, 220, 210],
[240, 230, 220],
[250, 240, 230],
[260, 250, 240],
[270, 260, 250],
[280, 270, 260],
[290, 280, 270],
[300, 290, 280],
[310, 300, 290],
[320, 310, 300],
[330, 320, 310],
[340, 330, 320],
[350, 340, 330],
[360, 350, 340]]
```

Tasks:

1. Calculate the total sales for each product over the two years.
2. Find the month with the highest sales for Product C.
3. Calculate the year-over-year (YoY) growth rate in sales for each product (from the first year to the second year).
4. Determine the average monthly sales for each product in the second year.
"""
