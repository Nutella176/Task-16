# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program") #Syntax Error: brackets missing
print("\n") #Syntax Error: indent not needed before print. Syntax Error: brackets missing enclosing "\n"

ageStr = "24" #I'm 24 years old. #Syntax Error: indent not needed before ageStr. Syntax Error: ageStr is not defined as == entered instead of =
age = int(ageStr) #Syntax Error: indent not needed before age. Runtime error: can't cast ageStr into integer as it included 'years old' therefore 'years old' removed from line above 
print("I'm " + ageStr + " years old.") #Syntax Error: indent not needed before print. Runtime Error: can't contatenate str to int, so used ageStr instead. Spaces also added after "I'm" and before "years old"
three = 3 #Syntax Error: indent not needed before three. Also variable name could be improved(i.e. added_years). Quatation marks removed as explained on line 14

answerYears = age + three #Syntax Error: indent not needed before answerYears. Runtime Error: as 3 was in quotation marks, it couldn't sum str with int

print("The total number of years:" + str(answerYears)) #Syntax Error: Brackets missing. Logical error: there should be no quotation marks around integer 'answerYears' and it needs to be cast to str to return the desired output
answerMonths = answerYears * 12 + 6 #Runtime Error: name 'answer' is not defined, it should be 'answerYears'. Logical error: 6 months need to be added
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") #Syntax Error: Brackets missing. Runtime Error: trying to concatename integer answerMonths with str

#HINT, 330 months is the correct answer

