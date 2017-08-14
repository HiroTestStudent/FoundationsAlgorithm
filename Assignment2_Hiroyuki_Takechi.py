
#converting sttring "1024" to int 1024:

def Main(input_string):
    str = input_string
    list = [int(i) for i in str]
    string_number = 0
    n=1

    for a, b in enumerate(list):
        digit = b*10**(len(list)-n)
        string_number = string_number + digit
        n += 1
        print(a, b, string_number)
    print("String 1024 data type is converted to", type(string_number))

if __name__ == "__main__":
    Main("1024")
