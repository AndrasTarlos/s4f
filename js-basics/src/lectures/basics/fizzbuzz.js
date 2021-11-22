/**
 * Lektion 3 - Kontrollfluss:
 * 7kyu | Fizz Buzz
 * https://www.codewars.com/kata/5300901726d12b80e8000498/javascript
 */

function fizzbuzz(n) {
    var arr = [];
    for (let i = 1; i <= n; i++) {
        let fizz = i % 3 == 0;
        let buzz = i % 5 == 0;
        arr.push(fizz ? buzz ? "FizzBuzz" : "Fizz" : buzz ? "Buzz" : i);
    }
    return arr;
}

console.log(fizzbuzz(20));
