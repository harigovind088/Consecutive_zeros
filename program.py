def consecutive_zeros(binary_string):
    # Check if the input is empty or contains invalid characters
    if not binary_string:
        return "Invalid"

    for char in binary_string:
        if char != '0' and char != '1':
            return "Invalid"


    max_zeros = 0  # Maximum number of consecutive zeros found so far
    current_zeros = 0  # Count of the current sequence of consecutive zeros


    for char in binary_string:
        if char == '0':
            current_zeros += 1
            if current_zeros > max_zeros:
                max_zeros = current_zeros
        else:
            current_zeros = 0

    return max_zeros



# Examples or Output:

print(consecutive_zeros("01001"))

print(consecutive_zeros("1001101000110"))  #Output is 3

print(consecutive_zeros("10000110"))  #Output is 4

print(consecutive_zeros("101001")) #Output is 2

print(consecutive_zeros("100a1")) #Output is Invalid

print(consecutive_zeros("")) #Output is Invalid

print(consecutive_zeros("  ")) #Output is Invalid

print(consecutive_zeros("@-101@")) #Output is Invalid


