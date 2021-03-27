# filename
file_name = input("Enter file name:")
# open file
file1 = open(file_name, "r")

# dictionary named d
d = {} 
print("\n File Contents are:\n")

# For loop to read each line one by one from the given text file
# display file contents line by line, too
for line in file1:
    print(line, end='')
    # use strip() method for removing any leading spaces and newline character 
    line = line.strip() 
    # we use lower() method to convert this line into lowercase 
    line = line.lower() 
    # we use split() method to split the line into words (use space as separator)
    # all words are in words list now
    words = line.split(" ") 
  
    # we wll loop through every word in the line 
    for word in words: 
        #  we check if the word is already in dictionary 
        if word in d: 
            # if word already present, increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # else if word not present in dictionary then add it to dictionary and now count =1 
            d[word] = 1

print("\n\nNumber of occurrences of each word in file is:")  
print("\n ===============\n")  
# use the for loop to show evey entry of dictionary
# this will print number of occurrences of each word in
# the given text file

for key in list(d.keys()): 
    print(key, ":", d[key]) 

# close the file
file1.close()