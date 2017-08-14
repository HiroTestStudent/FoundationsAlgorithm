def RPN(list):

    operator = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: float(x) / y),
        '^': (lambda x, y: x**y)
    } #lambda function is same as def func()...return...
    stack = []
    print("Reverse polish expression to compute: {}".format(list))
    for z  in list:
        if z not in operator.keys(): #operator.key() = dict_keys(['+', '-', '*', '/', '^'])
            stack.append(int(z))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.append(operator[z](x, y))#math operations based on lambda function above
            print("pop & operation : {} {} {} = ".format(x,z,y), operator[z](x, y))
    print('Answer = ', stack[0])
    #return stack[0]


RPN([1, 1, 2, 4, 5, '*', '+','/','^']) #1.0

#Reference URL: http://qiita.com/ogrew/items/8ae360ff648f99bf6c15
#Reference URL: https://stackoverflow.com/questions/40565027/reverse-polish-expression-monitoring-the-input
#Reference URL: https://codereview.stackexchange.com/questions/79795/reverse-polish-notation-calculator-in-python/79857