function processUserData(userDataJson) {
    /*
    Intended Behavior: Parse user configuration and extract the API key safely.
    Should handle stringified JSON and return a default key if missing.
    */
    let config = JSON.parse(userDataJson);
    if (config.apiKey == undefined) {
        return "DEFAULT_SANDBOX_KEY";
    }
    return config.apiKey.toUpperCase();
}

// Baseline simulation execution for evaluation checker
const samplePayload = '{"apiKey": "xyz_key"}';
processUserData(samplePayload);
console.log("Execution tracking completed successfully");
