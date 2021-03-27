print(r"""
$$\      $$\                           $$\        $$$$$$\                               $$\                        
$$ | $\  $$ |                          $$ |      $$  __$$\                              $$ |                       
$$ $$ $$\$$ |$$  __$$\ $$  __$$\ $$  __$$ |      $$ |     $$  __$$\ $$ |  $$ |$$  __$$\_$$  _| $$  __$$\ $$  __$$\ 
$$$$  _$$$$ |$$ /  $$ |$$ |  \__|$$ /  $$ |      $$ |     $$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |   $$$$$$$$ |$$ |  \__|
$$$  / \$$$ |$$ |  $$ |$$ |      $$ |  $$ |      $$ |  $$\$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$\$$   ____|$$ |      
$$  /   \$$ |\$$$$$$  |$$ |      \$$$$$$$ |      \$$$$$$  \$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$  \$$$$$$$\ $$ |      
\__/     \__| \______/ \__|       \_______|       \______/ \______/  \______/ \__|  \__| \____/ \_______|\__|      
                                                                                                                   
""")
Lines = int(input("Enter the number of paragraphs you have (numeric): "))
lines = ''
i = 0

while i in range(Lines):
    Text = str(input("Input text in your para number {}: ".format(i+1)))
    lines += Text+" \n"
    i += 1

Split_lines = lines.split("\n")
Split_words = lines.split(" ")


print(lines)
print("The text is {} words and spans {} lines".format(
    len(Split_words)-1, len(Split_lines)-1))
