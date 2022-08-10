import re
OPENING = "<text"
FIRST = ">"
SECOND = "</text"
FIND_BETWEEN_2_CHARACTERS_TEXT = f"(?<={FIRST}).*(?={SECOND})"
FIRST_DIM_Y = 'y="'
SECOND_DIM_Y = '" fill'
Y_DIM = f"(?<={FIRST_DIM_Y}).*(?={SECOND_DIM_Y})" #'y="[(0-9\.)]*"'
FIRST_DIM_X = 'x="'
SECOND_DIM_X = '" y='
X_DIM = f"(?<={FIRST_DIM_X}).*(?={SECOND_DIM_X})" #'y="[(0-9\.)]*"'

FORMAT_LINE = '  <text x="{x_dimension}" y="{y_dimension}" fill="black" style="font: 10px Poppins; white-space: pre; letter-spacing: 0px">{text}</text>'
storage = []

to_convert_name = "FinalCV2.html"
to_convert_out = "FinalCV2_out.html"

with open(to_convert_name, 'r', encoding='latin_1') as file:
    for i,line in enumerate(file.readlines()):
        if 'text' in line:
            
            text = re.findall(FIND_BETWEEN_2_CHARACTERS_TEXT, line)
            x_dim = re.findall(X_DIM, line)
            y_dim = re.findall(Y_DIM, line)
            storage.append((float(x_dim[0]),float(y_dim[0]), text[0], i))




x,y,text,line = storage[0]
text_so_far = [text]
lines_to_ignore = []
created_lines = dict()
starting_x = x

for i in range(1, len(storage)):
    x_curr, y_curr, text_curr, line_curr = storage[i]
    if y_curr == y and x_curr - x <= 100:
        x = x_curr
        text_so_far.append(text_curr)
        lines_to_ignore.append(line_curr)
    else:
        string = ' '.join(text_so_far)
        created_lines[(starting_x,y)] = string
        text_so_far = [text_curr]
        x = x_curr
        y = y_curr
        starting_x = x_curr
else:
    string = ' '.join(text_so_far)
    created_lines[(starting_x,y)] = string

with open(to_convert_name, 'r', encoding='latin_1') as file, open(to_convert_out, 'w', encoding='latin_1') as file_out:
    for i,line in enumerate(file.readlines()):
        if 'text' in line:
            x_dim = re.findall(X_DIM, line)
            y_dim = re.findall(Y_DIM, line)
            x = float(x_dim[0])
            y = float(y_dim[0])
            if (x,y) in created_lines:
                line = re.sub(FIND_BETWEEN_2_CHARACTERS_TEXT, created_lines[x,y], line)
                line = line.replace("- ", "-")
                line = line.replace(" .", ".")
                file_out.write(line)
        else:
            file_out.write(line)

"""
for elem in storage:
    print(elem)

x_diff = []
for i in range (0, len(storage) - 1):
    x_1, y_1 = storage[i]
    x_2, y_2 = storage[i+1]
    if y_1 == y_2:
        x_diff.append(x_2 - x_1)
    else:
        pass
from statistics import mean
print(mean(x_diff))            
print(min(x_diff))
print(max(x_diff))
x_diff.sort()
print(x_diff)

y_current = storage[0][1]
x_current = storage[0][0]
text_so_far = []
created_lines = []

for elem in storage:
    
    x,y,text = elem
    if y == y_current:
        text_so_far.append(text)
    else:
        string = ' '.join(text_so_far)
        txt = FORMAT_LINE.format(x_dimension=x_current,y_dimension=y_current, text=string)
        txt.replace(' .', '.')
        created_lines.append(txt)
        text_so_far = []
        y_current = y
        x_current = x

with open("CV.html", 'r') as file, open('CV_new.html','w') as file_out:
    y_current = None
    counter = -1
    for line in file.readlines():
        if OPENING in line:
            y_dim = re.findall(Y_DIM, line)
            if float(y_dim[0]) != y_current:
                y_current = float(y_dim[0])
                counter += 1
                try:
                    file_out.write(created_lines[counter])
                except Exception as e:
                    print("Error")
        else:
            file_out.write(line)
"""