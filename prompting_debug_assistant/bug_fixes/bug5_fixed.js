// FIXED: Added the 'async' keyword to the function declaration.
// This allows the use of 'await' inside the function without throwing a SyntaxError.

async function fetchUserData(userId) {
    console.log(`Starting fetch operation for user ID: ${userId}`);
    
    const apiUrl = `https://api.example.com/users/${userId}`;
    
    const response = await fetch(apiUrl);
    
    if (!response.ok) {
        console.error("Failed to fetch user data.");
    }
    
    console.log("Data fetched, parsing JSON...");
    
    // Also added await here to properly resolve the promise
    const data = await response.json(); 
    
    return data;
}
