<font size="5"> How the function works:

The `reduce_hash` function takes a hash value, an index, and the number of passwords as inputs. It converts the hash value to an integer, adds the index, and calculates the remainder when divided by the password count, which is then used to select a password from the list.

The `find_preimage` function attempts to find the original password for a given target hash. If the hash exists in the rainbow table, it returns the corresponding password. Otherwise, it iteratively applies the `reduce_hash` function to generate new hashes and checks if any match a hash in the table. If found, it returns the original password; if not, it returns `None`.

<font size="5"> What I learnt 
