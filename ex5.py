# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.;

complete_name = str(input("Type your complete name: ")).split(' ')
complete_name.reverse()

end_name = ""

for i in complete_name:
	end_name += i + ' '

print(end_name.strip())

