def track_session_logs(action, current_logs=None):
    if current_logs is None:
        current_logs = []
    current_logs.append(action)
    return current_logs
