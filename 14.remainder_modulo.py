# 1. Movie Theater Seating

# You're managing a small movie theater with 50 seats, and a 
# group of 7 peaple wants to sit togather in the same row. 
# How many complete rows can you fill, and how many seats will be 
# left over in the partially filled row?

total_seats = 50
people_to_seat = 7

rows_filled = total_seats // people_to_seat
remaining_seats = total_seats % people_to_seat

print("Total rows that can be filled: ", rows_filled)
print("Remaining Seats: ", remaining_seats)

# 2. Decode the Secret Message
# You've just intercepted an encoded message . 
# The message is a string of numbers, but you know their 
# encryption method: each letter of the alphabet is represented by its 
# position (hint1: A=0, B=1, C=2...Z=27; hint2: use chr()), and these numbers are then 
# concatenated into one long string. You need to decode the last 
# letter of this secret message. 

# 1. Extract the last digit of the encoded message.
# 2. Use this to determine the correstponding letter. 
# 3. Report back with the decoded letter.

encoded_message = 1233248916372176418

last_letter = encoded_message % 26

decoded_letter = chr(last_letter + 65)

print(f"The decoded message letter is {decoded_letter}")