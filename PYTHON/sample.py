marks=float(input("Enter marks:")) 
if marks >= 80:
    print("First Class with Distinction")
elif marks >= 60 and marks < 80:
    print("First Class")
elif marks >= 50 and marks < 60: 
    print("Second Class")
elif marks >= 35 and marks < 50: 
    print("Third Class")