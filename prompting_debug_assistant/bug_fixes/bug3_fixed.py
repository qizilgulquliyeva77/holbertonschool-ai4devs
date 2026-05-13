def track_session_logs(action, current_logs=None):
    """
    Fixed Behavior: Uses None as a default value to prevent shared mutable state
    between isolated function invocations.
    """
    # AI Fix Applied: Instantiate a unique list if no argument is provided
    if current_logs is None:
        current_logs = []
        
    current_logs.append(action)
    return current_logs

# Validation Tests
session_a = track_session_logs("login")
session_b = track_session_logs("view_profile") 

assert "view_profile" not in session_a, "Bug still persists! Session isolation failed."
assert session_a == ["login"]
assert session_b == ["view_profile"]
print("bug3_fixed.py: Session state completely isolated. All tests passed.")
