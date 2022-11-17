while True:
    try:
        print("(a^e + b^e-1...) / (x + c)")
        
        amount = int(input("What is the highest power in the polynomial: "))
        
        values = []
        for i in range(amount, -1, -1):
            if not i: values.append(float(input("Enter the constant value: ")))
            elif i == 1: values.append(float(input("Enter the linear value: ")))
            else: values.append(float(input("Enter the x^" + str(i) + " value: ")))
        e = 0 - float(input("Enter the c value: "))
        
        h = values[0]
        outputs = []
        
        for i in range(amount):
            outputs.append(h)
            h = values[i + 1] + (e * h)
        outputs.append(h)
        
        output = ""
        
        for i in range(amount - 2):
            if output:
                if outputs[i]: output += "+ " + str(outputs[i] if outputs[i] != 1 else "") + "x^" + str(amount - 1 - i) + " "
            else:
                if outputs[i]: output += str(outputs[i] if outputs[i] != 1 else "") + "x^" + str(amount - 1 - i) + " "
        
        if outputs[amount - 2]:
            if output: output += "+ " + str(outputs[amount - 2] if outputs[amount - 2] != 1 else "") + "x "
            else: output += str(outputs[amount - 2]) + "x "
        
        if outputs[amount - 1]:
            if output: output += "+ " + str(outputs[amount - 1]) + " "
            else: output += str(outputs[amount - 1]) + " "
        
        if outputs[amount]: output += "R" + str(outputs[amount])
        
        print(output)
    except: input("Bad input, press enter to continue!")
    print("")
