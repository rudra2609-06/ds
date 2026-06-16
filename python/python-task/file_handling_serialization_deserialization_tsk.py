import json
import string


'''
### `Q-1:` Write a function `get_final_line(filename)`, which takes filename as input and return final line of the file.

Note: You can choose any file of your choice.
'''


# def get_final_line(fileName):
# 	with open(f'{fileName}.txt','r') as f:
# 		content = f.readlines()[-1]

# 	print(content)


# get_final_line('sample')


'''
###`Q-2:` Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation -- dictionary.
'''

# vowels_count = {}
# vowels = ['a','e','i','o','u']

# with open('sample.txt','r') as f:
# 	while True:
# 		line = f.readline()
# 		if line == '':
# 			break
# 		print(line)
# 		for char in line.lower():
# 			if char in vowels:
# 				if char in vowels_count:
# 					vowels_count[char] += 1
# 				else:
# 					vowels_count[char] = 1	
					

# print(vowels_count)


'''
###`Q-3:` Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python to read through the file you've created. For each line, multiply each first number by the second and include it in the file in third column. In last add a line Total, by summing the value of third column
'''


# total = 0
# rows = []

# with open(r'D:\ds\python\taskfile.txt', 'r') as f:
#     for line in f:
#         line = line.strip()

#         num1, num2 = map(int, line.split('\t'))

#         product = num1 * num2
#         total += product

#         rows.append(f"{num1}\t{num2}\t{product}\n")

# with open(r'D:\ds\python\taskfile.txt', 'w') as a:
#     for row in rows:
#         a.write(row)

#     a.write(f"Total\t{total}\n")

# total = 0
# rows = []
# with open(r'D:\ds\python\taskfile.txt','r') as f:
# 	for each_line in f:
# 		each_line = each_line.strip()
# 		num1,num2 = map(int,each_line.split("\t"))
# 		product = num1 * num2
# 		rows.append(f'{num1}\t\t{num2}\t\t{product}')
# 		total += product
		
# 	rows.append(f'Total\t\t\t{total}')


# with open(r'D:\ds\python\taskfile.txt','w') as a:
# 	for row in rows:
# 		a.write(f'{row}\n')


'''
###`Q-4:` Create line wise reverse of a file
Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).
For example, if a file looks like
 ```
abc def
ghi jkl
```
then the output file will be
```
fed cba
lkj ihg
```
**Notice**: The newline remains at the end of the string, while the rest of the characters are all reversed.
'''

# def reverse_linewise(inputFileName,outputFileName):
# 	rows = []
# 	with open(f'{inputFileName}.txt','r') as f:
# 		while True:
# 			line = f.readline()[::-1]
# 			if line == '':
# 				break
# 			rows.append(f'{line}\n')
	
# 	with open(f'{outputFileName}.txt','w') as f1:
# 		for row in rows:
# 			f1.write(f'{row}')
		
		


# reverse_linewise('sample1','sample2')


'''
###`Q-5:` Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.

* List of word will be given

Given String

```
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']
```
'''

strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""


# words_count = {}

# for word in strings.lower().split():
# 	word = word.strip(string.punctuation)
# 	if word in words_count:
# 		words_count[word] += 1
# 	else:
# 		words_count[word] = 1


# with open('serialize.json','w') as f:
# 	json.dump(words_count,f)

# word_list = ['alice', 'wonder', 'natural']

# with open('serialize.json','r') as f1:
# 	count = json.load(f1)
# 	for word in word_list:
# 		if word in count:
# 			print(count[word])
# 		else:
# 			print("N/A")











	

		

			


			
