/* https://www.codewars.com/kata/reducing-by-rules-to-get-the-result/c */

typedef double (*rulesFnct)(double, double);

double reduceByRules(double numbers[], int numberCount, rulesFnct rules[],
					 int rulesCount) {
	int index = 1;
	int rule_index = 0;
	double result = numbers[0];
	while (index < numberCount) {
		result = rules[rule_index](result, numbers[index]);
		// if (rule_index == rulesCount - 1) {
		// 	rule_index = 0;
		// } else {
		// 	rule_index++;
		// }
		rule_index = (rule_index + 1) % rulesCount;
		index++;
	}
	return result;
}
