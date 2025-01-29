# Correct Indentation
  def alert():
      print("Security issue detected.")
  alert()


# Define a function named `alert()`
  def alert(): 
      for i in range(3):
          print("Potential security issue. Investigate further.")
# Call the `alert()` function
  alert()


# Define a function named `list_to_string()`
  def list_to_string():
# Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
# Write a for loop that iterates through the elements of `username_list` and displays each element
  for i in username_list:
        print("Prints each element")
# Call the `list_to_string()` function
    list_to_string()


# Define a function named `list_to_string()`
  def list_to_string():
# Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
# Assign `sum_variable` to an empty string
    sum_variable = ""
# Write a for loop that iterates through the elements of `username_list` and displays each element
    for i in username_list:
      sum_variable = sum_variable + i + ", "
# Display the value of `sum_variable`
    print(sum_variable)
# Call the `list_to_string()` function
    list_to_string()

#-------------------------------------------------------------------------------------------------------------------
#BUILT IN FUNCTIONS


# Assign `failed_login_list` to the list of the number of failed login attempts per month
  failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
# Sort `failed_login_list` in ascending numerical order and display the result
  print(sorted(failed_login_list))


# Assign `failed_login_list` to the list of the number of failed login attempts per month
  failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
# Determine the highest number of failed login attempts from `failed_login_list` and display the result
  print(max(failed_login_list))


# Define a function named `analyze_logins()` that takes in two parameters, `username` and `current_day_logins`
  def analyze_logins(username, current_day_logins):
    # Display a message about how many login attempts the user has made that day
      print("Current day login total for", username, "is", current_day_logins)
# Call `analyze_logins()`
  analyze_logins("ejones", 9)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
  def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
      print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
      print("Average logins per day for", username, "is", average_day_logins)
  # Call `analyze_logins()`
  analyze_logins ("ejones", 9, 3)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = (current_day_logins / average_day_logins)
    # Display a message about the ratio
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")
# Call `analyze_logins()`
analyze_logins("ejones", 9, 3)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
  def analyze_logins(username, current_day_logins, average_day_logins):
# Display a message about how many login attempts the user has made that day
      print("Current day login total for", username, "is", current_day_logins)
# Display a message about average number of login attempts the user has made that day
      print("Average logins per day for", username, "is", average_day_logins)
# Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
      login_ratio = current_day_logins / average_day_logins
# Return the ratio
      return login_ratio
# Call `analyze_logins() and store the output in a variable named `login_analysis`
  login_analysis = analyze_logins("ejones", 9, 3)
# Conditional statement that displays an alert about the login activity if it's more than normal
  if login_analysis > 1:
    print("Alert! This account has more login activity than normal.")



