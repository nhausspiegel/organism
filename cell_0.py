n = 0
limit = 100

import subprocess

if n < limit:
    mode = open("mode.txt", "r").read()
    if mode == "up":
        next_cell_lines = [f"n = {n+1}\n"] + open(f"cell_{n}.py", "r").readlines()[1:]
        open(f"cell_{n+1}.py", "w").writelines(next_cell_lines)
    if mode == "down":
        total = float(open("total.txt", "r").read())
        addend = 4 * (((-1) ** n) / (2 * n + 1))
        open("total.txt", "w").write(str(total + addend))
    subprocess.run(["python3", f"cell_{n+1}.py"])
