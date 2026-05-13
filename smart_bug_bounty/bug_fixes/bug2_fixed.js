/**
 * Asynchronously fetches user data from a mock API.
 * Fixes applied: Async/Await implementation.
 */
async function getUserData() {
    console.log("Initiating data fetch process...");
    try {
        const response = await fetch('https://api.example.com/user/1');
        const user = await response.json();
        
        if (user && user.name) {
            console.log("Success! User Name: " + user.name);
            return user;
        }
    } catch (error) {
        console.error("An error occurred during fetch: ", error);
        return null;
    }
}

getUserData();
