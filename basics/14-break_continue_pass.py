# loop control statement = cahnge a loops execution from itse normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = deos nothing, acts as a placeholder


# stop asking name when a user inputs something (break)
while True:
    name = input("Enter your name: ")
    if name != "":
        break


# show phone number in oneline (continue)
phone_num = "123-456-7890"

for i in phone_num:
    if i == "=":
        continue
    print(i, end="")
print()


# show even numbers in oneline (pass)
for i in range(1, 21):
    if i % 2 != 0:
        pass
    else:
        print(i, end=" ")