# JavaScript 
## `assessment.js`
Contain three functions with respective to assessment in three level of difficulties
- `intro()`
- `intermediate()`
- `difficult()`  

Constructs stave element and quiz context for each assessment 

## `formattime.js`
Trims down utc time precision in elements marked in `trim-time` class

## `note.js`
Contain helper functions constructed from [VexFlow](https://github.com/0xfe/vexflow) library to render music
related content 

## `timer.js`
Functions used to generate random binary choices for timed note/key quiz 

## `validate.js`
Performs clientside validation for 
- `submissionvalidate()` checks for empty or overflow submissions 
- `loginValidate()` checks for empty login fields 
- `registerValidate()` checks for invalid registration fields 
- `checkemail()` check for Regex that matches the following assumption of a valid email  
 
    >  Any number of(digit/alphabet/-/_ /.) follow by @ follow by any number of(alphabet/-) follow by . end with at least 2(alphabet)
