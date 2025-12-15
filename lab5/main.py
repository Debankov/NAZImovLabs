M = [1,3,5,7,9] # массив исходных значений

data = {
    "ax":[],
    "bx":[],
}

def A(data): # предикат A(x): x > 5
    resultBool = [] # массив хранящий результаты функции
    for i in data:
        resultBool.append(True) if i > 5 else resultBool.append(False)
    return resultBool

def B(data): # предикат  B(x): x положительное число
    resultBool = []
    for i in data:
        resultBool.append(True) if i >= 0 else resultBool.append(False)
    return resultBool

def implication(A,B): # импликация по заданному условию: !A(x) -> B(x)
    resultBool = []
    for i in range(len(A)):
        if A[i] == True and B[i] == True:
            resultBool.append(True)
        elif (A[i] == False and B[i] == True) or (A[i] == False and B[i] == False):
            resultBool.append(False) 
    return resultBool

def getOnlyTrueFromImlication(A,B,arr):
    # словарь в котором хранятся значения X для полной истины предикатов
    SpaceOfTrueForImplication = {
        "ax": [],
        "bx": [],
    } 
    for i in range(len(A)): # по скольку длина массива A и B одинакова, выбираем любой массив
        if A[i] == True and B[i] == True:
            SpaceOfTrueForImplication["ax"].append(arr[i])
            SpaceOfTrueForImplication["bx"].append(arr[i])
    return SpaceOfTrueForImplication


a = A(M)
print(f"A: {a}")
b = B(M)
print(f"B: {b}")
print(f"!A(x) -> B(x) {implication(a,b)}")
print(getOnlyTrueFromImlication(a,b,M))