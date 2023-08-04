coach_cost = 550.00
entry_ticket = 30.00
student_cost = 0
total_student_payment = 0
student_pay_list = [],[]

student_num = int(input("How many students are going for the trip? >>>"))
if student_num > 45:
    print("\n""There must be not more than 45 students.")
elif student_num < 1:
    print ("\n""You must have at least 1 student.")
else:
    print("\n""You have", student_num, "students.")
    student_cost = round((coach_cost/student_num)+entry_ticket)
    print("Each student will pay a total of $",student_cost, ".")
  
    for i in range(student_num):
      student_name=input("\n""What is your name?")
      student_pay_list[0].append(student_name)
      print(student_pay_list)
      student_payment = float(input("\n""How much have you paid? >>>"))
      student_pay_list[1].append(student_payment)

      
      total_student_payment +=student_payment
      
      if student_payment < student_cost:
        print("\n""You have not paid the total amount. You are $", student_payment-student_cost," short.")
      else:
        print("\n""Please proceed.")
    
    if total_student_payment > student_cost*student_num:
      print("\n""The school has made a profit of $", total_student_payment - student_cost*student_num,".")
    elif total_student_payment < student_cost*student_num:
      print("\n""The school has made a loss of $", total_student_payment - student_cost*student_num,".")
    else:
      print("\n""The school has paid the exact amount.")
