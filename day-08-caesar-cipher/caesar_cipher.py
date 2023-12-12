from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    shift = shift % 26

    if direction == "decode":
        shift *= -1

    transformed = ""
    for char in text:
        if char in alphabet:
            shifted_index = alphabet.index(char) + shift
            if shifted_index > 25:
                shifted_index -= 26
            transformed += alphabet[shifted_index]
        else:
            transformed += char

    print(f"The {direction}d text is {transformed}")

print(logo)

keep_going = True

while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    keep_going = input("Type 'yes' if you want to go again, otherwise type 'no'\n").lower() == "yes"
