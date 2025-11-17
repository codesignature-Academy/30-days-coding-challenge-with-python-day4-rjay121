num = int(input("Enter a number "))
number = num % 2
print(number)

name = input("Enter your name ")
age = int(input("Enter your age "))
if age > 18:
    print("You are eligible to vote")
else:
    print("Ypu are not eligible to vote")

    

score = int(input("Enter your score "))
if score >= 70:
    print("grade: A")
elif score >= 60:
    print("grade: B")
elif score >= 50:
    print("grade: C")
elif score >= 45:
    print("grade: D")
else:
    print("grade: F")




dept_and_cutoffs = {
    "Medicine": 250,
    "Public health": 230,
    "Nursing": 230,
    "Anatomy": 230,
    "Med-lab": 230,
    "Optometry": 240,
    "Physiology": 230,
    "Microbiology": 200
}
Score = int(input("Enter your Jamb score: "))
department = input("Enter your department ").capitalize()

if department not in dept_and_cutoffs:
    print("Invalid department")
else:
    if Score >= dept_and_cutoffs[department]:
        print("Congratulations, you're admitted into", department +"!")
    else:
        print("Sorry, you're not admitted")


