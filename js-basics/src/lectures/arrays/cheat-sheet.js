/**
 * Spickzettel fuer Hinzufuegen/Entfernen von Array-Elementen
 */

const numbers = [3];

/** Hinzufuegen... */

const length = numbers.unshift(0);        // ...am Anfang -> [0, 3]
const empty = numbers.splice(1, 0, 1, 2); // ...in Mitte  -> [0, 1, 2, 3]
const length2 = numbers.push(4, 5);       // ...am Ende   -> [0, 1, 2, 3, 4, 5]

console.log(numbers);
console.log({ length, empty, length2 });

/** Entfernen... */

const first = numbers.shift();            // ...am Anfang -> [1, 2, 3, 4, 5]
const deleted = numbers.splice(1, 2);     // ...in Mitte  -> [1, 4, 5]
const last = numbers.pop();               // ...am Ende   -> [1, 4]

console.log(numbers);
console.log({ first, deleted, last });

/**
 * Hinweis:
 * Denken Sie daran, dass Sie zur Ausfuehrung Ihrer js-Datei eine Engine benoetigen, entweder:
 *
 *      a) via Browser:
 *
 *         js-File via script-Element am Ende vom body-Element in Ihrer html-Datei einbinden
 *         <body>
 *             ...
 *             <script src="cheat-sheet.js"></script>
 *         </body>
 *
 *      b) via Node:
 *
 *         ggf. Node installieren (siehe https://nodejs.org/de/download/)
 *         ausfuehren in Konsole mit: node .\cheat-sheet.js
 */

