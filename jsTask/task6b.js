//Print out Equilateral triangle for equal sides, Isosceles triangle for two equal sides,Scalene triangle for none equal sides

const side1 = 7
const side2 = 7
const side3 = 6

if(side1===side2 && side2===side3 && side3===side1) {
    console.log('Equilateral triangle')
} else if(side1===side2 || side2===side3 || side1===side3){
    console.log('Isosceles triangle')
} else {
    console.log('Scalene triangle')
}