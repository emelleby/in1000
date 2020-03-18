def first_and_last(message):
  if message == "" or message[0] == message[-1]:
    return True
  return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

def groups_per_user(group_dictionary):
  user_groups = {}
	# Go through group_dictionary
  # Now go through the users in the group
  for group, users in group_dictionary.items():
    for user in users:
      if user not in user_groups.keys():
        user_groups[user] = [group]
        print(user_groups.keys())
      else:
        user_groups[user].append(group)
    """ for user in users:
      if user in user_groups.keys():
        user_groups[user].append(group)
      else:
        user_groups[user] = [group] """
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
  return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))