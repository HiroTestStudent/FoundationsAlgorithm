# -------------------------------------------------#
# Desc: Assignment 1 Converting base 62 to base 10
# Question:  After watching the binary number video, did you notice the YouTube url?
#            https://www.youtube.com/watch?v=LpuPe81bc2w
#            Write the code to convert the base-62 number to base-10.
#            Submit your program (C#, Python, Javascript, ...) as well as the decimal number value for LpuPe81bc2w.
#            Hint: Use an array/string that contains all the numbers and digits: "0123456789AB...YZab...yz"
# Dev: Hiroyuki Takechi
# Date: 7/5/2017
# ChangeLog: (when,who,what)
# -------------------------------------------------#

base_62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #String
str = "LpuPe81bc2w"

def base62_conv(str, chars = base_62):
  num = 0
  for char in str:
    num = num * len(chars)
    #print(chars.index(char)) #checking purpose
    num = num + chars.index(char) #num + the decimal value of the character in str (in order)
    #print(num) #checking purpose
  return num

if __name__ == "__main__":
    print(base62_conv(str)) #decimal number value for LpuPe81bc2w = 39792227967530847876

#Source code reference URL: "http://php6.jp/python/2011/02/02/%E5%9F%BA%E6%95%B0%E5%A4%89%E6%8F%9B/"
#I double checked in Excel. Excel shows "39792227967530800000". Not sure of why Excel shows different values

