/**
 * Lektion 3 - Kontrollfluss:
 * 6kyu | Split Strings
 * https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/javascript
 */

function solution(str) {
    if (!str || str == "")
        return [];
    str = str.length % 2 == 1 ? str += "_" : str;
    result = [];
    for (let i = 0; i < str.length; i += 2) {
        //result.push(str.slice(i, i + 2));
        let start = i; let stop = start + 2;
        result.push(str.substring(start, stop));
    }
    return result;
}

console.log(solution("abcdef"));  // ["ab", "cd", "ef"]
console.log(solution("abcdefg")); // ["ab", "cd", "ef", "g_"]
console.log(solution(""));        // []
console.log(solution());          // []
