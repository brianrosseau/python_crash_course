def greeter_info():                     #function definition with no info in ()
    """Display a simple greeting."""    #docstring describes what the function does
    print("Hello!")                     #body of the function

greeter_info()                          # Call the function

# the output is: Hello!

# modify the function by adding information inside the ()
def greeter_info(username): #'username' is the parameter # when writing a function, the information in the () is called a parameter
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greeter_info('jesse')    #'jesse' is the argument   #when calling a function, the information that is passed to the function is called an argument

# output is: Hello, Jesse!

