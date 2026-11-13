function findFirstEven(numbers) {
    let result = null;
    
    console.log("Searching for the first even number...");
    
    // BUG: Logical error. 'return' inside forEach only exits the callback, 
    // it does NOT return from the findFirstEven function.
    numbers.forEach(num => {
        console.log(`Checking number: ${num}`);
        if (num % 2 === 0) {
            console.log("Found an even number!");
            return num; // This only returns from the arrow function
        }
    });
    
    // This will always return null because the forEach doesn't update 'result'
    // and the 'return num' above doesn't escape the outer function.
    return result; 
}
