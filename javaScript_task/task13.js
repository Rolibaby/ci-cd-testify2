// My Personal Library2  >>> ToggleReadingStatus
const book = {
    title: 'Let it Shine',
    description: 'Motivational',
    numberOfPages: 85,
    author: 'Roli Mary',
    reading:true,
    toggleReadingStatus: function () {
        if(book.reading===false){
            book.reading = true
        } else {
            book.reading = false
        }
        
    }
   
    }
    book.toggleReadingStatus()
console.log(book.reading)
