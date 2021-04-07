try:
    #something that might cause an exception
    file = open("a_file.txt")


except KeyError: #you want to make sure except isnt bare. always have a FileNOtFound or KeyError etc...
    #do this if there was an exception

#you can also make except even more specific
except KeyError as error_message:
    print(f"the key {error_message} does not exist")


else:
    #do this if nothing went wrong in try


finally:
    #do this no matter what happens
    file.close()

#you can raise your own errors for example if someone entered they were 15Ft tall on a BMI Calculator
#no one should be over 8 feet tall so

if height > 8:
    raise ValueError("No one should be over 8 feet tall")

