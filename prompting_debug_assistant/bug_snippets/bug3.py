def track_session_logs(action, current_logs=[]):
    """
    Intended Behavior: Append the current action to the session log list 
    and return the updated list unique to that function call.
    """
    # Bug: Mutable default argument retains state across multiple function calls
    current_logs.append(action)
    return current_logs

session_a = track_session_logs("login")
session_b = track_session_logs("view_profile") 

print(f"Session A Logs: {session_a}")
print(f"Session B Logs: {session_b}") # Bug: Contains Session A's data
