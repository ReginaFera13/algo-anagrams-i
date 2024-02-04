exports.isCharacterMatch = function(string1, string2) {

};

exports.anagramsFor = function(word, listOfWords) {

};

function isCharacterMatch(string1, string2) {
    const arr1 = string1.replace(/\s/g,'').split("");
    const arr2 = string2.replace(/\s/g,'').split("");

    if (arr1.length !== arr2.length) {
        return false;
    } else {
        charsFound = 0;
        for (let i = 0; i < arr1.length; i++) {
            let char = arr1[i];
            if (arr2.indexOf(char.toLowerCase()) >= 0 || arr2.indexOf(char.toUpperCase() >= 0)) {
                charsFound++;
            }
        }

        if (charsFound === arr1.length) {
            return true;
        } else {
            return false;
        }
    }
}

listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];
function anagramsFor(word, listOfWords) {
    let anagrams = [];
    for (let i = 0; i < listOfWords.length; i++) {
        let curr = listOfWords[i]
        if (isCharacterMatch(word, curr) === true) {
            anagrams.push(curr)
        }
    }
    return anagrams
}

console.log(anagramsFor("threads", listOfWords))