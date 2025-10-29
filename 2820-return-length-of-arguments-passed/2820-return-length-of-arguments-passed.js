/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    a=0
    for(i=0;i<args.length;i++){
    a++
    }
    return a
};

/**
 * argumentsLength(1, 2, 3); // 3
 */