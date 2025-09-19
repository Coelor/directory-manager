from collections import deque
from fsnode import FSNode
import fnmatch


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
                new_dir = FSNode.create_directory(path, parent=current_node)
                current_node.add_child(new_dir)
            current_node = current_node.children[path]

        current_node.add_child(file_node)
        self.index_file(file_node, current_node)

    def index_file(self, file, directory):
        # """Index the file for quick lookups"""
        # Add to file index
        if file.name not in self.file_index:
            self.file_index[file.name] = []
        self.file_index[file.name].append((file, directory))

        # Add to type index
        ext = file.metadata.get('extension', 'unknown')
        if ext not in self.type_index:
            self.type_index[ext] = []
        self.type_index[ext].append((file, directory))

        # Add to size index
        size = file.get_size()
        if size not in self.size_index:
            self.size_index[size] = []
        self.size_index[size].append((file, directory))

    def find_file_by_name(self, filename):
        # """Find files by exact name match and return their full paths."""
        results = self.file_index.get(filename, [])
        return [directory.get_path() + '/' + file.name for file, directory in results]

    def wildcard_search(self, pattern):
        # """Support wildcard searches using regex"""
        results = []
        for filename in self.file_index:
            if fnmatch.fnmatch(filename, pattern):
                for file, directory in self.file_index[filename]:
                    results.append(f"{directory.get_path()}/{file.name} ({file.get_size()} KB)")
        return results

    def find_by_metadata(self, criteria):
        """Search files by metadata criteria"""
        results = []
        # Example: type-based search
        if 'extension' in criteria:
            ext = criteria['extension']
            if ext in self.type_index:
                for file, directory in self.type_index[ext]:
                    results.append(f"{directory.get_path()}/{file.name} ({file.get_size()} KB)")

        return results

    def find_shortest_path(self, filename):
        # """Find the shortest access path to a file using BFS (fewest directory hops)."""
        queue = deque([(self.root, [self.root.name])])  # (node, path_so_far)
        shortest_path = None
        min_depth = float('inf')

        while queue:
            current_node, path = queue.popleft()

            if not current_node.is_directory:
                if current_node.name == filename:
                    depth = len(path)
                    if depth < min_depth:
                        shortest_path = path.copy()
                        min_depth = depth
            else:
                for child in current_node.children.values():
                    queue.append((child, path + [child.name]))

        if shortest_path:
            return "/".join(shortest_path), min_depth - 1
        return None

    def find_duplicate_files(self):
        # """Find duplicates files based on name and size"""
        seen = {}
        duplicates = []

        for filename, entries in self.file_index.items():
            for file, directory in entries:
                key = (file.name, file.get_size())
                path = f"{directory.get_path()}/{file.name} ({file.get_size()} KB)"

                if key in seen:
                    if seen[key] is not None:
                        duplicates.append(seen[key])
                        seen[key] = None
                    duplicates.append(path)
                else:
                    seen[key] = path
        
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
