How the function works:

The `reduce_hash` function takes a hash value, an index, and the number of passwords as inputs. It converts the hash value to an integer, adds the index, and calculates the remainder when divided by the password count, which is then used to select a password from the list.

The `find_preimage` function attempts to find the original password for a given target hash. If the hash exists in the rainbow table, it returns the corresponding password. Otherwise, it iteratively applies the `reduce_hash` function to generate new hashes and checks if any match a hash in the table. If found, it returns the original password; if not, it returns `None`.

What I learnt 
- Rainbow Tables: Storing precomputed hash values to efficiently find pre-images.
- Hashing: Uses Python’s hashlib to compute MD5 hashes.
- Reduction Function: Maps hash values to potential password candidates.
- File Handling: Demonstrates reading from and writing to files (Passwords.txt and Rainbow.txt).
- Sorting: Sorts a dictionary by values using lambda functions.
- Error Checking: Validates user input (e.g., correct hash length).
- Iterative Process: Implements hash-reduction cycles for generating and searching rainbow tables.
- Algorithm Design: Balances space and time complexity.
- Modular Design: Encourages reusable functions for better code organization.
- Hash Collisions: Highlights challenges like hash collisions.
