/**
 * Lektion 3 - Kontrollfluss:
 * 7kyu | Find the nth Digit of a Number
 * https://www.codewars.com/kata/577b9960df78c19bca00007e/javascript
 */

function findDigit(num, nth) {
    if (nth <= 0) return -1;
    var txt = Math.abs(num).toString();
    var pos = txt.length - nth;
    if (pos < 0) return 0;
    return Number(txt[pos]);
}

console.log(findDigit(5673, 4));  // 5
console.log(findDigit(129, 2));   // 2
console.log(findDigit(-2825, 3)); // 8
console.log(findDigit(-456, 4));  // 0
console.log(findDigit(0, 20));    // 0
console.log(findDigit(65, 0));    // -1
console.log(findDigit(24, -8));   // -1