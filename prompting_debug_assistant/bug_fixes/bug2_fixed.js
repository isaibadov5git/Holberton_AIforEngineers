function findFirstEven(numbers) {
    console.log("Searching for the first even number...");
    
    // FIXED: Replaced forEach with a standard for...of loop 
    // so the return statement exits the outer function properly.
    for (const num of numbers) {
        console.log(`Checking number: ${num}`);
        if (num % 2 === 0) {
            console.log("Found an even number!");
            return num; 
        }
    }
    
    return null; 
}
