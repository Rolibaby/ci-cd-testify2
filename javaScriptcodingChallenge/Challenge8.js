//Return a Boolean if a number is divisible by 10

let number = 70
function divisibleByTen(number){ //Declaring the function
    if(number % 10 === 0){
        return true
    } else{
        return false
    }
}
console.log(divisibleByTen(number))//calling the function