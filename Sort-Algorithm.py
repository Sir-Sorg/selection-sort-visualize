import tkinter as tk
import re
from time import sleep


def creatLabel(howMany):
    # ================= creat Label ===================
    labelList = list()
    for _ in range(howMany):
        thisOne = tk.Label(master=lblFrm, bg="LIGHTBLUE", bd=10)
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


def selectionSort(atuple,labelList):
    # ===== Quantify len,min,index,position of min,start position ====
    alist = list(atuple)
    countt = len(atuple)
    minimum = alist[0]
    startIndex = index = minimumPosition = 0
    # ================== selection sort ===============
    for _ in range(countt-1):
        minimum, minimumPosition = alist[startIndex], startIndex
        while index < countt:
            thisElement = alist[index]
            if minimum > thisElement:
                # find the unicorn (target)
                minimum = thisElement
                minimumPosition = index
            index += 1
        alist[startIndex], alist[minimumPosition] = alist[minimumPosition], alist[startIndex]
        startIndex += 1
        index = startIndex
        yield alist


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
    numsCount = len(algorithmItems)
    labelsList = creatLabel(numsCount)
    printRaw(algorithmItems, labelsList)
    # ================ sort and print =================
    rouncCount = 1
    for this_round in selectionSort(algorithmItems,labelsList):
        listBox.insert(tk.END, 'Round {} - {}'.format(rouncCount,
                       changeListtoString(this_round)))
        rouncCount += 1 


# =================== create widow ================
window = tk.Tk()
window.title('Sort Algorithm')
window.geometry('800x500')
window.resizable(0, 0)
# same as window.resizable(width=False, height=False) ! Big brain Do
# ==== create 2 Frame to organizing the layout ====
inpFrm = tk.Frame(master=window, height=100)
inpFrm.pack(fill=tk.X)
lblFrm = tk.Frame(pady=20)
# ============== create lable & input =============
tk.Label(master=inpFrm, text='Please Enter numbers and separate those with \' SPACE \' :',
         font=("Arial")).place(x=20, y=20)
userEntery = tk.Entry(master=inpFrm, width=70, relief='solid')
userEntery.place(x=20, y=55)
# =============== create sort Button ===============
baseBtn = tk.Button(master=inpFrm, text='Sort',
                    bg="LIGHTBLUE", command=mainSort, relief='solid', borderwidth=1, padx=20, pady=5)
baseBtn.place(x=650, y=50)
# =============== create List Box widget ===============
listBox = tk.Listbox(window, width=90, bg='gray', fg='white', relief='flat')
listBox.pack()
# ========= Pack label Frame for this position =========
lblFrm.pack()

window.mainloop()
