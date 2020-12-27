lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Kevin", "Karen", "Bill", "Oscar", "Felipe"]

friends.extend(lucky_numbers)  # Add list values to another list

print(friends)

friends.append("Mike")  # Add value to the list

print(friends)

friends.insert(0, "Kelly")  # Insert value at some position in the list

print(friends)

friends.reverse()  # Reverse the values of the list

print(friends)

friends.remove(friends[0])  # Remove a value in the list

print(friends)

friends.pop()  # Remove the last value of the list

print(friends)

friends.clear()  # Clear the list

print(friends)
