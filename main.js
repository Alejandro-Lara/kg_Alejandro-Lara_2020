var args = process.argv.slice(2);
const numsString = args.join(',');


var resultString = "";
const phoneticKey = {
    '0' : "Zero",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five", 
    '6' : "Six",
    '7' : "Seven",
    '8' : "Eight",
    '9' : "Nine"
};

for(let i = 0; i < numsString.length; i++){
    const digitChar = numsString.charAt(i);
    if(digitChar === ','){
        resultString += ',';
    }
    else if(phoneticKey[digitChar]){
        resultString += phoneticKey[digitChar];
    }
}

console.log(resultString);