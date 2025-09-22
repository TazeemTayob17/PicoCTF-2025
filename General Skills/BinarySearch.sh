#Below is the program given to us by the Binary Search picoCTF challenge.
#Connect to the server using cmd command and password provided in description
#We need to guess the number that the code generates randomly within 10 attempts
#We use binary search:
#Attempt 1: 500 (program says higher)
#Attempt 2: 750 (program says higher)
#Attempt 3: 875 (program says higher)
#Attempt 4: 938 (program says higher)
#Attempt 5: 969 (program says higher)
#Attempt 6: 985 (program says lower)
#Attempt 7: 977 (program says CORRECT)
#Hence we are given our flag: picoCTF{g00d_gu355_6dcfb67c}

            #!/bin/bash

            # Generate a random number between 1 and 1000
            target=$(( (RANDOM % 1000) + 1 ))

            echo "Welcome to the Binary Search Game!"
            echo "I'm thinking of a number between 1 and 1000."

            # Trap signals to prevent exiting
            trap 'echo "Exiting is not allowed."' INT
            trap '' SIGQUIT
            trap '' SIGTSTP

            # Limit the player to 10 guesses
            MAX_GUESSES=10
            guess_count=0

            while (( guess_count < MAX_GUESSES )); do
                read -p "Enter your guess: " guess

                if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
                    echo "Please enter a valid number."
                    continue
                fi

                (( guess_count++ ))

                if (( guess < target )); then
                    echo "Higher! Try again."
                elif (( guess > target )); then
                    echo "Lower! Try again."
                else
                    echo "Congratulations! You guessed the correct number: $target"

                    # Retrieve the flag from the metadata file
                    flag=$(cat /challenge/metadata.json | jq -r '.flag')
                    echo "Here's your flag: $flag"
                    exit 0  # Exit with success code
                fi
            done

            # Player has exceeded maximum guesses
            echo "Sorry, you've exceeded the maximum number of guesses."
            exit 1  # Exit with error code to close the connection

            