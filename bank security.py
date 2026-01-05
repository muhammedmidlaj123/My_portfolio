import random
transaction=[50, 1200, 30, 450, 2000, 90]
admin_name =input("enter your admin name ")

suspicious_count=0

def audit_transactions(transaction):
   global  suspicious_count
   for item in transaction:
        if item >= 1000:
            suspicious_count += 1
            print(f"Suspicious: {item}")

        else:
            print(f"Not suspicious: {item}")
audit_transactions(transaction)

if suspicious_count >1:
    print("emergency alert")
else:
    security_code=random.randint(1000,9999)
    print(f"System Clean. Welcome {admin_name}. Your Token: {security_code}.")