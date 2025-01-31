# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]
# Assign `new_user` to the username of a new approved user
new_user = "gesparza"
# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"
# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append("gesparza")
approved_devices.append("3rcv4w6")
# Display the contents of `approved_users`
print(approved_users)
# Diplay the contents of `approved_devices`
print(approved_devices)


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `removed_user` to the username of the employee who has left the team
removed_user = "tshah"
# Assign `removed_device` to the device ID of the employee who has left the team
removed_device = "2ye3lzg"
# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively
approved_users.remove("tshah")
approved_devices.remove("2ye3lzg")
# Display `approved_users`
print(approved_users)
# Diplay `approved_devices`
print(approved_devices)


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `username` to a username
username = "sgilmore"
# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users:
    print("The user", username, "is approved to access the system.")
else:
    print("The user", username, "is not approved to access the system.")


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `username` to a username
username = "sgilmore"
# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)
# Display the value of `ind`
print(ind)


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `username` to a username
username = "sgilmore"
# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)
# Display the device ID at the index that matches the value of `ind` in `approved_devices`
print(approved_devices[ind])



# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `username` to a username
username = "sgilmore"
# Assign `device_id` to a device ID
device_id = "4n482ts"
# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)
# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device
if username in approved_users and device_id in approved_devices:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Assign `username` to a username
username = "sgilmore"
# Assign `device_id` to a device ID
device_id = "4n482ts"
# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)
# If statement
# If `username` belongs to `approved_users`, and if the element at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device
if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
# Elif statement
# Handles the case when `username` belongs to `approved_users` but element at `ind` in `approved_devices` does not match `device_id`,
# and displays two messages accordingly
elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")


# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id):
    # If `username` belongs to `approved_users`
    if username in approved_users:
        # Display approval message
        print("The user", username, "is approved to access the system.")
        # Assign `ind` to the index of `username` in `approved_users`
        ind = approved_users.index(username)
        # Check if `device_id` matches the assigned device
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")
    else:
        # Display rejection message
        print("The user", username, "is not approved to access the system.")
# Call the function with different username and device_id combinations
login("sgilmore", "4n482ts")  # Approved user with correct device
login("sgilmore", "hl0s5o1")  # Approved user with incorrect device
login("jdoe", "xyz123")       # Unapproved user



