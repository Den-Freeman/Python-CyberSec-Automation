# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"
# First line of the `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, 'r') as file:
    log_content = file.read()
# Now the content of the file is stored in the `log_content` variable.


# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"
# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store the result in a variable named `text`
  text = file.read()
# Display the contents of `text`
print(text)


# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"
# Assign `missing_entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:
    # Use `.write()` to append `missing_entry` to the log file
    file.write(missing_entry + "\n")  # Adding newline to separate entries
# Use `open()` with the parameter "r" to open the security log file for reading purposes
with open(import_file, "r") as file:
    # Use `.read()` to read in the contents of the log file and store in a variable named `text`
    text = file.read()
# Display the contents of `text`
print(text)


# Assign `import_file` to the name of the text file that you want to create
import_file = "allowed_ips.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Display `import_file`
print(import_file)
# Display `ip_addresses`
print(ip_addresses)


# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(ip_addresses)



# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"
# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
# Create a `with` statement to write to the text file
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(ip_addresses)
# Create a `with` statement to read in the text file
with open(import_file, "r") as file:
    # Read the file and store the result in a variable named `text`
    text = file.read()
# Display the contents of `text`
print(text)



# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# First line of `with` statement to read the file
with open(import_file, "r") as file:
    # Read all lines and split into a list of IP addresses
    ip_addresses = file.read().split()
# Filter out IP addresses that are in `remove_list`
updated_ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
# Write the updated list back to the file
with open(import_file, "w") as file:
    file.write(" ".join(updated_ip_addresses))
# Display the updated contents of the file
print("Updated IP Addresses:")
print(" ".join(updated_ip_addresses))



