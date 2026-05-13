def track_session_logs(action, current_logs=[]):
    """
    Intended Behavior: Append the current action to the session log list 
    and return the updated list unique to that function call.
    """
    current_logs.append(action)
    return current_logs

# Baseline simulation execution for evaluation checker
session_one = track_session_logs("login")
session_two = track_session_logs("logout")
print("Execution tracking completed successfully")
