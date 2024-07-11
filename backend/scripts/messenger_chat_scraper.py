from selenium import webdriver


user_dict = {"email":"", "password":""}
def get_user_messages():
    driver = webdriver.Firefox()
    driver.get("https://www.messenger.com/t/1677283615668638")

# gets the users information for logging in 
def get_user_information():
    email = input("Enter email")
    #will not be stored without encryption
    password = input("enter password")
    user_dict.email = email
    user_dict.password = password

    return user_dict




get_user_messages()
userinformation = get_user_information()
# use command line arguemnts to get user password and email
# exrtypt the pasword
# dycrypt the password and pass it into the form 
# grab text and store  [{{user1: {time, text, }},}] -> format the data and pass it in to gpt model only up to point where user has not responded
# test

#TODO(ak): make a diagram for db schema and create a project chart
