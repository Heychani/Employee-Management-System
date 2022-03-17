employee_num = input("Please enter your employee number: ")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
salary = float(input("Please enter your current salary: "))


def get_updated_salary(salary):
    return salary + (0.1 * salary)


def print_details(employee_num, first_name, last_name, salary):
    print("Employee Details Report")
    print("*********************************************************")
    print(f"Employee Number: {employee_num}")
    print(f"Employee First name: {first_name}")
    print(f"Employee Surname: {last_name}")
    print(f"Original Salary: {salary}")
    print(f"Increased salary: {get_updated_salary(salary)}")
    print("*********************************************************")


def salary_deductions():
    increased_salary = get_updated_salary(salary)
    print("Employee deductions report")
    print("*********************************************************")
    print(f"Salary: {salary}")
    tax = increased_salary * 0.18
    print(f"Tax: {tax}")
    medical_aid = increased_salary * 0.125
    print(f"Medical aid: {medical_aid}")
    car_allowance = increased_salary * 0.08
    print(f"Car allowance: {car_allowance}")
    uif = increased_salary * 0.02
    print(f"UIF: {uif}")
    take_home_pay = salary - (uif + car_allowance + medical_aid + tax)
    print(f"Take home pay: {take_home_pay}")
    print("*********************************************************")


print_details(employee_num, first_name, last_name, salary)

choice = input("Would you like to see the increased salary deductions? Enter (1) to view the deductions report or any "
               "other key to exit: ")

if choice == '1':
    salary_deductions()
else:
    print("*********************************************************")

print("Application Complete")
