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
