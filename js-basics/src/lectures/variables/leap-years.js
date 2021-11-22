/**
 * Lektion: Abschluss
 * 7kyu | Leap Years
 * https://www.codewars.com/kata/526c7363236867513f0005ca/javascript
 */

function isLeapYear(year) {
    if (year % 400 === 0) return true;
    if (year % 100 === 0) return false;
    if (year % 4 === 0) return true;
    return false;
}

console.log(isLeapYear(1234)); // false
console.log(isLeapYear(1984)); // true
console.log(isLeapYear(2000)); // true
console.log(isLeapYear(2010)); // false
console.log(isLeapYear(2013)); // false