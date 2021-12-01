/**
 * Arrays Exercise 2
 * 
 * Implementieren Sie die Funktion includes() zur Überprüfung, ob ein bestimmtes Element 'searchElement' im Array enthalten ist.
 * Verwenden Sie dazu einen Loop. 
 * 
 * Tipp: Beachten Sie den Unterschied for/in vs. for/of: 
 *      -> Zur Erinnerung: Ein Property eines JS Objects besteht aus name:value.
 *                         Ein Element in einem JS Array besteht aus index:value.
 *         for/in - iteriert über die Property-Namen (resp. liefert den Index bei einem JS Array)
 *         for/of - iteriert über die Werte
 *      -> siehe https://www.w3schools.com/js/js_loop_forin.asp
 *               https://www.w3schools.com/js/js_loop_forof.asp
 * 
 * Benutzen Sie die nachfolgenden Tests zur Kontrolle.
 * 
 * Test 1: includes([1, 2, 3, 4], 3); // -> true
 * Test 2: includes([1, 2, 3, 4], 5); // -> false
 */

const output = includes([1, 2, 3, 4], 3);

console.log(output);

function includes(array, searchElement) {
    // TODO
    return false;
}