# Basic of Python

# Title : With
# Date : 2020-06-30
# Creator : tunealog

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("Studing Python")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
