###.2

find = 'nemo'

while True:

    word = input()

    if word == "EOI":

        break

    else:

        print("Found" if find in word.lower() else "Missing")









































###.1

# find = 'nemo'
#
# while True:
#
#    word = input().lower()
#
#    if word != "eoi":
#
#        if word.count(find):
#
#            print("Found")
#
#        else:
#
#            print("Missing")
#
#    else:
#
#        break
