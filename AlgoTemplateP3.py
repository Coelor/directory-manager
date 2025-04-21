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
        
    def index_file(self, file, directory):
        return 0
    ##########        implement above

    def find_file_by_name(self, filename):
        return self.file_index.get(filename, [])
        #"""Find files by exact name match"""
        return 0

        
    def wildcard_search(self, pattern):
        """Support wildcard searches using regex"""

    
    def find_by_metadata(self, criteria):
        """Search files by metadata criteria"""

        # Example: type-based search
        if 'extension' in criteria:
            ext = criteria['extension']
            if ext in self.type_index:
                for file, directory in self.type_index[ext]:
                    results.append((file, directory.get_path() + '/' + file.name))
        
        return results
    
    def find_shortest_path(self, filename):
        """Find the shortest path to a file using BFS"""
        if filename not in self.file_index:
            return None
            
        # Use BFS to find shortest path (fewest directory hops)
        from collections import deque
        
        # Find all instances of the file
    
        
        for file, directory in file_instances:
            continue# Calculate path depth

                
        return shortest_path, min_depth
    
    def find_duplicate_files(self):
        """Find duplicate files based on size and content hash"""
        # Group by size first (quick filter)

        # For files with same size, we would compare content hash
        # (in a real implementation, not just simulated)
        duplicates = []
        for size, files in size_groups.items():
            if len(files) > 1:
                continue
                # In a real implementation, we would hash file contents here
                # For simulation, just assume files with same name and size are duplicates
        
        return duplicates
    

