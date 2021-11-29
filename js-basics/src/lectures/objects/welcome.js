/** 
 * Lektion 4 - Objekte:
 * 8kyu | Welcome! 
 * https://www.codewars.com/kata/577ff15ad648a14b780000e7/javascript
 */

function greet(language) {
    let languages = {
        english: 'Welcome',
        czech: 'Vitejte',
        danish: 'Velkomst',
        dutch: 'Welkom',
        estonian: 'Tere tulemast',
        finnish: 'Tervetuloa',
        flemish: 'Welgekomen',
        french: 'Bienvenue',
        german: 'Willkommen',
        irish: 'Failte',
        italian: 'Benvenuto',
        latvian: 'Gaidits',
        lithuanian: 'Laukiamas',
        polish: 'Witamy',
        spanish: 'Bienvenido',
        swedish: 'Valkommen',
        welsh: 'Croeso'
    };
    return language in languages
        ? languages[language]
        : languages.english;
}

console.log('actual: ' + greet('english'), 'expected: ' + 'Welcome');
console.log('actual: ' + greet('dutch'), 'expected: ' + 'Welkom');
console.log('actual: ' + greet('IP_ADDRESS_INVALID'), 'expected: ' + 'Welcome');