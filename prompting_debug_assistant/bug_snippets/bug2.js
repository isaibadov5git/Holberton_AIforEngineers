function findFirstEven(numbers) {
    let result = null;
    
    // BUG: Logical error. 'return' inside forEach only exits the callback, 
    // it does NOT return from the outer function.
    numbers.forEach(num => {
        if (num % 2 === 0) {
            return num; 
        }
    });
    
    return result; 
}
