print("Welcome to Gorge Lake.")
direction = input("There are two paths down to the lake, which will you choose? Right or Left? ")
if direction == "Left" or direction == "left":
    print("The path twists and turns, but eventually you arrive safely at the edge of the lake.")
else:
    print("You find a rope bridge spanning a large ravine. As you cross the bridge it breaks, and you fall to your death, GAME OVER.")
    raise SystemExit
lake = input("At the edge of the lake you see an old rickety row boat. Do you take the boat or swim? ")
if lake == "swim" or lake == "Swim":
    print("You underestimated how cold the water was and your muscles begin to seize and you drown. GAME OVER")
    raise SystemExit
else:
    print("The old boat holds together, and you make it to the other side of the lake safely.")
cave = input("As you leave the lake behind you approach a cave with three entrances, Right, Left, Center. Which do you take? ")
if cave == "Right" or cave == "right":
    print("As you go further into the cave a giant spider drops down from the ceiling and kills you. GAME OVER")
    raise SystemExit
elif cave == "Center" or cave == "center":
    print("You enter the cave and see light in the distance.")
    print("As you get to the other side you find a huge pile of treasure. Congratulations! Your are now wealthy and you win the game!!!")
else:
    print("You enter the cave and wind through the dark until you slip and fall down a chasm to you death. GAME OVER")
