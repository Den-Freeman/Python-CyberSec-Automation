# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network
  connection_attempts = 10
# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`
  for i in range(connection_attempts):
      print("Connection could not be established")


# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network
  connection_attempts = 0
# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number
  while connection_attempts < 5:
      print("You can still try and log in")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration) 
      connection_attempts = connection_attempts + 1


# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
  ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For loop that displays the elements of `ip_addresses` one at a time
  for i in ip_addresses:
      print(f"Address in list: {i}")


# Assign `allow_list` to a list of IP addresses that are allowed to log in
  allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
  ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
  for i in ip_addresses:
	  if i in allow_list:
	  	print("IP address is allowed")
	  else:
		  print("IP address is not allowed")


# Assign `allow_list` to a list of IP addresses that are allowed to log in
  allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
  ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”           
  for i in ip_addresses:
  	if i in allow_list:
	  	print("IP address is not allowed")
	  else:
		  print("IP address is not allowed. Further investigation of login activity required")
		  break


#Explanation:
    #The loop starts at 5000 and continues while i is less than or equal to 5150.
    #Each iteration, i is incremented by 5 to ensure the IDs are divisible by 5.
    #The code prints the newly created employee ID in each iteration.

# Assign the loop variable `i` to an initial value of 5000
  i = 5000
# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
  while i <= 5150:
      print(f"New employee ID created: {i}")
      i += 5  # Increment by 5 to ensure divisibility by 5



