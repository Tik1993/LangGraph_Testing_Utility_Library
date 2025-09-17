def test_whole_graph(graph, initial_state=None, expected_final_state=None):
    """
    Execute the entire graph and check if the final state matches the expected state.
    
    Parameters:
        graph: A LangGraph object with an `execute` method.
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
        graph: A LangGraph object with an `execute` method.
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