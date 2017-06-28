function answerQuestion(){
	var answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

	var textBox = $("#ask");
	var result = textBox.val();
	var notaQuest = result.indexOf("?");

	textBox.val("");

	if(notaQuest == -1){
		alert("Unable to answer the question, please try again.");
	} else{
		alert(answers[Math.floor(Math.random()*20)]);
	}
}