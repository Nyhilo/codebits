// FizzBuzz.js

var fizzbuzz = function(limit) {
	var output = "";
	for (var i = 1; i <= limit; i++) {
		if (i % 3 == 0)
			output += "fizz";
		
		if (i % 5 == 0)
			output += "buzz";

		if (i % 3 != 0 && i % 5 != 0)
			output = i;

		console.log(output)
		output = "";
	}
}

fizzbuzz(20)