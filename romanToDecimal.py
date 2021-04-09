def romanToDecimal(str):
    # code here
    romanDec = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000 }
    
    num = romanDec[str[0]]
    for i in range(1,len(str)):
        if romanDec[str[i]] > romanDec[str[i-1]]:
            num -= romanDec[str[i-1]]
            num += romanDec[str[i]] - romanDec[str[i-1]]
        else:
            num += romanDec[str[i]]
    return num