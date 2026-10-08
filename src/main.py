from datetime import date
from utils import add, subtract

print("===== Simple Calculator =====")

print("My name is Ahmad Zorjis")
print("Today's date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))

try:
    print("Division:", divide(10, 0))
except ValueError as error:
    print("Error:", error)