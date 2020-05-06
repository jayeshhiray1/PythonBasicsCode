# Python program to explain os.path.basename() method

# importing os.path module
import os.path

# Path
path = '/home/User/Documents'

# Above specified path
# will be splited into
# (head, tail) pair as
# ('/home/User', 'Documents')

# Get the base name
# of the specified path
basename = os.path.basename(path)

# Print the base name
print(basename)

# Path
path = '/home/User/Documents/file.txt'

# Above specified path
# will be splited into
# (head, tail) pair as
# ('/home/User/Documents', 'file.txt')

# Get the base name
# of the specified path
basename = os.path.basename(path)

# Print the basename name
print(basename)

# Path
path = 'file.txt'

# The above specified path
# will be splitted into
# head and tail pair
# as ('', 'file.txt')
# so 'file.txt' will be printed

# Get the base name
# of the specified path
basename = os.path.basename(path)

# Print the base name
print(basename)
