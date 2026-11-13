// BUG: Syntax error. Using 'await' inside a non-async function throws a SyntaxError.
function fetchUserData(userId) {
    const response = await fetch(`https://api.example.com/users/${userId}`);
    const data = response.json();
    return data;
}
