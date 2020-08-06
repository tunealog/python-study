# Basic of Python

# Title : Pickle
# Date : 2020-06-30
# Creator : tunealog

import pickle

# Pickle Write
profile_file = open("profile.pickle", "wb")
profile = {"name": "James", "age": 30, "hobby": ["soccer", "golf", "coding"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

# Pickle Load
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
