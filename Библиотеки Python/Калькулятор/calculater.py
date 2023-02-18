from tkinter import *


def no_numbers(text):
    while text[0] in operandes:
        lbl['text'] = text[1:]
        text = text[1:]
    while text[-1] in operandes:
        lbl['text'] = text[:-1]
        text = text[:-1]


def press_key(event):
    ch = event.char.upper()
    if lbl['text'] == '0':
        lbl['text'] = ''
    if ch.isdigit() or ch in operandes or ch in ('(', ')'):
        lbl['text'] += ch


def double_operands(text):
    for i in range(len(text) - 1):
        if text[i] in operandes and text[i + 1] in operandes or text[i + 1] == '0':
            lbl['text'] = text.replace(text[i + 1], '', 1)


def set_value(formula):
    print(f'set_value: {formula}')
    if formula != '':
        double_operands(lbl['text'])
        no_numbers(lbl['text'])
        lbl['text'] = str(eval(formula))
    elif formula == '':
        lbl['text'] = '0'

    if lbl['text'][0] == '0' and len(lbl['text']) > 1:
        lbl['text'] = lbl['text'].strip('0')

    if 'Error' in lbl['text']:
        lbl['text'] = lbl['text'].replace('Error', '0')
    else:
        try:
            print(lbl['text'])
            if lbl['text'][-1] == '0' and lbl['text'][-2] == '/':
                lbl['text'] = 'Error'
            else:
                print(lbl['text'])
                lbl['text'] = str(eval(formula))
        except (ZeroDivisionError, IndexError):
            pass


def logicalc(operation):
    print(f'logicalc: {operation}')
    if operation == 'C':
        set_value('')

    elif operation == 'D':
        text = lbl['text']
        print(len(text))
        if len(text) > 1:
            if text[-2:] == '.0' or (text[-1].isdigit() and text[-2] in operandes):
                set_value(lbl['text'][:-2])
            else:
                set_value(lbl['text'][:-1])
        else:
            set_value('')

    elif operation == 'X^2':
        set_value(str((eval(lbl['text'])) ** 2))

    elif operation == '=':
        set_value(lbl['text'])

    else:
        if lbl['text'] == '0':
            lbl['text'] = ''
        lbl['text'] = lbl['text'] + operation
        print(lbl['text'])


root = Tk()
root['bg'] = 'black'
root.geometry('485x550+200+100')
root.title('Калькулятор')
root.resizable(False, False)

btns = [['C', 'D', '*', '='],
        ['1', '2', '3', '/'],
        ['4', '5', '6', '+'],
        ['7', '8', '9', '-'],
        ['(', '0', ')', 'X^2']]

operandes = ('-', '*', '/', '+')

x = 10
y = 140

for i in range(len(btns)):
    for j in range(len(btns[i])):
        if i == 0 or j == 3:
            back = 'gray'
        else:
            back = 'white'

        Button(root, text=btns[i][j], bg=back, fg='black', activebackground='black', activeforeground='white',
               font=('Consolas', 15),
               command=lambda x=btns[i][j]: logicalc(x)) \
            .place(x=x, y=y, width=115, height=78)
        x += 117
        if x > 400:
            x = 10
            y += 81


cnv = Canvas(root, width=460, height=115, bg='white')
cnv.place(x=10, y=10)

lbl = Label(root, text='0', font=('Consolas', 21, 'bold'), foreground='black', bg='white')
lbl.place(x=11, y=50)

root.bind('<Key>', press_key)  # Регистрируем нажатия клавиш
root.mainloop()
