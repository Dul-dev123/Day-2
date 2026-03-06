while True:
    name = input("\nEnter student's name (or type 'Exit' to stop): ")
    
    if name.lower() == 'exit':
        print("Goodbye!")
        break

    marks = []
    for i in range(1, 4):
        while True:
            try:
                m = float(input(f"Enter mark {i}: "))
                # Logic to reject negative numbers or numbers above 100
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Invalid input! Please enter a mark between 0 and 100.")
            except ValueError:
                print("That's not a number! Please enter a valid mark.")

    average = sum(marks) / 3
    print(f"Average Score: {average:.2f}")

    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student: {name} | Grade: {grade}")