/** 
 * Lektion 4 - Objekte:
 * 7kyu | Scrabblemania
 * https://www.codewars.com/kata/5b68983a975680155000005d/javascript
 */

function wordscore(word) {
    const scores = {
        a: 1, b: 3, c: 3, d: 2, e: 1, f: 4, g: 2, h: 4, i: 1,
        j: 8, k: 5, l: 1, m: 3, n: 1, o: 1, p: 3, q: 10, r: 1,
        s: 1, t: 1, u: 1, v: 4, w: 4, x: 8, y: 4, z: 10
    };
    const bonus = word.length === 7 ? 50 : 0;
    let sum = 0;
    // for (let i = 0; i < word.length; i++) {
    //     let letter = word[i];
    //     sum += scores[letter];
    // }
    for (let letter of word) {
        sum += scores[letter];
    }
    // word.split('').forEach(letter => {
    //     sum += scores[letter]
    // });
    return sum * word.length + bonus;
}

console.log('actual: ' + wordscore('great'), 'expected: ' + 30);
console.log('actual: ' + wordscore('deceive'), 'expected: ' + 141);
console.log('actual: ' + wordscore('melon'), 'expected: ' + 35);