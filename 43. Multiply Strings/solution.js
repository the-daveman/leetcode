/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    const product = Array(num1.length+num2.length).fill(0);
    for (let i = num1.length; i--; null) {
        let carry = 0;
        for (let j = num2.length; j--; null) {
            product[1+i+j] += carry + num1[i]*num2[j];
            carry = Math.floor(product[1+i+j] / 10);
            product[1+i+j] = product[1+i+j] % 10;
        }
        product[i] += carry;
    }
    return product.join("").replace(/^0*(\d)/, "$1");
};
