from pathlib import Path


def decode(coding_qual: str | Path):
    # Read the content of the file
    with open(coding_qual, 'r') as file:
        lines = file.readlines()

    # Initialize a list to store decoded words
    decoded_words = []

    # Initialize a counter to keep track of the current line
    line_counter = 1

    # Iterate through each line in the file
    for line in lines:
        # Split the line into number and word
        number, word = line.split()

        # Convert number to integer
        number = int(number)

        # Check if the current line number matches the number in the pyramid
        if number == line_counter:
            # Add the word to the decoded words list
            decoded_words.append(word)
            # Increment the line counter
            line_counter += 1

    # Join the decoded words into a string
    decoded_message = ' '.join(decoded_words)

    return decoded_message


if __name__ == "__main__":
    # Test the function
    encoded_message_path = Path(__file__).parent / "coding_qual_input.txt"
    decoded_message = decode(encoded_message_path)
    print(decoded_message)