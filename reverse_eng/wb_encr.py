def isSecret(guessString) -> bool:
    secretBytes = [0x4a, 0x69, 0x70, 0x7a, 0x60, 0x39, 0x54, 0x7a, 0x5a, 0x71, 0x70, 0x7a, 0x72, 0x7c, 0x77]
    userBytes = []
    if(len(guessString) != len(secretBytes)):
        return(0)
    else:
        for i in range(0, len(guessString)):
            magic = (int(guessString[i].encode("utf-8").hex(), 16) ^ 25)
            userBytes.append(magic)
            if(userBytes[i]==(int(secretBytes[i]))):
                if((i == len(guessString)-1)):
                    return(1)
            else:
                return(0)

def main() -> None:
    userGuess = input("Guess the secret: ")
    if(isSecret(userGuess)):
        print(f"Great job! The secret is: {userGuess}\n")
    else:
        print(f"Sorry, {userGuess} is not the secret!\n")

main()
