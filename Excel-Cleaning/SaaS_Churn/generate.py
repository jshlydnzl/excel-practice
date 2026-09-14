import csv
import random
from datetime import datetime, timedelta

def get_date():
    return datetime(2023, 1, 1) + timedelta(days=random.randint(0, 700))

with open('/home/jshlydnzl/Projects/eksel-praktis/SaaS_Churn/saas_raw_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Cust_ID', 'Company ', 'Plan', 'Monthly_Rev', 'JoinDate', 'Status '])
    
    for i in range(1, 1001):
        cid = f"C-{random.randint(1000,9999)}" if random.random() > 0.05 else "" # Ghost blank
        company = f"Corp_{i}"
        plan = random.choice(['Basic', 'Pro', 'Enterprise', '  Pro  ', 'enterprise']) # String trap
        
        rev = random.choice([29, 99, 499])
        if random.random() > 0.8: rev = f"${rev}.00" # Text trap
        elif random.random() > 0.9: rev = f"{rev} USD"
        
        date = get_date().strftime('%Y/%m/%d') if random.random() > 0.5 else get_date().strftime('%d-%b-%Y')
        status = random.choice(['Active', 'Churned', 'Paused', '  Active '])
        
        row = [cid, company, plan, rev, date, status, "", ""] # Ghost columns
        w.writerow(row)
        if random.random() > 0.98: w.writerow(row) # Duplicates

print("Created SaaS dirty data.")
