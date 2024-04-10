# Check if all values in a Dictionary are equal in Python

a_dict = {
    'bobby': 5,
    'hadz': 5,
    'com': 5
}

# ✅ Check if all values in dict are equal to a specific value

all_equal_to_5 = all(value == 5 for value in a_dict.values())
print(all_equal_to_5)  # 👉️ True

# -------------------------------------------------

# ✅ Check if all values in dict are equal

first_value = list(a_dict.values())[0]
print(first_value)  # 👉️ 5

all_equal = all(value == first_value for value in a_dict.values())
print(all_equal)  # 👉️ True