/*function changeBorder() {
	var poster = $('#poster');
	poster.toggleClass('border');
}*/

/*function changeImage() {
	var poster = $('#poster');
	poster.attr('src', 'http://esportsjunkie.com/wp-content/uploads/2017/06/Yahoo.jpg');
}*/

/*function changeLink(){
	var link = $('a');
	if (link.text() == "Yahoo") {
		link.attr('href', 'http://www.google.com');
		link.text('Google')
		poster.attr('src','http://www.sitepronews.com/wp-content/uploads/2016/07/Google.png')
	} else{
		link.text('Yahoo');
		link.attr('href', 'https://www.yahoo.com/');
		poster.attr('src', 'http://esportsjunkie.com/wp-content/uploads/2017/06/Yahoo.jpg')
	}
}*/

/*function changeImage() {
	var poster = $('#poster')

	if (poster.attr('src') == "http://www.sitepronews.com/wp-content/uploads/2016/07/Google.png"){
		poster.attr('src','https://cdn.pixabay.com/photo/2013/01/29/22/53/yahoo-76684_960_720.png')
	} else{
		poster.attr('src', 'http://www.sitepronews.com/wp-content/uploads/2016/07/Google.png')
	}
}*/
function changeImage(){
	var image = $('#ImageList');
	var poster = $('#poster');
	if (image.val() == 'Google'){
		poster.attr('src', 'google.png');
	}
	else if (image.val() == 'Yahoo') {
		poster.attr('src','yahoo.jpg');
	}
	else if (image.val() == 'Bing'){
		poster.attr('src','bing.png')
	}
}
function popup(){
	alert('jam!');
}
function setupEverything() {
	var poster = $('#poster');
	poster.toggleClass('border');

	poster.on('click', popup);
	var image = $('#ImageList')
	image.on("change", changeImage);
}
$(document).ready(setupEverything);