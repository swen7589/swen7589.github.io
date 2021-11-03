
# step 2 part 1
with open('dracula.html', 'r', encoding='utf-8') as f:
    text = f.read()

# step 2 part 2

text = text.replace('Count', 'Professor')
text = text.replace('count ', 'professor ')

text = text.replace('Dracula', 'Izbicki')
text = text.replace('dracula', 'izbicki')
text = text.replace('DRACULA', 'IZBICKI')
text = text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A', 'I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I')

text = text.replace('Bram Stoker', 'Swen Ihueze')
text = text.replace('Bram ', 'Swen ')
text = text.replace(' Stoker', ' Ihueze')

with open('izbicki.html', 'w', encoding='utf-8') as f:
    f.write(text)


'''
accumulator = []

for i in dracula.html:

    # for count turning into professor
    if i == 'Count':
        i = 'Professor'
        accumulator.append(i)
    elif i == 'count':
        i = 'professor'
        accumulator.append(i)
    
    # for dracula turning into izbicki
    elif i == 'Dracula':
        i = 'Izbicki'
        accumulator.append(i)
    elif i == 'dracula':
        i = 'izbicki'
        accumulator.append(i)
    elif i == 'DRACULA':
        i = 'IZBICKI'
        accumulator.append(i)
    
    # for the edge case
    elif i == 'D R A C U L A':
        i = 'I Z B I C K I'
        accumulator.append(i)

    # for my name
    elif i == 'Bram':
        i = 'Swen'
        accumulator.append(i)
    elif i == 'Stroker'
        i = 'Ihueze'
        accumulator.append(i)
    
    # any other word
    else:
        accumulator.append(i)

return accumulator.join('')
'''