# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 ==0:
    print(f"Leap Year.")
elif year % 100 ==0:
    print(f"Not Leap.")
elif year % 400 ==0:
    print(f"Leap Year.")

#     Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.
