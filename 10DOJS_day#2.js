'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    const ch = s.charAt(0)
    const vowels = new Set(['a','e','i','o','u']);
    const cons1 = new Set(['b','c','d','f','g']);
    const cons2 = new Set(['h','j','k','l','m']);
    if(vowels.has(ch)){
        letter = 'A';
    }
    else if(cons1.has(ch)){
        letter = 'B';
    }
    else if(cons2.has(ch)){
        letter = 'C';
    }
    else{
        letter = 'D';
    }
    return letter;
}


function main() {
    const s = readLine();

    console.log(getLetter(s));
}
