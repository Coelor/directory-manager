from filesystem import FileSystem, FSNode
from utils import measure_time, print_results

fs = FileSystem()
# Example usage
fs.add_file(['dir1', 'subdir1'], FSNode.create_file('file1.txt', 100, {'extension': 'txt'}))
fs.add_file(['dir1', 'subdir2'], FSNode.create_file('file1.txt', 100, {'extension': 'txt'}))
fs.add_file(['dir1', 'subdir2'], FSNode.create_file('file2.txt', 200, {'extension': 'txt'}))
fs.add_file(['dir1', 'subdir1', 'subdir1-1'], FSNode.create_file('file3.jpg', 300, {'extension': 'jpg'}))
fs.add_file(['dir1', 'subdir1', 'subdir1-1', 'subdir1-1-1'], FSNode.create_file('file4.txt', 50, {'extension': 'txt'}))
fs.add_file(['dir2'], FSNode.create_file('file3.jpg', 300, {'extension': 'jpg'}))
fs.add_file(['dir2', 'subdir3'], FSNode.create_file('file5.doc', 250, {'extension': 'doc'}))
fs.add_file(['dir2', 'subdir3', 'subdir3-1'], FSNode.create_file('file6.txt', 75, {'extension': 'txt'}))
fs.add_file(['dir1', 'subdir1'], FSNode.create_file('file6.txt', 75, {'extension': 'txt'}))
fs.add_file(['dir3'], FSNode.create_file('archive.zip', 500, {'extension': 'zip'}))
fs.add_file(['dir3', 'backup'], FSNode.create_file('file7.txt', 90, {'extension': 'txt'}))
fs.add_file(['dir3', 'backup'], FSNode.create_file('notes.md', 60, {'extension': 'md'}))
fs.add_file(['dir3', 'backup', '2025'], FSNode.create_file('log1.txt', 30, {'extension': 'txt'}))
fs.add_file(['dir3', 'backup', '2025'], FSNode.create_file('log2.txt', 40, {'extension': 'txt'}))
fs.add_file(['dir3', 'backup', '2025'], FSNode.create_file('log3.txt', 30, {'extension': 'txt'}))
fs.add_file(['dir3', 'images'], FSNode.create_file('image1.png', 120, {'extension': 'png'}))
fs.add_file(['dir3', 'images'], FSNode.create_file('image2.png', 180, {'extension': 'png'}))
fs.add_file(['dir3', 'images'], FSNode.create_file('image3.jpg', 200, {'extension': 'jpg'}))
fs.add_file(['dir3', 'docs'], FSNode.create_file('manual.pdf', 220, {'extension': 'pdf'}))
fs.add_file(['dir3', 'docs'], FSNode.create_file('license.txt', 15, {'extension': 'txt'}))


print("Finding files by name 'file1.txt':")
result = measure_time(fs.find_file_by_name, 'file1.txt')
print_results("Results:", result)

print("\nFinding files by extension 'txt':")
result = measure_time(fs.find_by_metadata, {'extension': 'txt'})
print_results("Results:", result)

print("\nCalculating size of 'dir1':")
result = measure_time(fs.root.children['dir1'].get_size)
print(f"Size of 'dir1': {result} KB")

print("\nwildcard search for '*.txt':")
result = measure_time(fs.wildcard_search, '*.txt')
print_results("Results:", result)

print("\nFinding shortest path to 'file3.jpg':")
result = measure_time(fs.find_shortest_path, 'file3.jpg')
print(result)

print("\nFinding duplicate files:")
result = measure_time(fs.find_duplicate_files)
print_results("Results:", result)

print("\nDirectory structure:")
measure_time(fs.print_directory)

print("\nDirectory structure for 'dir1':")
measure_time(fs.print_directory, fs.root.children['dir1'])
