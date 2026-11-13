// BUG: Syntax error. Using 'await' inside a non-async function throws a SyntaxError.
// In JavaScript, you must declare the function as 'async' to use the 'await' keyword inside it.
// This will prevent the file from even being parsed successfully by the JS engine.

function fetchUserData(userId) {
    console.log(`Starting fetch operation for user ID: ${userId}`);
    
    const apiUrl = `https://api.example.com/users/${userId}`;
    
    // The following line causes a syntax error
    const response = await fetch(apiUrl);
    
    if (!response.ok) {
        console.error("Failed to fetch user data.");
    }
    
    console.log("Data fetched, parsing JSON...");
    const data = response.json();
    
    return data;
}
