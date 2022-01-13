import tkinter as tk
import re


def creatLabel(howMany):
    # ================= creat Label ===================
    labelList = list()
    for _ in range(howMany):
        thisOne = tk.Label(master=tempFrm, bg="LIGHTBLUE", bd=10)
        thisOne.pack(side=tk.LEFT)
        labelList.append(thisOne)
    return labelList


def changeListtoString(alist):
    # ====== function for convert list for show =======
    string = ''
    for this in alist:
        string = string + str(this) + ', '
    return string[:-2]  # for removing last ','


def printRaw(numList, labelList):
    # ================ print raw list =================
    listBox.insert(1, 'beginnings : {}'.format(
        changeListtoString(numList)))
    # ======= creat Label and fill by user entry ======
    index = 0
    for thisLabel in labelList:
        thisLabel.config(text='{}'.format(numList[index]))
        index += 1


def set_color(labelList, index, color, start):
    colorDict = {'b': '#6699ff', 'r': '#ff6666',
                 'y': '#ffff99', 'd': 'LIGHTBLUE'}
    labelList[index].config(bg=colorDict[color])
    # read it cerfully
    if color != 'y' and start != index:
        labelList[index-1].config(bg=colorDict['d'])
    elif start == len(labelList)-2:
        labelList[-1].config(bg=colorDict['y'])
    else:
        labelList[-1].config(bg=colorDict['d'])


def assign(obj, value):
    obj.config(text=value)


def selectionSort(atuple, labelList):
    # ===== Quantify len,min,index,position of min,start position ====
    numList = list(atuple)
    countt = len(numList)
    # ================== selection sort ===============
    startI = 0
    delay = 500
    for _ in range(countt-1):
        minn = numList[startI]
        minPosition = i = startI
        for thisOne in numList[startI:]:
            window.after(delay, set_color, labelList, i, 'b', startI)
            if thisOne < minn:
                minn = thisOne
                minPosition = i
                window.after(delay, set_color, labelList, i, 'r', startI)
            i += 1
            delay += 500
        window.after(delay, assign, labelList[startI], numList[minPosition])
        window.after(delay, assign, labelList[minPosition], numList[startI])
        numList[startI], numList[minPosition] = numList[minPosition], numList[startI]
        window.after(delay, set_color, labelList, startI, 'y', startI)
        startI += 1
        yield numList


def clearr():
    listBox.delete(0, tk.END)
    userEntery.delete(0, tk.END)
    tempFrm.destroy()
    clrBtn.destroy()


def mainSort():
    # ========== covert user input to list ============
    value = userEntery.get()
    value = re.sub(r'\s+', ' ', value)
    algorithmItems = value.strip().split(' ')
    try:
        algorithmItems = tuple(map(lambda x: int(x), algorithmItems))
    except:
        print('you must Enter just number Not chareter! (Error-1)')
    # ===== create Label and send it for first show =====
    global tempFrm
    tempFrm = tk.Frame(master=lblFrm)
    tempFrm.pack()
    numsCount = len(algorithmItems)
    labelsList = creatLabel(numsCount)
    printRaw(algorithmItems, labelsList)
    # ============== creat Clear-Button ===============
    global clrBtn
    clrBtn = tk.Button(master=inpFrm, text='Clear',
                       bg="#ffff99", command=clearr, relief='solid', borderwidth=1, padx=16, pady=5)
    clrBtn.place(x=610, y=50)
    # ================ sort and print =================
    rouncCount = 1
    for this_round in selectionSort(algorithmItems, labelsList):
        listBox.insert(tk.END, 'Round {}: {}'.format(rouncCount,
                       changeListtoString(this_round)))
        rouncCount += 1


# =================== create widow ================
window = tk.Tk()
window.title('Sort Algorithm')
window.geometry('800x400')
window.resizable(0, 0)
# same as window.resizable(width=False, height=False) ! Big brain Do
# ==== create 3 Frame to organizing the layout ====
inpFrm = tk.Frame(master=window, height=100)
inpFrm.pack(fill=tk.X)
lblFrm = tk.Frame(pady=20)
terFrm = tk.Frame(pady=20)
# ============== create lable & input =============
tk.Label(master=inpFrm, text='Please Enter numbers and separate those with \' SPACE \' :',
         font=("Arial")).place(x=38, y=20)
userEntery = tk.Entry(master=inpFrm, width=69, relief='solid')
userEntery.place(x=38, y=55)
# =============== create sort Button ===============
baseBtn = tk.Button(master=inpFrm, text='Sort',
                    bg="LIGHTBLUE", command=mainSort, relief='solid', borderwidth=1, padx=20, pady=5)
baseBtn.place(x=688, y=50)
# =============== create List Box widget ===============
listBox = tk.Listbox(master=terFrm, width=90, bg='gray',
                     fg='white', relief='flat')
listBox.pack()
# ========= Pack label Frame for this position =========
lblFrm.pack()
terFrm.pack(side=tk.BOTTOM)

window.mainloop()
