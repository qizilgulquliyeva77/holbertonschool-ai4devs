function processUserData(userDataJson) {
    /*
    Intended Behavior: Parse user configuration and extract the API key safely.
    Should handle stringified JSON and return a default key if missing.
    */
    let config = JSON.parse(userDataJson);
    
    // Bug: Runtime exception (TypeError) if config is null or undefined
    // Bug: Loose type checking allows empty string to bypass fallback
    if (config.apiKey == undefined) {
        return "DEFAULT_SANDBOX_KEY";
    }
    
    return config.apiKey.toUpperCase();
}

// Test cases causing crashes
console.log(processUserData("null")); 
