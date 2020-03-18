"""#def cube(x,y):
for n in range(1,11):
    print(n, (n ** 3))

#cube(1,11)
"""
def get_members(member):
    return 0

def is_group():
    return 0

x = 2

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)
      count -=1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18