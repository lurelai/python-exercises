'''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]

def change():
	color_list[0], color_list[-1] = color_list[-1], color_list[0]

change()

print(color_list)

