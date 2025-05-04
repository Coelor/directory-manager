from collections import deque


class FSNode:
    def __init__(self, name, is_directory=False, size=0, metadata=None, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.size = size if not is_directory else 0  # in KB (only for files)
        self.metadata = metadata or {}  # For storing attributes like last modified, type, etc.
        self.parent = parent
        self.children = {} if is_directory else None  # Only directories have children

    def add_child(self, node):
        if not self.is_directory:
            raise ValueError("Cannot add child to a file")
        self.children[node.name] = node
        node.parent = self

    def get_path(self):
        if self.parent is None:
            return self.name
        return self.parent.get_path() + '/' + self.name

    def get_size(self):
        if not self.is_directory:
            return self.size

        total_size = 0
        for child in self.children.values():
            total_size += child.get_size()
        return total_size


# Factory functions to create specific node types
def create_file(name, size, metadata=None, parent=None):
    return FSNode(name, is_directory=False, size=size, metadata=metadata, parent=parent)


def create_directory(name, parent=None):
    return FSNode(name, is_directory=True, parent=parent)


class FileSystem:
    def __init__(self):
        self.root = FSNode("Root", is_directory=True)
        # Inverted index for fast file lookups regardless of location
        self.file_index = {}  # Key: filename, Value: list of references to File objects
        # Type index for quick file type searches
        self.type_index = {}  # Key: file extension, Value: list of references to File objects
        # Size index for range queries on file sizes
        self.size_index = {}  # Key: size range, Value: list of references to File objects

    def add_file(self, path_list, file_node):
        current_node = self.root

        for path in path_list:
            if path not in current_node.children:
                new_dir = create_directory(path, parent=current_node)
                current_node.add_child(new_dir)
            current_node = current_node.children[path]

        current_node.add_child(file_node)
        self.index_file(file_node, current_node)

    def index_file(self, file, directory):
        return 0

    def find_file_by_name(self, filename):
        # """Find files by exact name match"""
        return self.file_index.get(filename, [])

    def wildcard_search(self, pattern):
        # """Support wildcard searches using regex"""
        return 0

    def find_by_metadata(self, criteria):
        """Search files by metadata criteria"""
        results = []
        # Example: type-based search
        if 'extension' in criteria:
            ext = criteria['extension']
            if ext in self.type_index:
                for file, directory in self.type_index[ext]:
                    results.append((file, directory.get_path() + '/' + file.name))

        return results

    def find_shortest_path(self, filename):
        shortest_path = None
        min_depth = float('inf')
        file_instances = self.find_file_by_name(filename)
        if not file_instances:
            return None
        # """Find the shortest path to a file using BFS"""
        if filename not in self.file_index:
            return None
        # Use BFS to find shortest path (fewest directory hops)

        # Find all instances of the file

        for file, directory in file_instances:
            continue  # Calculate path depth

        return shortest_path, min_depth

    def find_duplicate_files(self):
        """Find duplicate files based on size and content hash"""
        # Group by size first (quick filter)
        size_groups = {}
        # For files with same size, we would compare content hash
        # (in a real implementation, not just simulated)
        duplicates = []
        for size, files in size_groups.items():
            if len(files) > 1:
                continue
                # In a real implementation, we would hash file contents here
                # For simulation, just assume files with same name and size are duplicates

        return duplicates

    def print_directory(self, node=None, level=0):  # DFS traversal
        """Print the directory structure"""
        if node is None:
            node = self.root
        indent = ' ' * (level * 2)
        print(f"{indent}{node.name} ({'Dir' if node.is_directory else 'File'}, Size: {node.get_size()} KB)")
        if node.is_directory:
            for child in node.children.values():
                self.print_directory(child, level + 1)


fs = FileSystem()
# Example usage
fs.add_file(['dir1', 'subdir1'], create_file('file1.txt', 100, {'extension': 'txt'}))
fs.add_file(['dir1', 'subdir2'], create_file('file2.txt', 200, {'extension': 'txt'}))
fs.add_file(['dir2'], create_file('file3.jpg', 300, {'extension': 'jpg'}))

print(fs.find_file_by_name('file1.txt'))
print(fs.find_by_metadata({'extension': 'txt'}))
print(fs.find_shortest_path('file3.jpg'))
print(fs.find_duplicate_files())
fs.print_directory()
