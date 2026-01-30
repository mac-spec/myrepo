import numpy as np
# problem-1

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

#Problem-2
scores = np.array([
    [85, 78, 92],
    [60, 65, 70],
    [90, 88, 95],
    [72, 75, 68],
    [88, 80, 85]
])
print("Average score per student:", np.mean(scores, axis=1))
print("Average score per subject:", np.mean(scores, axis=0))
print("Index of top performer:", np.argmax(np.sum(scores, axis=1)))
print( "Count of students scoring above 80 in all subjects:",np.sum(np.all(scores > 80, axis=1)))


#Problem -3
spending = np.array([
    [2000, 2500, 1800, 2200],
    [1500, 1600, 1700, 1650],
    [3000, 3200, 3100, 3300],
    [800,  900,  850,  950],
    [2600, 2700, 2650, 2800]
])
print("Total spending per customer", np.sum(spending,axis=1))
print("Average spending per monthr", np.mean(spending,axis=0))
c=spending[np.sum(spending,axis=1)>10000]
print("Identify VIP customers (total spending > 10,000)", c )
vip_count = c.shape[0]
total_customers = spending.shape[0]
percentage_vip = (vip_count / total_customers) * 100
print("Percentage of customers who are VIP:", percentage_vip)

#Problem-4
sensor = np.array([
    [72, 75, 78, 80, 76, 74],
    [68, 70, 69, 71, 72, 70],
    [90, 92, 95, 93, 94, 96],
    [65, 66, 64, 67, 66, 65],
    [85, 88, 90, 89, 87, 86]
])
print("Average temperature per machine",np.mean(sensor,axis=1))
avg_temp= np.mean(sensor, axis=1)
print("Identify faulty machines",sensor[avg_temp > 85])
print("Count faulty machines", np.sum(avg_temp > 85))
print("Find peak temperature recorded overall",np.max(sensor))

#problem-5
employees = np.array([
    [220, 1, 60],
    [180, 5, 85],
    [250, 2, 55],
    [200, 10, 90],
    [230, 3, 65],
    [170, 8, 88]
])
print("At-risk employees",employees[(employees[:, 0] > 210) & (employees[:, 2] < 70)])
print("Count at-risk employees",employees[(employees[:, 0] > 210) & (employees[:, 2] < 70)].shape[0])
print("Percentage of workforce at risk",(employees[(employees[:, 0] > 210) & (employees[:, 2] < 70)].shape[0]/ employees.shape[0]) * 100)

# mini project
employees = np.array([
    [220, 1, 60, 40],
    [180, 5, 85, 60],
    [250, 2, 55, 35],
    [200, 10, 90, 80],
    [230, 3, 65, 45],
    [170, 8, 88, 70],
    [260, 1, 50, 30],
    [190, 6, 78, 55]
])
""" Business Objectives
1. Workforce Overview (KPIs)

Average working hours

Average performance score

Average salary

2. Attrition Risk Identification

Employee is high risk if:

Hours > 220

Performance < 65

3. High Performers

Performance ≥ 85

AND salary < company average salary
(Potential retention risk)

4. management Insights

Answer with NumPy:

% employees at attrition risk

% high performers underpaid

Max & Min salary

Correlation between hours & performance"""
#WORKFORCE OVERVIEW
print("Average working hours",np.mean(employees[:,0]))
print("Average performance score",np.mean(employees[:,2]))
print("Average salary",np.mean(employees[:,3]))
#Attrition Risk Identification
print("Employee is at high risk:",(employees[(employees[:,0]>220)&(employees[:,2]<65)]))
#High performance
print("Potential retention risk",employees[(employees[:,2]>=85)&(employees[:,3]<np.mean(employees[:,3]))])
#Management Insights
print("Percentage of employees at attrition risk",((((employees[(employees[:,0]>220)&(employees[:,2]<65)]).shape[0]))/employees.shape[0])*100)
print("Maximum salary:", np.max(employees[:,3]))
print("Minimum salary:", np.min(employees[:,3]))
corr = np.corrcoef(employees[:,0], employees[:,2])[0,1]
print("Correlation between hours & performance:", corr)
