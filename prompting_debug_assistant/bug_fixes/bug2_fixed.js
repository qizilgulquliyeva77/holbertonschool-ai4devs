function processUserData(userDataJson) {
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
