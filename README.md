# LangGraph Testing Utility Library

A small Python library to help test **LangGraph** workflows. Provides utility functions for:

- Running the entire graph end-to-end
- Testing individual nodes and edges
- Partial execution of the graph

## Installation

You can install the library locally for development:

```bash
git clone <your-repo-url>
cd LangGraph_Testing_Utility_Library
pip install -e .
```

## API Reference

### `test_whole_graph(graph, initial_state=None, expected_final_state=None)`

**Description:**  
Executes the entire LangGraph and checks if the final state matches the expected state.  
Use this to verify the end-to-end behavior of your graph.

**Parameters:**

| Name                   | Type             | Description                                                                                              |
| ---------------------- | ---------------- | -------------------------------------------------------------------------------------------------------- |
| `graph`                | LangGraph object | A graph object with a `.compile()` method that returns an object with `.invoke(state)`                   |
| `initial_state`        | dict, optional   | The initial state to pass into the graph. Defaults to an empty dictionary `{}`                           |
| `expected_final_state` | dict, optional   | The state expected after the graph executes. If provided, the function compares the result to this state |

**Returns:**

- `True` if the final state matches `expected_final_state`
- `False` otherwise

### `test_whole_graph_state(graph, state_keys, initial_state=None, expected_final_state=None)`

**Description:**  
Executes the entire LangGraph and checks whether the specified state keys match the expected values.  
Use this when you want to test **specific parts of the graph state** without comparing the full state.

**Parameters:**

| Name                   | Type             | Description                                                                         |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------------- |
| `graph`                | LangGraph object | A graph object with a `.compile()` method returning an object with `.invoke(state)` |
| `state_keys`           | list of str      | The keys in the state to check                                                      |
| `initial_state`        | dict, optional   | Initial state to pass into the graph. Defaults to `{}`                              |
| `expected_final_state` | dict             | Key-value pairs of the expected values for the specified keys                       |

**Returns:**

- `True` if all keys in `state_keys` match the expected values in `expected_final_state`
- `False` otherwise

### `test_individual_node(graph, node, state_keys=None, initial_state=None, expected_state=None)`

**Description:**  
Execute the graph up to a specific node and check if specified state keys of that node match the expected state.  
Use this to test **individual nodes** without running full graph state comparisons.

**Parameters:**

| Name             | Type                  | Description                                                                                     |
| ---------------- | --------------------- | ----------------------------------------------------------------------------------------------- |
| `graph`          | LangGraph object      | A graph object with a `.compile()` method returning an object with `.nodes[node].invoke(state)` |
| `node`           | str                   | The name of the node to test                                                                    |
| `state_keys`     | list of str, optional | Keys in the node's state to check; if `None`, the whole node state is compared                  |
| `initial_state`  | dict, optional        | Initial state to pass to the graph. Defaults to `{}`                                            |
| `expected_state` | dict                  | Expected key-value pairs for the node's state                                                   |

**Returns:**

- `True` if all specified keys (or the whole node state if `state_keys` is `None`) match `expected_state`
- `False` otherwise

### `test_partial_execution(graph, node_before_start_node, end_node, state_keys=None, initial_state=None, expected_state=None)`

**Description:**  
Execute a LangGraph **partially**, starting immediately after a given node and stopping at a specified end node.  
The resulting state at interruption is compared against the `expected_state`.  
Use this to test **subsections of a graph** without running the entire workflow.

**Parameters:**

| Name                     | Type                  | Description                                                                                     |
| ------------------------ | --------------------- | ----------------------------------------------------------------------------------------------- |
| `graph`                  | LangGraph object      | A graph object with a `.compile()` method returning an object with `.invoke(state)`             |
| `node_before_start_node` | str                   | The node immediately before the desired start point. Execution resumes just **after** this node |
| `end_node`               | str                   | The node at which execution stops, using `interrupt_after`                                      |
| `state_keys`             | list of str, optional | Keys in the state to check. If `None`, the entire state is compared                             |
| `initial_state`          | dict, optional        | Initial state to pass to the graph. Defaults to `{}`                                            |
| `expected_state`         | dict                  | Expected key-value pairs for the state at interruption                                          |

**Returns:**

- `True` if all specified keys (or the full state if `state_keys` is `None`) match `expected_state`
- `False` otherwise
