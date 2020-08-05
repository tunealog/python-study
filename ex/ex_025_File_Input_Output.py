# Basic of Python

# Title : File Input Output
# Date : 2020-06-29
# Creator : tunealog

# Write
score_file = open("score.txt", "w", encoding="utf8")
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close()

# Append
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("science : 80")
score_file.write("\ncomputer : 100")
score_file.close()

# Read
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# Read
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# Read
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# Read
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
