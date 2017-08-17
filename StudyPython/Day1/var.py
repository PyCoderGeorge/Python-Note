# Author: Junting

name = input("name: ")
age = input("age: ")
job = input("job: ")
salary = input("salary: ")

info = '''
---------- info of -------------
Name: %s
Age: %s
Job: %s
Salary: %s
'''%(name, age, job, salary)

info2 = '''
---------- info of {_name}-------------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

print(info2)
