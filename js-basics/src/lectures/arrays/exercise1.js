/**
 * Arrays Exercise 1
 * 
 * Implementieren Sie die Funktion arrayFromRange(), um damit ein Array mit allen Elementen von 'min' bis und mit 'max' zu erstellen.
 * Verwenden Sie Array.push() und benutzen Sie die nachfolgenden Tests zur Kontrolle.
 * 
 * Test 1: arrayFromRange(-1, 4); // -> [-1, 0, 1, 2, 3, 4]
 * Test 2: arrayFromRange(1, -4); // -> []
 */

const numbers = arrayFromRange(-1, 4);

console.log(numbers);

function arrayFromRange(min, max) {
    const arr = [];
    for (let i = min; i <= max; i++)
        arr.push(i);
    return arr;
}