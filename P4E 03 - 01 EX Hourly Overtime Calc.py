hours = int(input("Enter Hours:"))
rate = int(input("Enter Rate:"))
if hours > 40:
    overtime_hours = hours - 40
    overtime_extra = overtime_hours * 15
    pay = overtime_extra + 400
    print(pay)
else:
    pay = hours * rate
    print(pay)