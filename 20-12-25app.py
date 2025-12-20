# file=open('example.txt','a')
# file.write('to continue the previous text')
# file.close()

# with open('example.txt','a') as file:
#     file.write('to work with keyword')

# file = open("C:\Users\shiva\Downloads\Advertising.csv.xlsx", "r")
# file.write
# file.close()

#Exception Handling
#try,except,finallyb 
# try:
#     x = int("str")  
#     inv = 1 / x   
    
# except ValueError:
#     print("Not Valid!")
    
# except ZeroDivisionError:
#     print("Zero has no inverse!")

# try:
#     a = 10/0
#     print(a)
# except ZeroDivisionError:
#     print("you are diving values with 0")
#     print('python class')

# try:
#     a = 10/0
#     print(a)
# except Exception as e:
#     print(e)
#     print('python class')

from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "this is the first route"

app.run(use_reloader=True)
