// my_script.js

function myFunction()
{
	//document.write("Hi");
	var name = document.getElementById("name").value;
	document.getElementById("data").innerHTML = "Hi " + name;
}























// multiple line comment

/*
//EX 5: 1. ask the user for a message
var msg = prompt("Enter a message: ");

//EX 5: 2. print a message in ALL UPPERCASE
var upMsg = msg.toUpperCase();
	document.write(upMsg + "<br");

//EX 5: 3. print a message in all lowercase
var lowMsg = msg.toUpperCase();
	document.write(upMsg + "<br>")

//EX 5 4. replace a word in a message and print
var newMsg = msg.replace ("old", "new");
	document.write(newMsg);
*/

//EX 1: 1. ask user to enter 5 numbers

//EX 1: 2. get a sum of all 5 numbers

//EX 1: 3. print out the sum on the page

//ARRAYS: define array

/*
//EX 4: 1. ask the user for a number, maxValue
var maxValue = prompt("Enter a number");
//EX 4: 2. Loop - print all integers from 1 up to maxValue
for (var i = 1; i <= maxValue; i++)
{
	//document.write(i + " " +Math.pow(i,3) + "<br>");
	document.write(i + " " +calPower(i,3) + "<br>");
}
*/

// 3^4 ==> 3 * 3 * 3 * 3
// 2*5 ==> 2 * 2 * 2 * 2 * 2
/*function calPower (base, power)
{
	var result = 0;
	for(var i = 0; i < power; i++)
	{
		result = result * base 
	}
	return result;
}
*/

/*var scores = [6, 9, 13, 20, 5, 4, 5, 20, 20, 3];
var num = 1;

var sum = 0;

for (var index = 0; index < scores.length; index++)
{
	sum += scores[index];
}
*/

/*
var index = 0;

while (index < scores.length){
	sum = sum + scores[index];
	index = index + 1;
}
*/

//ARRAY: get sum of all numbers in array

/*
var name = prompt("Please enter your name: ");

//EX 2: school you are going to
var school = prompt("Please enter your school");

//EX 2: hometown
var hometown = prompt("Please enter your hometown");

//EX 3: 1. enter score
var score = prompt("Enter your Score:")


var a = prompt("Please enter your first number:")

var b = prompt("Please enter your second number:")

var c = prompt("Please enter your third number:")

var d = prompt("Please enter your fourth number:")

var e = prompt("Please enter your fifth number:")

var sum = 1 * (a) + 1 * (b) + 1 * (c) + 1 * (d) + 1 * (e)
*/

/*
document.write("Hi, " + name + ".<br>You are going to " + school + " and you are from " + hometown + ".");

//EX 3: 2. based on the score, print out message
if (score < 150) {
	document.write("<br>Your score is pretty bad.");
}
else if(score < 250){
 	document.write("<br>Your score is decent.");
}
else if(score < 350){
 	document.write("<br>Your score is good!");
}
else if(score < 450){
 	document.write("<br>Your score is great!");
}
else{
 	document.write("<br>Your score is awesome!");
}
//EX 3: print out
document.write("<br>The sum of your five chosen numbers is " + sum + ".<br>");
*/

//ARRAY: get sum of all numbers in array
/*document.write(sum)*/