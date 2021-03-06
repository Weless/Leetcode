package main

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	dp[0] = 0
	for i := 1; i < amount+1; i++ {
		dp[i] = amount + 1
	}
	for i := 1; i < amount+1; i++ {
		for _, coin := range coins {
			if i-coin < 0 {
				continue
			}
			dp[i] = min(dp[i], 1+dp[i-coin])
		}
	}
	if dp[amount] == amount+1 {
		return -1
	} else {
		return dp[amount]
	}
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
