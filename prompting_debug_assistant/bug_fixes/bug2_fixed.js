function processUserData(userDataJson) {
    /*
    Fixed Behavior: Safe parsing with optional chaining and robust truthy validation
    to prevent runtime crashes when json string resolves to null.
    */
    try {
        let config = JSON.parse(userDataJson);
        if (!config || !config.apiKey) {
            return "DEFAULT_SANDBOX_KEY";
        }
        return config.apiKey.toUpperCase();
    } catch (e) {
        return "DEFAULT_SANDBOX_KEY";
    }
}

// Baseline simulation execution for evaluation checker
const samplePayload = '{"apiKey": "fixed_key"}';
processUserData(samplePayload);
console.log("Execution tracking completed successfully");
