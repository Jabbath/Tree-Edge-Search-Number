# Tree Edge Search

This is a NetworkX graph theory package that calculates the edge search number of a tree. The algorithm is based off of The Complexity of Searching a Graph by N. Megiddo et. al. The algorithm runs in O(nlog(n)) and is very fast for small to mid sized trees (hundreds of vertices).

## Usage

First, install the package with:

```
pip install tree-search-number
```

Then, similar code to the below can be used to calculate the search number of a tree. Note that the package does not check if the passed graph is a tree. Whether the graph is a tree should be checked to ensure correct behavior.

```python
from tree_search_number.tree import edge_search
import networkx as nx

G = nx.balanced_tree(2, 4)

print edge_search(G)
#3
```

## Contributing

If you feel that you have something useful to add, feel free to submit a pull request.

## License

Licensed under the MIT license. See license.txt.
