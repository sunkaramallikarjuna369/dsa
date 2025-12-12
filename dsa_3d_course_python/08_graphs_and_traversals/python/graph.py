"""
Graph Module

This module provides implementations of graph data structures
and traversal algorithms with step-by-step tracking for 3D visualization.

Includes adjacency list representation, BFS, DFS, and related algorithms.
"""

from typing import TypeVar, Generic, Iterator
from dataclasses import dataclass, field
from collections import deque

T = TypeVar('T')


@dataclass
class GraphStep:
    """Represents a single step in graph visualization."""
    step_number: int
    operation: str
    description: str
    current_node: T | None = None
    neighbor: T | None = None
    edge: tuple[T, T] | None = None
    visited: set[T] = field(default_factory=set)
    queue_or_stack: list[T] = field(default_factory=list)
    level: int = -1
    path: list[T] = field(default_factory=list)


class Graph(Generic[T]):
    """
    Graph implementation using adjacency list.
    
    Supports both directed and undirected graphs.
    
    Time Complexity:
    - Add vertex: O(1)
    - Add edge: O(1)
    - Remove edge: O(degree)
    - Check edge: O(degree)
    - Get neighbors: O(1)
    - BFS/DFS: O(V + E)
    """
    
    def __init__(self, directed: bool = False) -> None:
        """
        Initialize an empty graph.
        
        Args:
            directed: If True, edges are directed. Default is undirected.
        """
        self._adj: dict[T, list[T]] = {}
        self._directed = directed
        self._steps: list[GraphStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        current_node: T | None = None,
        neighbor: T | None = None,
        edge: tuple[T, T] | None = None,
        visited: set[T] | None = None,
        queue_or_stack: list[T] | None = None,
        level: int = -1,
        path: list[T] | None = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = GraphStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            current_node=current_node,
            neighbor=neighbor,
            edge=edge,
            visited=visited.copy() if visited else set(),
            queue_or_stack=list(queue_or_stack) if queue_or_stack else [],
            level=level,
            path=list(path) if path else []
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[GraphStep]:
        """Return all recorded steps."""
        return self._steps
    
    @property
    def is_directed(self) -> bool:
        """Return True if graph is directed."""
        return self._directed
    
    def add_vertex(self, vertex: T) -> None:
        """Add a vertex to the graph."""
        if vertex not in self._adj:
            self._adj[vertex] = []
    
    def add_edge(self, u: T, v: T) -> None:
        """
        Add an edge between vertices u and v.
        
        For undirected graphs, adds edge in both directions.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        
        if v not in self._adj[u]:
            self._adj[u].append(v)
        
        if not self._directed and u not in self._adj[v]:
            self._adj[v].append(u)
    
    def remove_edge(self, u: T, v: T) -> None:
        """Remove edge between u and v."""
        if u in self._adj and v in self._adj[u]:
            self._adj[u].remove(v)
        
        if not self._directed:
            if v in self._adj and u in self._adj[v]:
                self._adj[v].remove(u)
    
    def has_edge(self, u: T, v: T) -> bool:
        """Check if edge exists between u and v."""
        return u in self._adj and v in self._adj[u]
    
    def neighbors(self, vertex: T) -> list[T]:
        """Return list of neighbors for a vertex."""
        return self._adj.get(vertex, [])
    
    def vertices(self) -> list[T]:
        """Return list of all vertices."""
        return list(self._adj.keys())
    
    def edges(self) -> list[tuple[T, T]]:
        """Return list of all edges."""
        result: list[tuple[T, T]] = []
        seen: set[tuple[T, T]] = set()
        
        for u in self._adj:
            for v in self._adj[u]:
                edge = (u, v)
                reverse = (v, u)
                
                if self._directed:
                    result.append(edge)
                elif edge not in seen and reverse not in seen:
                    result.append(edge)
                    seen.add(edge)
        
        return result
    
    def degree(self, vertex: T) -> int:
        """Return degree of a vertex."""
        return len(self._adj.get(vertex, []))
    
    def vertex_count(self) -> int:
        """Return number of vertices."""
        return len(self._adj)
    
    def edge_count(self) -> int:
        """Return number of edges."""
        count = sum(len(neighbors) for neighbors in self._adj.values())
        return count if self._directed else count // 2
    
    def bfs(self, start: T) -> list[T]:
        """
        Breadth-First Search traversal.
        
        Explores vertices level by level, like ripples in water.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Returns:
            List of vertices in BFS order.
        """
        if start not in self._adj:
            return []
        
        visited: set[T] = set()
        result: list[T] = []
        queue: deque[T] = deque([start])
        visited.add(start)
        level = 0
        
        self._record_step(
            "bfs_start",
            f"Starting BFS from {start}",
            current_node=start,
            visited=visited,
            queue_or_stack=list(queue),
            level=level
        )
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                current = queue.popleft()
                result.append(current)
                
                self._record_step(
                    "visit",
                    f"Visiting {current} at level {level}",
                    current_node=current,
                    visited=visited,
                    queue_or_stack=list(queue),
                    level=level
                )
                
                for neighbor in self._adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
                        self._record_step(
                            "discover",
                            f"Discovered {neighbor} from {current}",
                            current_node=current,
                            neighbor=neighbor,
                            edge=(current, neighbor),
                            visited=visited,
                            queue_or_stack=list(queue),
                            level=level + 1
                        )
            
            level += 1
        
        self._record_step(
            "bfs_complete",
            f"BFS complete. Order: {result}",
            visited=visited,
            path=result
        )
        
        return result
    
    def dfs(self, start: T) -> list[T]:
        """
        Depth-First Search traversal (iterative).
        
        Explores as deep as possible before backtracking.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Returns:
            List of vertices in DFS order.
        """
        if start not in self._adj:
            return []
        
        visited: set[T] = set()
        result: list[T] = []
        stack: list[T] = [start]
        
        self._record_step(
            "dfs_start",
            f"Starting DFS from {start}",
            current_node=start,
            queue_or_stack=stack
        )
        
        while stack:
            current = stack.pop()
            
            if current in visited:
                continue
            
            visited.add(current)
            result.append(current)
            
            self._record_step(
                "visit",
                f"Visiting {current}",
                current_node=current,
                visited=visited,
                queue_or_stack=stack,
                path=result
            )
            
            # Add neighbors in reverse order for consistent traversal
            for neighbor in reversed(self._adj[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
                    self._record_step(
                        "push",
                        f"Pushing {neighbor} to stack",
                        current_node=current,
                        neighbor=neighbor,
                        edge=(current, neighbor),
                        visited=visited,
                        queue_or_stack=stack
                    )
        
        self._record_step(
            "dfs_complete",
            f"DFS complete. Order: {result}",
            visited=visited,
            path=result
        )
        
        return result
    
    def dfs_recursive(self, start: T) -> list[T]:
        """
        Depth-First Search traversal (recursive).
        
        Returns:
            List of vertices in DFS order.
        """
        visited: set[T] = set()
        result: list[T] = []
        
        def dfs_helper(vertex: T) -> None:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self._adj[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        if start in self._adj:
            dfs_helper(start)
        
        return result
    
    def shortest_path_bfs(self, start: T, end: T) -> list[T] | None:
        """
        Find shortest path between start and end using BFS.
        
        Works for unweighted graphs.
        
        Returns:
            List of vertices in path, or None if no path exists.
        """
        if start not in self._adj or end not in self._adj:
            return None
        
        if start == end:
            return [start]
        
        visited: set[T] = {start}
        queue: deque[T] = deque([start])
        parent: dict[T, T] = {}
        
        while queue:
            current = queue.popleft()
            
            for neighbor in self._adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
                    
                    if neighbor == end:
                        # Reconstruct path
                        path: list[T] = []
                        node: T | None = end
                        while node is not None:
                            path.append(node)
                            node = parent.get(node)
                        return path[::-1]
        
        return None
    
    def connected_components(self) -> list[list[T]]:
        """
        Find all connected components in an undirected graph.
        
        Returns:
            List of components, each component is a list of vertices.
        """
        visited: set[T] = set()
        components: list[list[T]] = []
        
        for vertex in self._adj:
            if vertex not in visited:
                component: list[T] = []
                queue: deque[T] = deque([vertex])
                visited.add(vertex)
                
                while queue:
                    current = queue.popleft()
                    component.append(current)
                    
                    for neighbor in self._adj[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                components.append(component)
        
        return components
    
    def has_cycle(self) -> bool:
        """
        Check if graph contains a cycle.
        
        Uses DFS with coloring for directed graphs.
        """
        if self._directed:
            return self._has_cycle_directed()
        else:
            return self._has_cycle_undirected()
    
    def _has_cycle_directed(self) -> bool:
        """Check for cycle in directed graph using DFS coloring."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color: dict[T, int] = {v: WHITE for v in self._adj}
        
        def dfs(vertex: T) -> bool:
            color[vertex] = GRAY
            
            for neighbor in self._adj[vertex]:
                if color[neighbor] == GRAY:
                    return True  # Back edge found
                if color[neighbor] == WHITE and dfs(neighbor):
                    return True
            
            color[vertex] = BLACK
            return False
        
        for vertex in self._adj:
            if color[vertex] == WHITE:
                if dfs(vertex):
                    return True
        
        return False
    
    def _has_cycle_undirected(self) -> bool:
        """Check for cycle in undirected graph."""
        visited: set[T] = set()
        
        def dfs(vertex: T, parent: T | None) -> bool:
            visited.add(vertex)
            
            for neighbor in self._adj[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True  # Back edge to non-parent
            
            return False
        
        for vertex in self._adj:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        
        return False
    
    def topological_sort(self) -> list[T] | None:
        """
        Topological sort for directed acyclic graph (DAG).
        
        Returns:
            List of vertices in topological order, or None if cycle exists.
        """
        if not self._directed:
            raise ValueError("Topological sort requires directed graph")
        
        if self.has_cycle():
            return None
        
        visited: set[T] = set()
        result: list[T] = []
        
        def dfs(vertex: T) -> None:
            visited.add(vertex)
            for neighbor in self._adj[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(vertex)
        
        for vertex in self._adj:
            if vertex not in visited:
                dfs(vertex)
        
        return result[::-1]
    
    def __str__(self) -> str:
        """String representation of the graph."""
        lines = []
        graph_type = "Directed" if self._directed else "Undirected"
        lines.append(f"{graph_type} Graph:")
        for vertex in sorted(self._adj.keys(), key=str):
            neighbors = ", ".join(str(n) for n in self._adj[vertex])
            lines.append(f"  {vertex}: [{neighbors}]")
        return "\n".join(lines)


def demo() -> None:
    """Run demonstrations of graph operations."""
    print("\n" + "="*60)
    print("GRAPH DEMONSTRATIONS")
    print("="*60)
    
    # Create undirected graph
    print("\n--- Undirected Graph ---")
    g: Graph[str] = Graph()
    
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), 
             ("C", "E"), ("C", "F"), ("E", "F")]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print(g)
    print(f"\nVertices: {g.vertex_count()}")
    print(f"Edges: {g.edge_count()}")
    
    # BFS
    print("\n--- BFS from A ---")
    bfs_order = g.bfs("A")
    print(f"BFS order: {bfs_order}")
    
    # DFS
    print("\n--- DFS from A ---")
    g.clear_steps()
    dfs_order = g.dfs("A")
    print(f"DFS order: {dfs_order}")
    
    # Shortest path
    print("\n--- Shortest Path A to F ---")
    path = g.shortest_path_bfs("A", "F")
    print(f"Path: {path}")
    
    # Connected components
    print("\n--- Connected Components ---")
    g2: Graph[int] = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(4, 5)
    g2.add_edge(6, 6)  # Self-loop for isolated node
    
    components = g2.connected_components()
    print(f"Components: {components}")
    
    # Directed graph with cycle detection
    print("\n--- Directed Graph Cycle Detection ---")
    dg: Graph[int] = Graph(directed=True)
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 2)  # Creates cycle
    
    print(dg)
    print(f"Has cycle: {dg.has_cycle()}")
    
    # Topological sort
    print("\n--- Topological Sort ---")
    dag: Graph[str] = Graph(directed=True)
    dag.add_edge("A", "B")
    dag.add_edge("A", "C")
    dag.add_edge("B", "D")
    dag.add_edge("C", "D")
    
    print(dag)
    topo = dag.topological_sort()
    print(f"Topological order: {topo}")


if __name__ == "__main__":
    demo()
