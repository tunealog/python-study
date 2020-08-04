# Basic of Python

# Title : Output Formats
# Date : 2020-06-29
# Creator : tunealog

#        500
print("{0: >10}".format(500))
#       +500
print("{0: >+10}".format(500))
#       -500
print("{0: >+10}".format(-500))
# +500______
print("{0:_<+10}".format(500))
# 500_______
print("{0:_<10}".format(500))

# 500,000,000,000
print("{0:,}".format(500000000000))
# +500,000,000,000
print("{0:+,}".format(500000000000))
# -500,000,000,000
print("{0:+,}".format(-500000000000))
# +500,000,000,000^^^^^^^^^^^^^^
print("{0:^<+30,}".format(500000000000))

# 1.666667
print("{0:f}".format(5/3))
# 1.67
print("{0:.2f}".format(5/3))
