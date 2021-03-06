#Installing pip 
# $apt install python3-pip

#Including numers in strings:
print(f"20 days are {20*24*60} minutes") #f means format, doesn't work in python 2x

#User input
user_input = int(input("How many days you want to calculate?"))

#Defining functions
def days_to_seconds (value):
    return print(f"{value} days are {value * 24 * 60 * 60} seconds ") #function may not return anything, it can print text only
    
days_to_seconds(user_input)

#If-else conditionals
if 2>1:
    print("Do something.")       #return may be used
elif 2<1:
    print("Do this.")
else:
    print("Do this.")

