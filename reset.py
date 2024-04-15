import os

print("Resetting...")

# remove files
n = 1
filename = f"cell_1.py"
while os.path.exists(filename):
    os.remove(filename)
    n += 1
    filename = f"cell_{n}.py"

# reset default values
open("mode.txt", "w").write("up")
open("total.txt", "w").write("0")

print("Done.")
