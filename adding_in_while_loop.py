# 3/usr/bin/env python3

# This program was created by Larry Nkengbeza
# Created on December 2020
# THis program will add the up to the number that the user input in

def main():
    # This function uses loop to answer a questin.
    loop_counter = 0

    # Input
    user_input = int(input("Enter a number which will be added: "))
    print("")

    # Process and Output
    while loop_counter < user_input:
        print("The answer is {0}.".format(loop_counter))
        loop_counter = loop_counter + 1
    print("add the numbers up")


if __name__ == "__main__":
    main()
