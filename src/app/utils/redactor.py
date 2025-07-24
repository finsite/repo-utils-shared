# src/app/utils/redactor.py

SENSITIVE_KEYS = {"password", "secret", "token", "api_key", "authorization", "access_token"}


def redact_dict(obj):
    if not isinstance(obj, dict):
        return obj
    redacted = {}
    for key, value in obj.items():
        if key.lower() in SENSITIVE_KEYS:
            redacted[key] = "***REDACTED***"
        elif isinstance(value, dict):
            redacted[key] = redact_dict(value)
        elif isinstance(value, list):
            redacted[key] = [redact_dict(v) for v in value]
        else:
            redacted[key] = value
    return redacted
