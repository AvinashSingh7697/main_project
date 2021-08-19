
// const name = document.getElementById("name")
// const password = document.getElementById("password")
// const form = document.getElementById("form")

// form.addEventListener("submit")
// let message = []
// if (name.value=="" || name.value==null) 
// {message.push("name is reqired")}

// function greet(name, thank){ 
//   let msg= (`gdhdh ${name} cs `);
//     return msg;c
// }
// let name = `skillf`;

// let name1 = "kay";

// let val= greet(name);
// console.log(val)


// console.log("shiv")
// let a = document;
// a= document.all;

// console.log(a);


// console.log("hdsb");
// console.log("hdsb");







// alert("hi")
// a.prompt("write ur msg")
// a = window.innerWidth;
// a = window.innerHeight;


console.log('Events')


document.getElementById('heading').addEventListener('click',function(e){
    let variable;
    console.log('u hv clicke heading')

    variable = e.target;
    variable = e.target.classname;
    variable = Array.from(e.target.classlist);
    variable = e.target.id;
    console.log(variable)

});