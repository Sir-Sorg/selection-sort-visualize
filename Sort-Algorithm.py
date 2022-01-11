import tkinter as tk
import re


def changeListtoString(alist):
    # ====== function for convert list for show =======
    string = ''
    for this in alist:
        string = string + str(this) + ', '
    return string[:-2]  # for removing last ','


def selectionSort(atuple):
    # ===== Quantify len,min,index,position of min,start position ====
    alist = list(atuple)
    lenofList = len(atuple)
    mini = alist[0]
    startIndex = index = miniPosition = 0
    # ================== selection sort ===============
    for _ in range(lenofList-1):
        mini, miniPosition = alist[startIndex], startIndex
        while index < lenofList:
            thisElement = alist[index]
            if mini > thisElement:
                mini = thisElement
                miniPosition = index
            index += 1
        alist[startIndex], alist[miniPosition] = alist[miniPosition], alist[startIndex]
        startIndex += 1
        index = startIndex
        yield alist


def entryToList():
    # ========== covert user input to list ============
    value = userEntery.get()
    value = re.sub(r'\s+', ' ', value)
    algorithmItems = value.strip().split(' ')
    try:
        algorithmItems = tuple(map(lambda x: int(x), algorithmItems))
    except:
        print('you must Enter just number Not chareter! (Error-1)')
    # ================ sort and print =================
    listBox.insert(1, 'beginnings : {}'.format(
        changeListtoString(algorithmItems)))
    rouncCount = 1
    for this_round in selectionSort(algorithmItems):
        listBox.insert(tk.END, 'Round {} - {}'.format(rouncCount,
                       changeListtoString(this_round)))
        rouncCount += 1


# =================== create widow ================
window = tk.Tk()
window.title('Sort Algorithm')
window.geometry('800x500')
window.resizable(0, 0)
# same as window.resizable(width=False, height=False) ! Big brain Do
# ============== create lable & input =============
tk.Label(window, text='Please Enter numbers and separate those with \' SPACE \' :',
         font=("Arial")).pack()
userEntery = tk.Entry(window, width=70)
userEntery.pack()
# =============== create submit btn ===============
baseBtn = tk.Button(window, text='Sort', bg="LIGHTBLUE", command=entryToList)
baseBtn.pack()
# =============== create Text widget ===============
listBox = tk.Listbox(window, width=90, bg='black', fg='white')
listBox.pack()


window.mainloop()
