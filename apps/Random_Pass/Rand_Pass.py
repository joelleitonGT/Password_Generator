#Random_Pass

import random

lowerCase = "abcdefgjhijklmnopqrstuwyxz"
upperCase = "ABCDEGHHIJKLMNOPQRSTUWXYXZ"

number = "0123456789"
specialCharts = "#@!&*\/.><$%+-"

formatPass = upperCase + upperCase +  specialCharts + specialCharts + number + number  + number + number 

lenghtPass = 8

password = "".join(random.sample(formatPass, lenghtPass))

print("Your new password is: " + password)