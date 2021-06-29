from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']

        subsets = self.generateParenthesis(n - 1)
        newSubsets = set()
        for subset in subsets:
            possPos = len(subset)
            for i in range(possPos):
                newSubsets.add(subset[:i] + '()' + subset[i:])

        return list(newSubsets)


test = Solution()
print(test.generateParenthesis(3))

# use a set to take care of duplicates?
# GP(1) = [ '()' ]
# GP(2) =

# https://leetcode.com/problems/unique-binary-search-trees


class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        return self.numTreesHelper(n, memo)

    def numTreesHelper(self, n, memo):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return 1
        count = 0

        for i in range(1, n+1):
            left = self.numTreesHelper(i - 1, memo)
            right = self.numTreesHelper(n - i, memo)
            count += left * right

        memo[n] = count
        return memo[n]

# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest
