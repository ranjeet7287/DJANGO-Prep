# Some Theory

# Types of data used for I/O(Input/Output)
    # Text - '12345' as a sequence of unicode chars
    # Binary - 12345 as a sequence of bytes of its binary equivalent

# Hence there are 2 file types to deal with
    # Text files - All program files are text files
    # Binary Files - Images,music,video,exe files

# How File I/O is done in most programming languages
    # Open a file
    # Read/Write data
    # Close the file


# ⭐ case 1 - if the file is not present

f = open('sample.txt','w')
# w -> write
f.write('Waheguru ji')
f.close()

# f.write('Waheguru ji')
# ValueError: I/O operation on closed file.


#  ⭐ write multiline string
f = open('sample2.txt','w')

f.write('hello world')
f.write('\n Tho kisa ho aap log ?')
f.close()

# ⭐ case 2 -> if the file is already present
f = open('sample.txt','w')
f.write('I just want mental peace')
f.close()