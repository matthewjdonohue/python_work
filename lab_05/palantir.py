import random

def touch_stone(is_king_of_gondor=False):
    if is_king_of_gondor:
        print("The stone bends to your will as the rightful heir of Elendil.")
    else:
        print("A mighty voices bellows 'I see you!'")

def see_realm(realm):
    print(f"You attempt to cast your eye on the realm of {realm}...")
    if random.randint(0, 9) < 2:
        print("The realm opens before your eyes.")
    else:
        print(f"A darkness shrouds your vision, hiding {realm} from your gaze.")