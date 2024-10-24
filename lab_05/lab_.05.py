# Import palantir.py
import palantir as pal

# Name Check
if __name__ == "__main__":
    # Gandalf
    def get_the_time():
        return "A wizard is never late, nor is he early. He arrives precisely when he means to."
    message = get_the_time()
    print(message)

# Fellowship  
def check_party_size(number):
    if number < 9:
        print("You will need more companions on the long road ahead.")
    elif number > 9:
        print("Too many will draw the Eye of the Enemy!")
    else:
        print("Nine walkers to match the nine riders.")
user_input_size = int(input("How many companions join you on the road ahead?: "))

check_party_size(user_input_size)


pal.see_realm("Arnor")
pal.touch_stone(True)
pal.touch_stone(False)