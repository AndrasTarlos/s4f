/**
 * Lektion 4 - Objekte:
 * 7kyu | Ironman Triathlon
 * https://www.codewars.com/kata/57d001b405c186ccb6000304/javascript
 */

function iTri(dist) {
    //its gonna be a long day!
    const totalDist = 2.4 + 112 + 26.2;
    const toGo = (totalDist - dist).toFixed(2) + ' to go!';
    if (dist === 0) return 'Starting Line... Good Luck!';
    if (dist < 2.4) return { 'Swim': toGo };
    if (dist < 2.4 + 112) return { 'Bike': toGo };
    if (dist < totalDist - 10) return { 'Run': toGo };
    if (dist < totalDist) return { 'Run': 'Nearly there!' };
    return "You're done! Stop running!";
}

console.log('actual: ' + JSON.stringify(iTri(36)), 'expected: ' + JSON.stringify({ 'Bike': '104.60 to go!' }));
console.log('actual: ' + JSON.stringify(iTri(103.5)), 'expected: ' + JSON.stringify({ 'Bike': '37.10 to go!' }));
console.log('actual: ' + JSON.stringify(iTri(0)), 'expected: ' + JSON.stringify('Starting Line... Good Luck!'));
console.log('actual: ' + JSON.stringify(iTri(2)), 'expected: ' + JSON.stringify({ 'Swim': '138.60 to go!' }));