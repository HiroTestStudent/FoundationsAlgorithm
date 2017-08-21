#Assignment 6: String Comparison

#Approach 1:

def compare(one, two, caseInsensitive):
    s1 = list(one.lower())
    s2 = list(two.lower())
    bool = caseInsensitive.lower()
    if len(s1) != len(s2):
        return False
    else:
      for i in range(len(s1)):
         if (s1[i] == s2[i]) and bool == 'true':
             return True
         else:
             return False

print('compare("hello", "hello", "false")','->',compare("hello", "hello", "false"))
print('compare("hello", "hello", "true")','->',compare("hello", "hello", "true"))
print('compare("hello", "HELLO", "false")','->',compare("hello", "HELLO", "false"))
print('compare("hello", "HELLO", "true")','->',compare("hello", "HELLO", "true"))

#Approach 2:

def compare(s1, s2, bool):
    s1 = s1.lower()
    s2 = s2.lower()
    bool = bool.lower()
    if len(s1) != len(s2):
        return False
    else:
      for c1, c2 in zip(s1, s2):
         if (c1 == c2) and bool == 'true':
             return True
         else:
             return False

print('compare("hello", "hello", "false")','->',compare("hello", "hello", "false"))
print('compare("hello", "hello", "true")','->',compare("hello", "hello", "true"))
print('compare("hello", "HELLO", "false")','->',compare("hello", "HELLO", "false"))
print('compare("hello", "HELLO", "true")','->',compare("hello", "HELLO", "true"))

#Approach 3:

def compare(a, b, c):
    a = a.lower()
    b = b.lower()
    c = c.lower()
    if len(a) == len(b):
        for i in a:
            for t in b:
                if (i is t) and c == 'true':
                    return True
                else:
                    return False
    else:
        return False

print('compare("hello", "hello", "false")','->',compare("hello", "hello", "false"))
print('compare("hello", "hello", "true")','->',compare("hello", "hello", "true"))
print('compare("hello", "HELLO", "false")','->',compare("hello", "HELLO", "false"))
print('compare("hello", "HELLO", "true")','->',compare("hello", "HELLO", "true"))
