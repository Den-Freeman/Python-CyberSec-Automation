# Ahh s%$* here we go again
  print("Sample string print")


# This will be 0
  print(1//4)


# This will be 0.0
  print(1.0//4.0)


# TUPLE:
# data is a data structure that consists of a collection of data that cannot be changed. Like lists, tuples can contain elements of varying data types. 
# a difference between tuple data and list data is that it is possible to change the elements in a list, but it is not possible to change the elements in a tuple. This could be useful in a cybersecurity context.
# TUPLES are more memory efficient than lists, so they are useful when you are working with a large quantity of data.
# a TUPLE is placed in parentheses() rather than brackets[]. These are all examples of the tuple data type:
  ("wjaffrey", "arutley", "dkot")
  ("wjaffrey", 13, True)


# SET:
# In Python, set data is data that consists of an unordered collection of unique values. This means no two values in a set can be the same. 
# Elements in a set are always placed within curly brackets and are separated by a comma.
# These elements can be of any data type. This example of a set contains strings of usernames:
  {"jlanksy", "drosas", "nmason"}


# The following code demonstrates how a username can be updated. The username variable is assigned an initial value, which is then stored in a second variable called old_username.
# After this, the username variable is reassigned a new value. You can run this code to get a message about the previous username and the current username:
  username = "nzhao"
  old_username = username
  username = "zhao2"
  print("Previous username:", old_username)
  print("Current username:", username)


# Assign the `device_id` variable to the device ID that only specified users can access
  device_id = "72e08x0"
# Assign `device_id_type` to the data type of `device_id`
  device_id_type = type(device_id)
# Display `device_id_type`
  print(device_id_type)


# Assign `username_list` to the list of usernames who are allowed to access the device
  username_list = (["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"])
# Display `username_list`
  print(username_list)


# Assign `username_list` to the list of usernames who are allowed to access the device
  username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Assign `username_list_type` to the data type of `username_list`
  username_list_type = type(username_list)
# Display `username_list_type`
  print(username_list_type)


# In this task, reassign the variable username_list to the new list. Run the code to display the list before and after it's been updated to observe the difference.
# Assign `username_list` to the list of usernames who are allowed to access the device
  username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Display `username_list`
  print(username_list)
# Assign `username_list` to the updated list of usernames who are allowed to access the device
  username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]
# Display `username_list`
  print(username_list)


# In this task, define a variable called max_logins that represents the maximum number of login attempts allowed per user.
# Store the value 3 in this variable. Then, store its data type in another variable called max_logins_type.
# Display max_logins_type to examine the output.
# Assign `max_logins` to the value 3
  max_logins = 3
# Assign `max_logins_type` to the data type of `max_logins`
  max_logins_type = type(max_logins)
# Display `max_logins_type`
  print(max_logins_type)


# In this task, you'll determine the Boolean value that represents whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed.
# Assign `max_logins` to the value 3
  max_logins = 3
# Assign `login_attempts` to the value 2
  login_attempts = 2
# Determine whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed,
# and display the resulting Boolean value
  print(max_logins <= login_attempts)


# In this task, you'll create a variable called login_status, which is a Boolean that represents whether a user is logged in.
# Assign False to this variable and store its data type in a variable called login_status_type and display it.
# Assign `login_status` to the Boolean value False
  login_status = False
# Assign `login_status_type` to the data type of `login_status`
  login_status_type = type(login_status)
# Display `login_status_type`
  print(login_status_type)


#----------------------------------------------------------------------------


# Assign a variable named `system` to a specific operating system, represented as a string
# This variable indicates which operating system is running
  system = "OS 2"
# If OS 2 is running, then display a "no update needed" message
  if system == "OS 2":
      print("no update needed")


#IF + ELSE
# Assign `system` to a specific operating system
# This variable represents which operating system is running
  system = "OS 5"
# If OS 2 is running, then display a "no update needed" message
# Otherwise, display a "update needed" message
  if system == "OS 2":
      print("no update needed")
  else:
      print("update needed")


#IF + ELIF
# Assign `system` to a specific operating system
# This variable represents which operating system is running
  system = "OS 3"
# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message
  if system == "OS 2":
      print("no update needed")
  elif system == "OS 1":
      print("update needed")
  elif system == "OS 3":
      print("update needed")


#ELIF + OR
# Assign `system` to a specific operating system
# This variable represents which operating system is running
  system = "OS 1"
# If OS 2 is running, then display a "no update needed" message
# Otherwise if either OS 1 or OS 3 is running, display a "update needed" message
  if system == "OS 2":
      print("no update needed")
  elif system == "OS 2" or "OS 3":
      print("update needed")


#IF + OR + ELSE
#You'll start with two authorized users, stored in the variables approved_user1 and approved_user2.
#You'll need to write a conditional statement that compares those variables to a third variable, username.
#This will be the username of a specific user trying to log in.
# Assign `approved_user1` and `approved_user2` to usernames of approved users
  approved_user1 = "elarson"
  approved_user2 = "bmoreno"
# Assign `username` to the username of a specific user trying to log in
  username = "bmoreno"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
  if username == approved_user1 or username == approved_user2:
      print("This user has access to this device.")
  else:
      print("This user does not have access to this device.")


#IF + IN [list] + ELSE
#The in operator in Python can be used to determine whether a given value is an element of a sequence.
#Using the in operator in a condition can help you check whether a specific username is part of a list of approved usernames.
#For example, in the code below, username in approved_list evaluates to True if the value of the username variable is included in approved_list.
# Assign `approved_list` to a list of approved usernames
  approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `username` to the username of a specific user trying to log in
  username = "bmoreno"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
  if username in approved_list:
      print("User is legit, welcome!")
  else: 
      print("Do not have access to this device!")


#IF + BOOLEAN + ELSE
# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
  organization_hours = False
# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
  if organization_hours == True:
     print("Login attempt made during organization hours.")
  else:
     print("Login attempt made outside of organization hours.")


#IF + IN [list] + BOOLEAN + ELSE
#It includes the conditional statement that checks if a user is on the allow list and the conditional statement that checks if the user logged in during organization hours.
# Assign `approved_list` to a list of approved usernames
  approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `username` to the username of a specific user trying to log in
  username = "bmoreno"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
  if username in approved_list:
      print("This user has access to this device.")
  else:
      print("This user does not have access to this device.")
# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
  organization_hours = True
# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
  if organization_hours == True:
      print("Login attempt made during organization hours.")
  else:
      print("Login attempt made outside of organization hours.")


#You can also provide a single message about the login attempt.
#To do this, you can join both conditions into a single conditional statement using a logical operator. This will make the code more concise.
# Assign `approved_list` to a list of approved usernames
  approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `username` to the username of a specific user trying to log in
  username = "bmoreno"
# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
  organization_hours = True
# If the user is among the approved users and they are logging in during organization hours, then convey that the user is logged in
# Otherwise, convey that either the username is not approved or the login attempt was made outside of organization hours
  if username in approved_list and organization_hours == True:
      print("Login attempt made by an approved user during organization hours.")
  else:
      print("Username not approved or login attempt made outside of organization hours.")
