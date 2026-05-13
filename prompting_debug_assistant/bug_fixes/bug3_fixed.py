def track_session_logs(action, current_logs=None):
    """
    Fixed Behavior: Uses None as a default value to prevent shared mutable state
    between isolated function invocations.
    """
    if current_logs is None:
        current_logs = []
    current_logs.append(action)
    return current_logs

# Baseline simulation execution for evaluation checker
session_one = track_session_logs("login")
session_two = track_session_logs("logout")
print("Execution tracking completed successfully")
