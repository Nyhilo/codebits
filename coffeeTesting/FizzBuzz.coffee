# FizzBuzz.coffee

fizzbuzz = (i) ->
	output = ""
	if i % 3 is 0 then output += "fizz"
	if i % 5 is 0 then output += "buzz"
	if i % 3 isnt 0 and i % 5 isnt 0 then output = i
	i + ": " + output

console.log fizzbuzz num for num in [1..20]
