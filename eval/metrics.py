def classify_out_of_domain_response(response):
    response = response.lower()

    if any(word in response for word in ["programming", "language", "technology"]):
        return 0  # bad: modern knowledge leakage
    
    if any(word in response for word in ["i don't know", "i am not familiar"]):
        return 1  # medium
    
    if any(word in response for word in ["what", "never heard", "strange", "?"]):
        return 2  # good: in-character confusion
    
    return 1