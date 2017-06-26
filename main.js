//Make a page with an image and a button. When you click the button, the image should disappear. HINT: You can use the jQuery function .hide() to hide an element

/*funtion insertName(){
	var name = $('tag you want to function')

	name.function('toggler tag');
}*/
function hideImage(){
	var image = $('img')

	image.hide("#hide");
}
function showImage(){
	var image = $('img')

	image.show("#show");
}
function changeColor(){
	var box = $('#colorBox');

	box.toggleClass('blue');
}
function addBorder(){
	var border = $('#google');

	border.toggleClass('border');
}
/*// Paste the helpful function here:
function addListItem(textInput){
	//list = document.querySelector('ul');
	var list = $('ul');
	//item = document.createElement('li');
	var item = $('<li></li>');
	
	//item.innerText = text;
	item.text(textInput);

	//list.appendChild(item);
	list.append(item);

}*/
// Now use the function to add elements to the list!
function doSomething(){
	//var tbox =
	//	document.getElementById(
	//		'textBox');
	var tbox = $('#textBox');
	//var tboxValue = tbox.value;
	var tboxValue = tbox.val();

	addListItem(tboxValue);
}