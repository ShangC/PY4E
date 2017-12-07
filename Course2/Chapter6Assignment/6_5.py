text = 'X-DSPAM-Confidence:    0.8475'
pos = text.find('0')
print(float(text[pos:]))

# use a function to extract numbers in the string. However, since '.' throws the traceback, '0' is discarded and only return decimal numbers.
# def function(string):
#     final = ''
#     for i in string:
#         try:
#             final += str(int(i))
#         except ValueError:
#             continue
#     return int(final)
# print(function('X-DSPAM-Confidence:    0.8475'))

# one line for extracting digits from string, but not good for floating numbers
# print(''.join(filter(str.isdigit, 'X-DSPAM-Confidence:    0.8475')))
