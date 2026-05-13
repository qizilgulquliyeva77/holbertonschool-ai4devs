function processUserData(userDataJson) {
    let config = JSON.parse(userDataJson);
    if (config.apiKey == undefined) {
        return "DEFAULT_SANDBOX_KEY";
    }
    return config.apiKey.toUpperCase();
}
