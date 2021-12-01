/**
 * Arrays Exercise 4
 * 
 * Implementieren Sie die Funktion move() so, dass das Array-Element an Position 'index' um 'offset' Stellen nach 
 * rechts verschoben wird. Falls 'offset' negativ ist, wird das Element entsprechend nach links verschoben.
 * Überprüfen Sie, ob die neue Position im Array enthalten ist. Wenn nicht, geben Sie einen Fehler auf der Konsole aus: 
 *      -> console.error("Invalid offset.")
 * 
 * Tipp: Fürs Kopieren des Arrays kann der Spread-Operator verwendet werden: 
 *      -> const output = [...array];
 *      -> siehe https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Spread_operator
 * 
 * Benutzen Sie diese Tests zur Kontrolle:
 * 
 * Test 1: move([1, 2, 3, 4], 1, -1); // -> [2, 1, 3, 4]
 * Test 2: move([1, 2, 3, 4], 1, -2); // -> Invalid offset.
 */

const output = move([1, 2, 3, 4], 1, -2);

console.log(output);

function move(array, index, offset) {
    // TODO
    return [];
}