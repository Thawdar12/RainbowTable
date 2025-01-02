import hashlib

# Step 1
passwords = []
with open("Passwords.txt", "r") as file:
    for line in file:
        passwords.append(line.strip())
print(f"Number of words read in: {len(passwords)}")

# Step 2
rainbow_table = {}
for word in passwords:
    current_word = word
    for _ in range(5):
        hash_value = hashlib.md5(current_word.encode()).hexdigest()
        current_word = passwords[int(hash_value, 16) % len(passwords)]
    rainbow_table[word] = hashlib.md5(current_word.encode()).hexdigest()

# Step 3
sorted_rainbow_table = sorted(rainbow_table.items(), key=lambda x: x[1])

# Step 4
with open("Rainbow.txt", "w") as file:
    for item in sorted_rainbow_table:
        file.write(f"{item[0]} {item[1]}\n")
print(f"Number of lines in the rainbow table: {len(sorted_rainbow_table)}")

# Second Step
def reduce_hash(hash_value, index, password_count):
    return passwords[(int(hash_value, 16) + index) % password_count]

def find_preimage(target_hash, rainbow_table):
    if target_hash in rainbow_table.values():
        for word, hashed_word in rainbow_table.items():
            if hashed_word == target_hash:
                return word

    for i in range(10000):  
        current_hash = target_hash
        for _ in range(5):
            current_hash = hashlib.md5(reduce_hash(current_hash, i, len(passwords)).encode()).hexdigest()
            if current_hash in rainbow_table.values():
                for word, hashed_word in rainbow_table.items():
                    if hashed_word == current_hash:
                        return word

    return None

# Taking input hash value from the use
# checking input length
while True: 
    hash_value = input("Enter a hash value: ")
    if len(hash_value) == 64:
        break
    print("The input length must be 64!!")
 
# Finding the pre-image
result = find_preimage(hash_value, rainbow_table)
if result:
    print(f"Pre-image for the hash value {hash_value}: {result}")
else:
    print("Pre-image not found.")