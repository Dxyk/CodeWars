/* https://www.codewars.com/kata/sum-the-tree/c */


struct node {
	int value;
	struct node *left;
	struct node *right;
};


int sumTheTreeValues(struct node *root) {
	int sum = 0;
	if (!root) {
		return 0;
	}

	sum += root->value;
	sum += sumTheTreeValues(root->left);
	sum += sumTheTreeValues(root->right);


	return sum;
}
