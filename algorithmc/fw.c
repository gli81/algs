// -*- coding: utf-8 -*-

/*
* implementation of Floyd Warshall algorithm in C
* 
* @author: Gavin Li
* @email: liguangzheng998@hotmail.com
* @created: 08222024
*/

#include <stdio.h>
#include <limits.h>

/**
* 
* 
* Params
* ----------
* 	adjMat
*/
int fw_recur_helper_2(
	int const* const* const adjMat,
	int n,
	int i,
	int j,
	int k
) {
	if (k < 0) {
		return adjMat[i][k];
	}
	// recursive calls
	int use_it = fw_recur_helper_2(
		adjMat, n, i, k, k - 1
	) + fw_recur_helper_2(
		adjMat, n, k, j, k - 1
	);
	// lost it
	int lose_it = fw_recur_helper_2(
		adjMat, n, i, j, k - 1
	);
	return use_it > lose_it ? lose_it : use_it;
}

/**
* floyd warshall with recursion
* 
* Params
* ----------
*
*/
int** fw_recur(
	int const* const* const adjMat,
	int n,
	int use_list
) {
	int ans[n][n];
	for (size_t i = 0; i < n; ++i) {
		for (size_t j = 0; j < n; ++j) {
			if (use_list) {
				printf("Not Implemented\n");
			} else {
				ans[i][j] = fw_recur_helper_2(
					adjMat, n, i, j, n - 1
				);
			}
		}
	}
	return ans;
}


int main() {
	int test_case_1[][3] = {
		{0, 2, -1},
		{3, 0, INT_MAX},
		{4, 2, 0}
	};
	int const* const* const tc1p = test_case_1;
	int** recur_1 = fw_recur(
		tc1p, 3, 0
	);
	for (size_t i = 0; i < 3; ++i) {
		for (size_t j = 0; j < 3; ++j) {
			printf("%d", recur_1[i][j]);
			if (j != 2) printf("\t\t");
		}
		printf("\n");
	}
}
