def grade(mark):
   
   if mark >= 90:
            return 'A'
   elif mark >= 80:
            return 'B'
   elif mark >= 70:
            return 'C'
   elif mark >= 60:
            return 'D'
   else:
            return 'F'


try:
    mark = int(input("Enter mark (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid input! Marks should be between 0 and 100.")

    else:
        print("Grade:", grade(mark))

except ValueError:
    print("Invalid input! Please enter a valid number.")
