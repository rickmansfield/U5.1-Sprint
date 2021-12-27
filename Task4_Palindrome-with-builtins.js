// write a function that checks if a string is palindrome using builtin methods
/*
The toLowerCase() method to return the calling string value converted to lowercase.

The replace() method to return a new string with some or all matches of a pattern replaced by a replacement. We will use one of the RegExp.

The split() method splits a String object into an array of strings by separating the string into sub strings.

The reverse() method reverses an array in place. The first array element becomes the last and the last becomes the first.

The join() method joins all elements of an array into a string.
*/

function palindrome(str) {
    // Step 1. Lowercase the string and use the RegExp to remove unwanted characters from it
    var re = /[\W_]/g; // or var re = /[^A-Za-z0-9]/g;

    var lowRegStr = str.toLowerCase().replace(re, '');
    // str.toLowerCase() = "A man, a plan, a canal. Panama".toLowerCase() = "a man, a plan, a canal. panama"
    // str.replace(/[\W_]/g, '') = "a man, a plan, a canal. panama".replace(/[\W_]/g, '') = "amanaplanacanalpanama"
    // var lowRegStr = "amanaplanacanalpanama";

    // Step 2. Use the same chaining methods with built-in functions from the previous article 'Three Ways to Reverse a String in JavaScript'
    var reverseStr = lowRegStr.split('').reverse().join('');
    // lowRegStr.split('') = "amanaplanacanalpanama".split('') = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
    // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].reverse() = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
    // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].join('') = "amanaplanacanalpanama"
    // So, "amanaplanacanalpanama".split('').reverse().join('') = "amanaplanacanalpanama";
    // And, var reverseStr = "amanaplanacanalpanama";

    // Step 3. Check if reverseStr is strictly equals to lowRegStr and return a Boolean
    return reverseStr === lowRegStr; // "amanaplanacanalpanama" === "amanaplanacanalpanama"? => true
}

// WITHOUT COMMENTS --------------------------
function palindrome(str) {
    var re = /[\W_]/g;
    var lowRegStr = str.toLowerCase().replace(re, '');
    var reverseStr = lowRegStr.split('').reverse().join('');
    return reverseStr === lowRegStr;
}

console.log(palindrome('eye'));
console.log(palindrome('me'));
console.log(palindrome('race car')) // should return true
console.log(palindrome('not a palindrome')) // should return false
console.log(palindrome('A man, a plan, a canal. Panama')) // should return true
console.log(palindrome('never odd or even')) // should return true
console.log(palindrome('nope')) // should return false
console.log(palindrome('almostomla')) // should return false
console.log(palindrome('My age is 0, 0 si ega ym.')) // should return true
console.log(palindrome('1 eye for of 1 eye.')) // should return false
console.log(palindrome('0_0 (: /-\ :) 0–0')) // should return true