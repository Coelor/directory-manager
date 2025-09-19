class FSNode:
    """
    FSNode class represents a node in a file system hierarchy.
    This class can represent both directories and files. Directories can have children (other FSNodes),
    while files cannot. Sizes are stored only for files in kilobytes (KB).
    Attributes:
        name (str): The name of the file or directory.
        is_directory (bool): True if this node is a directory, False if it's a file.
        size (int): Size of the file in KB (only applicable for files, directories have size 0).
        metadata (dict): Dictionary for storing additional attributes like last modified time, file type, etc.
        parent (FSNode): Reference to the parent node. None for the root node.
        children (dict): Dictionary of child nodes, with names as keys and FSNode objects as values.
                        Only directories have children; for files, this is None.
    Methods:
        add_child(node): Adds a child node to a directory.
        get_path(): Returns the full path from root to this node.
        get_size(): For files, returns the file size. For directories, returns the sum of all contained files.
        create_file(name, size, metadata=None, parent=None): Factory function to create a file node.
        create_directory(name, parent=None): Factory function to create a directory node.
    """
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

    def create_file(name, size, metadata=None, parent=None):
        return FSNode(name, is_directory=False, size=size, metadata=metadata, parent=parent)

    def create_directory(name, parent=None):
        return FSNode(name, is_directory=True, parent=parent)
