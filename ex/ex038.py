# Basic of Python

# Title : A variety of Functions
# Date : 2020-07-05
# Creator : tunealog

import datetime
import time
import os
import glob

# glob
# import glob
print(glob.glob("*.py"))


# os
# import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("Exist sample_dir")
    os.rmdir(folder)
    print(folder, "The folder is Deleted")
else:
    os.makedirs(folder)
    print(folder, "The folder is created")

print(os.listdir())

# time
# import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime
# import datetime
print("Today is ", datetime.date.today())

# --timedelta
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("I go to school on", today + td)
