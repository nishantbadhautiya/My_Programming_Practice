import os
if (not os.path.exists("data")):
    os.mkdir("data")
else:
    for i in range(0, 100):
        os.mkdir(f"data/day{i+1}")