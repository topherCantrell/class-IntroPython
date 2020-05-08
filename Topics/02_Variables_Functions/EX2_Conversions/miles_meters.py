# Input and conversion in one step
feet = float(input('Number of feet: '))

miles = feet/5280 # 5,280 feet per mile

print(feet,'feet is',miles,'miles')

meters = feet * 0.3048 # Found this on the web

print(feet,'feet is',meters,'meters')