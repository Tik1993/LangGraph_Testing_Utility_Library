def test_whole_graph(graph, initial_state=None, expected_final_state=None):
    """
    Execute the entire graph and check if the final state matches the expected state.
    
    Parameters:
        graph: LangGraph object with a .compile() method returning an object with .invoke(state)
        initial_state: dict, the initial state to pass to the graph.
        expected_final_state: dict, the expected final state to compare against.
        
    Returns:
        True if the final state matches the expected state, False otherwise.
    """
    state= initial_state or {}
    compile_graph = graph.compile()
    result = compile_graph.invoke(state)
    return result == expected_final_state

def test_whole_graph_state(graph, state_keys=None, initial_state=None, expected_final_state=None):
    """
    Execute the whole graph and check if specified state keys match the expected final result

    Parameters:
        graph: LangGraph object with a .compile() method returning an object with .invoke(state)
        state_keys: list of str, the keys in the state to check
        initial_state: dict, the initial state to pass to the graph.
        expected_final_state: dict, the expected final state to compare against.
    
    Returns:
        True if all keys in state_keys match the expected final result, False otherwise
    """
    state= initial_state or {}
    compile_graph = graph.compile()
    result = compile_graph.invoke(state)
    for key in state_keys:
        if result[key] != expected_final_state[key]:
            return False
    return True

def test_individual_node(graph, node, state_keys=None, initial_state=None, expected_state=None):
    """
    Execute the graph up to a specific node and check if specified state keys of that node match the expected state.

    Parameters:
        graph: LangGraph object with a .compile() method returning an object with .invoke(state)
        node: str, the name of the node to test
        state_keys: list of str, the keys in the state to check; if None, the whole state of the node will be checked
        initial_state: dict, the initial state to pass to the graph.
        expected_state: dict, the expected final state to compare against.
    
    Returns:
        True if all specified keys (or the whole node state if state_keys is None) match the expected_state, False otherwise
    """
    state= initial_state or {}
    compile_graph = graph.compile()
    result = compile_graph.nodes[node].invoke(state)
    if state_keys:
        for key in state_keys:
            if result[key] != expected_state[key]:
                return False
        return True
    return result == expected_state