
# graph 1
import json
import matplotlib.pyplot as plt

space_peeps = json.loads(open('astros.json', 'r'))

left = [1, 2, 3]
 
# heights of bars
height = [7, 3]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'red'])
 
# naming the x-axis
plt.xlabel('Space Station')
# naming the y-axis
plt.ylabel('Number of People')
# plot title
plt.title('The People in Space Right Now')
 
# showing the plot
plt.show()



# start of graph 2

meteors = json.loads(open('astros-2.json', 'r'))
meteors_2 = json.loads(open('astros-3.json', 'r'))

'''
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(True)


LINE GRAPH 
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')
'''

'''
# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
 
# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()
'''