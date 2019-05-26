# 26.05.2019
# Working with BitwiseOperators and different kind of String Outputs.

print(f"Working with Bitwise Operators and different kind of String Outputs.")
var1 = 13       # 13    in Binary: 1101
var2 = 5        # 5     in Binary: 0101

# AND Operator with format String
#   1101    13
#   0101    5
#   ----    AND: 1,0 = 0; 1,1 = 1; 0,0 = 0
#   0101    ->  5
print("AND & Operator {}".format(var1 & var2))


# OR Operator with f-String
#   1101    13
#   0101    5
#   ----    OR: 1,0 = 1; 1,1 = 1; 0,0 = 0
#   1101    ->  13
print(f"OR | operator {var1 | var2}")


# XOR Operator with String-formatting
#   1101    13
#   0101    5
#   ----    XOR: 1,0 = 1; 1,1 = 0; 0,0 = 0
#   1000    ->  8
print("XOR ^ operator %d" %(var1 ^ var2))


# Left Shift Operator with String .format
#   1101    13
#   ----    Left Shift: var << 1
#   11010    ->  26
print("Left Shift << operator {}".format(var1 << 1))


# Right Shift Operator with f-String
#   1101    13
#   ----    Right Shift: var >> 1
#   0110    ->  6
print(f"Right Shift >> operator {var1 >> 1}")