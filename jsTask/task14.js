const books =[
  {
    title: 'Let it Shine',
    description: 'Motivational',
    numberOfPages: 85,
    author: 'Roli Mary',
    reading:true
  },
  {
    title: 'Macro Economics',
    description: 'Educational',
    numberOfPages: 90,
    author: 'Omajemite',
    reading:true
  },
  {
    title: 'Agricultural Science',
    description: 'Plant Biology',
    numberOfPages: 120,
    author: 'Sire Tunde',
    reading:false
  },
  {
    title: 'Restoration',
    description: 'Motivational',
    numberOfPages: 135,
    author: 'Grace Geegbi',
    reading:true
  }
];

// print out the books where the reading status is true to the console
for (let i = 0; i < books.length; i++) {
  if(books[i].reading === true){
    console.log(books[i])
  }
  
}
