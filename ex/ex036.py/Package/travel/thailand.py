# Basic of Python

# Title : Packages
# Date : 2020-07-05
# Creator : tunealog

class ThailandPackage:
    def detail(self):
        print("[Thailand Package] Bankok Travel $500")


if __name__ == "__main__":
    print("Run Thailand Module")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Run outside Thailand Mudule")
