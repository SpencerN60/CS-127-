def inputValidInt():
    try:
        var1 = int(input("Input a Valid Integer: "))
        var2 = int(input("Input a Valid Integer: "))
        var3 = int(input("Input a Valid Integer: "))
        var4 = int(input("Input a Valid Integer: "))
        return var1, var2, var3, var4
    except Exception as e:
        print("ERROR",e)
#starting with A
def calcAAA(a,b,c,d):
    final = a + b + c + d
    return final
def calcAAS(a,b,c,d):
    final = a + b + c - d
    return final
def calcAAM(a,b,c,d):
    final = a + b + c * d
    return final
def calcASS(a,b,c,d):
    final = a + b - c - d
    return final
def calcASA(a,b,c,d):
    final = a + b - c + d
    return final
def calcASM(a,b,c,d):
    final = a + b - c * d
    return final
def calcAMM(a,b,c,d):
    final = a + b * c * d
    return final
def calcAMA(a,b,c,d):
    final = a + b * c + d
    return final
def calcAMS(a,b,c,d):
    final = a + b * c - d
    return final
#starting with S
def calcSSS(a,b,c,d):
    final = a - b - c - d
    return final
def calcSSA(a,b,c,d):
    final = a - b - c + d
def calcSSM(a,b,c,d):
    final = a - b - c * d
def calcSAS(a,b,c,d):
    final = a - b + c - d
    return final
def calcSAM(a,b,c,d):
    final = a - b + c * d
    return final
def calcSAA(a,b,c,d):
    final = a - b + c + d
    return final
def calcSMM(a,b,c,d):
    final = a - b * c * d
    return final
def calcSMS(a,b,c,d):
    final = a - b * c - d
    return final
def calcSMA(a,b,c,d):
    final = a - b * c + d
    return final
#starting with M
def calcMMM(a,b,c,d):
    final = a * b * c * d
    return final
def calcMMA(a,b,c,d):
    final = a * b * c + d
    return final
def calcMMS(a,b,c,d):
    final = a * b * c - d
    return final
def calcMAM(a,b,c,d):
    final = a * b + c * d
    return final
def calcMAS(a,b,c,d):
    final = a * b + c - d
    return final
def calcMAA(a,b,c,d):
    final = a * b + c + d
    return final
def calcMSS(a,b,c,d):
    final = a * b - c - c
    return final
def calcMSM(a,b,c,d):
    final = a * b - c * d
    return final
def calcMSA(a,b,c,d):
    final = a * b - c + d
    return final

def main():
    a,b,c,d = inputValidInt()
    finalDict = {}
    finalDict["AAA"] = calcAAA(a,b,c,d)
    finalDict["AAS"] = calcAAS(a,b,c,d)
    finalDict["AAM"] = calcAAM(a,b,c,d)
    finalDict["ASS"] = calcASS(a,b,c,d)
    finalDict["ASA"] = calcASA(a,b,c,d)
    finalDict["ASM"] = calcASM(a,b,c,d)
    finalDict["AMM"] = calcAMM(a,b,c,d)
    finalDict["AMA"] = calcAMA(a,b,c,d)
    finalDict["AMS"] = calcAMS(a,b,c,d)

    finalDict["SSS"] = calcSSS(a,b,c,d)
    finalDict["SSA"] = calcSSA(a,b,c,d)
    finalDict["SSM"] = calcSSM(a,b,c,d)
    finalDict["SAS"] = calcSAS(a,b,c,d)
    finalDict["SAM"] = calcSAM(a,b,c,d)
    finalDict["SAA"] = calcSAA(a,b,c,d)
    finalDict["SMM"] = calcSMM(a,b,c,d)
    finalDict["SMS"] = calcSMS(a,b,c,d)
    finalDict["SMA"] = calcSMA(a,b,c,d)

    finalDict["MMM"] = calcMMM(a,b,c,d)
    finalDict["MMA"] = calcMMA(a,b,c,d)
    finalDict["MMS"] = calcMMS(a,b,c,d)
    finalDict["MAM"] = calcMAM(a,b,c,d)
    finalDict["MAS"] = calcMAS(a,b,c,d)
    finalDict["MAA"] = calcMAA(a,b,c,d)
    finalDict["MSS"] = calcMSS(a,b,c,d)
    finalDict["MSA"] = calcMSA(a,b,c,d)
    finalDict["MSM"] = calcMSM(a,b,c,d)

    for keys in finalDict:
        print(keys, ": ", finalDict[keys])
    

main()
