/*
Evaluates the prefix expression and calculates the result for the given
variable values.

@param {String} expression - the prefix expression to evaluate.
@param {Object} variables - all the variables in the expression are the keys of
    this object and their corresponding values are the values the variable
    should take
@returns {Number|null} the numerical result of the expression evaluated with the
    given variable values. If the expression is invalid, it will return `null`.
*/
function calcOperator(op, op1, op2) {
    if(!op || !op1 || !op2) return null;

    switch(op) {
        case "+":
            return parseInt(op1) + parseInt(op2);
        case "-":
            return parseInt(op1) - parseInt(op2);
        case "*":
            return parseInt(op1) * parseInt(op2);
        case "/":
            return parseInt(parseInt(op1) / parseInt(op2));
        default:
            return null;
    }
}

function result_expression(expression, variables) {
    //Enter your code here
    const stack = [];
    const operators = {"+": "+", "-": "-", "*": "*", "/": "/" };
	
    let prevSpace = true;
    for(let i = expression.length - 1; i >= 0; i--) {
        let symb = expression[i];

        if(symb == " ") {
		prevSpace = true;
		continue;
	}
	
	if(!prevSpace) return null;

	prevSpace = false;

        if(symb in variables) {
            symb = variables[symb];
        }

        if(symb in operators) {
            const op = operators[symb];
            if(op == null) {
                return null;
            }
            const res = calcOperator(op, stack.pop(), stack.pop());

	    if(res == null) return null;

            stack.push(res);
        } else {
            stack.push(symb);
        }
    }
	
    if(stack.length != 1) return null;

    return stack[0];
}
