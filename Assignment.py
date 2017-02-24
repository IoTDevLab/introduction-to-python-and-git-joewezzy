## Template
#!/usr/bin/env python3

# Name: <Joshuah Marbell>
# Index number: <PS/ITC/14/0067>

print 'Question 1 \n Answer: '

# TODO: Put your codes here ...

#Creates a variable called line 
line = ""

#Iterate through a number of range from 1000 to 7000
for numbers in range(1000, 7001):
    #Check if numbers is divisible by 7 and not a multiple of 5
    if(numbers % 7 == 0) and (numbers % 5 != 0):
        #Stores Everything on in line variable with comma-sepated
        line += str(numbers) + ", " 
#Prints the line variable
print line, '\n'

print 'Question 2\n Answer: '

total = 0

for numbers in range(2000):
    if(numbers % 3 == 0) or (numbers % 5 == 0):
        total += numbers

print total, '\n'


print 'Question 3\n Answer: '

decimal_value = int(input("Please enter a value: "));


print '{0:b}'.format(int(decimal_value)), '\n'

print 'Question 4\n Answer: '

def EvenFibonacci(n):
    num1 = 1
    num2 = 2
    z = 0
    totalSum =0
    while(num1<=n):
        if(num1%2 ==0):
            totalSum = totalSum + num1
        #print(sum)
        z = num1
        num1 = num2
        num2 = z + num2
    return totalSum

if __name__ == '__main__':
  print EvenFibonacci(4000000), '\n'

print 'Question 5a\n Answer: '

my_input = "0123456789"
Zero = ["****** ", "*    * ", "*    * ", "*    * " , "*    * " , "*    * " , "****** "]
One = ["*      ","*      ","*      ","*      ","*      ","*      ","*      "]
Two = ["****** ", "     * ","     * ", "****** ", "*      ","*      ", "****** "]
Three = ["****** ", "     * ","     * ", "****** ", "     * ","     * ", "****** "]
Four = ["*    * ", "*    * ","*    * " ,  "****** ", "     * ","     * ","     * "]
Five = ["****** ", "*      ","*      " , "****** ", "     * ", "     * ", "****** "]
Six = ["****** ", "*      ","*      " , "****** ", "*    * ", "*    * ", "****** "]
Seven = ["****** ","     * " , "     * ", "     * ", "     * ", "     * ", "     * "]
Eight = ["****** ", "*    * ", "*    * ", "****** ", "*    * " , "*    * " , "****** "]
Nine = ["****** ", "*    * ", "*    * ", "****** ", "     * " , "     * " , "****** "]

Digits = [Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero, One]

# TODO: Print all the digits on the same line
try:
    row = 0
    while row < 7:
        space = ""
        column = 0
        while column < len(my_input):
            # TODO: Put your code after this comment
            
            space += Digits[column][row]            
            column += 1
            
        # TODO: Print line here and add an incrementer
        print space, '\n'
        row += 1   
except:
    # TODO: Handle one suitable error which may occur
    print 'Error!! Please go back to the codes!, \n'

print 'Question 5b\n Answer: '

my_input = "0123456789"
Zero = ["****** ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * " , "*    * " , "*    * " , "****** "]
One = ["*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      "]
Two = ["****** ", "     * ","     * ", "     * ","     * ", "****** ","*      ","*      ","*      ","*      ", "****** "]
Three = ["****** ", "     * ","     * ","     * ","     * ", "****** ", "     * ","     * ","     * ","     * ", "****** "]
Four = ["*    * ", "*    * ","*    * " , "*    * " ,"*    * " ,  "****** ", "     * ","     * ", "     * ","     * ","     * ","     * ","     * "]
Five = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "     * ", "     * ","     * ","     * ", "****** "]
Six = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "*    * ", "*    * ","*    * ","*    * ", "****** "]
Seven = ["****** ","     * " , "     * ", "     * ", "     * ", "     * ","     * ","     * ","     * ","     * ", "     * "]
Eight = ["****** ", "*    * ", "*    * ","*    * ","*    * ", "****** ", "*    * " , "*    * " ,"*    * " ,"*    * " , "****** "]
Nine = ["****** ", "*    * ", "*    * ", "*    * ","*    * ", "****** ", "     * " ,"     * " ,"     * " , "     * " , "****** "]

Digits = [Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero, One]

# TODO: Print all the digits on the same line
try:
    row = 0
    while row < 11:
        line = ""
        column = 0
        while column < len(my_input):
            # TODO: Put your code after this comment
            
            line += Digits[column][row]            
            column += 1
            
        # TODO: Print line here and add an incrementer
        print line, '\n'
        row += 1   
except:
    # TODO: Handle one suitable error which may occur
    print 'Error!! Please go back to the codes!, \n'

raw_input('Press enter to end!')

