import numpy as np
sales = np.array([
    [12000, 15000, 13000],   # Jan
    [14000, 16000, 15500],   # Feb
    [17000, 16500, 16000],   # Mar
    [18000, 17500, 17000]    # Apr
])
print("Total sales per month:", np.sum(sales,axis=1))
print("Total sales per product:", np.sum(sales,axis=0))
print("Best-selling product overaller product:", np.argmax(sales,axis=0))
max=np.argmax(np.sum(sales,axis=1))
print("Month with highest total sales:", max)
print("Percentage contribution of each product:", (np.sum(sales,axis=0)/np.sum(sales))*100)