class File:
    def __init__(self, name, size, metadata=None):
        self.name = name
        self.size = size  # in KB
        self.metadata = metadata or {}  # For storing attributes like last modified, type, etc.
        
class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirectories = {}  # Key: name, Value: Directory object
        self.files = {}  # Key: name, Value: File object
        
    def addFile(self, file):
        self.files[file.name] = file
        
    def addDirectory(self, directory):
        self.subdirectories[directory.name] = directory
        directory.parent = self
        
    def getPath(self):
        if self.parent is None:
            return self.name
        return self.parent.getPath() + '/' + self.name
        
    def getSize(self):
        total_size = sum(file.size for file in self.files.values())
        for subdir in self.subdirectories.values():
            total_size += subdir.getSize()
        return total_size
    

class FileSystem:
    def __init__(self):
        self.root = Directory("Root")
        # Inverted index for fast file lookups regardless of location
        self.file_index = {}  # Key: filename, Value: list of references to File objects
        # Type index for quick file type searches
        self.type_index = {}  # Key: file extension, Value: list of references to File objects
        # Size index for range queries on file sizes
        self.size_index = {}  # Key: size range, Value: list of references to File objects
        
    def index_file(self, file, directory):

    ##########        implement above

    def find_file_by_name(self, filename):
        """Find files by exact name match"""
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
            # Calculate path depth

                
        return shortest_path, min_depth
    
    def find_duplicate_files(self):
        """Find duplicate files based on size and content hash"""
        # Group by size first (quick filter)

        # For files with same size, we would compare content hash
        # (in a real implementation, not just simulated)
        duplicates = []
        for size, files in size_groups.items():
            if len(files) > 1:
                # In a real implementation, we would hash file contents here
                # For simulation, just assume files with same name and size are duplicates
        
        return duplicates
    

