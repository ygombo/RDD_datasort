import glob
import os

result = ''
directory = "/Users/ygombo1016/Desktop/KonstruksiAI/road_damage_data/output/test"
for f in glob.glob(os.path.join(directory, "*.json")):
    with open(f, "r") as infile:
        result += infile.read()
        result += "\n"

with open("test_file.jsonl", "w") as outfile:
    outfile.write(result)