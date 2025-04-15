#NUMBERCAL COMPARISONS
age = 18
age == 18

answer = 17
if answer != 42:
    print("That answer is not the correct answer. Please try again!")

# the conditional test passes, bc the answer is not equal to 42.
# because the test passes, the indented code block is executed.

age = 19
age < 21
age <= 21
age > 21
age >= 21

#CHECKING MULTIPLE CONDITIONS
#using 'and'
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 22
age_0 >= 21 and age_1 >= 21

#parentheses are optional, but can improve readability
(age_0 >= 21) and (age_1 >= 21)

#using 'or'
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
age_0 =18
age_0 >= 21 or age_1 >= 21