# Which Regular Expression will we need to pass the last test case?
Regular expressions are patterns used to match character combinations in strings.

When the search for a match requires something more than a direct match, the pattern includes special characters.

```
To pass the last test case, we can use two Regular Expressions:

/[^A-Za-z0–9]/g  or

/[\W_]/g
```
## __\W__ removes all __non-alphanumeric characters:__

- \W matches any non-word character
- \W is equivalent to [^A-Za-z0–9_]
- \W matches anything that is not enclosed in the brackets

## What does that mean?
```

[^A-Z] matches anything that is not enclosed between A and Z

[^a-z] matches anything that is not enclosed between a and z

[^0-9] matches anything that is not enclosed between 0 and 9

[^_] matches anything that does not enclose _
```

But in our test case, we need palindrome(“0_0 (: /-\ :) 0–0”) to return true, which means “_(: /-\ :)–” has to be matched.

We will need to add “_” to pass this specific test case.

```
We now have “\W_”
```
We will also need to add the __g__ flag for global search.

```
We finally have “/[\W_]/g”
```
/[\W_]/g was used for pure demonstrative purpose to show how RegExp works. /[^A-Za-z0–9]/g is the easiest RegExp to choose.

## Resources

[Regular Expressions — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Regular_Expressions)

[toLowerCase() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)

[replace() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

[split() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)

[reverse() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)

[join() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)

[String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)

[for Loop — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)