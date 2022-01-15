# 基岩版充值档位
coins_price = {
	320: 12,
	960 + 60: 40,
	1600 + 120: 68,
	3200 + 300: 128,
	8000 + 800: 328,
}

# 自下而上计算
def calc_min_cost(coins_price, n):
	# 初始化 coins 列表
	coins = []
	for i in coins_price.keys():
		coins.append(i)
	
	# result_memo 初始化储存计算结果，小于等于 0 的一律为 0
	# path_memo 储存每个比 n 小的金额的 f() 的解
	result_memo = {}
	choice_memo = {}
	sum_coins = -8800
	while sum_coins <= 0:
		result_memo[sum_coins] = 0
		choice_memo[sum_coins] = []
		sum_coins += 10
	
	# 枚举所有小于 n 的待计算金额，考虑到充值档的精度，步长取 10
	lst = []
	# print("sum_coins: ", sum_coins)
	while sum_coins <= n:
		lst.append(sum_coins)
		sum_coins += 10
		
	# 计算所有比 n 小的金额的 f()
	for i in lst:	
		min_cost = float("inf")
		for j in coins:
			#min_cost = min(min_cost, coins_price[j] + result_memo[i-j])
			cost = coins_price[j] + result_memo[i-j]
			# 迭代更新最小值、解
			if cost < min_cost:
				min_cost = cost
				choice_memo[i] = j
		# 比 n 小的金额，从小到大所有计算结果储存
		result_memo[i] = min_cost		
	# print("lst[-1]: ", lst[-1])
	
	return result_memo[lst[-1]], choice_memo

# 根据充值解的列表，打印充值建议
def print_charge_suggest(choices):
	# 初始化充值组合 dict
	charge_comb = {}
	coins = list(set(choices))
	coins.sort(reverse=True)
	for i in coins:
		charge_comb[i] = 0
	
	# 遍历充值组合计数
	for i in choices:
		charge_comb[i] += 1
	
	# 打印充值组合建议，实际充值金额
	print("充值组合：")
	sum_coins = 0
	for i in charge_comb.keys():
		if charge_comb[i] > 0:
			print("{} 档位 {} 次".format(i, charge_comb[i]))
			sum_coins = sum_coins + i * charge_comb[i]
	print("实际充值 {} 硬币\n".format(sum_coins))	

def main():
	# 目标金额，必需是大于 0、精度为 10 的整数
	target_coins = 17170
	min_cost, choice_memo = calc_min_cost(coins_price, target_coins)
	print("充值 {} 硬币需要至少 {} 元。".format(target_coins, min_cost))
	
	# 基于储存的每一步的解，重构出整体的充值组合
	n = target_coins
	choices = []
	while n > 0:
		choice = choice_memo[n]
		choices.append(choice)
		# print("f({}) 时取 {}".format(n, choice))
		n -= choice

	print_charge_suggest(choices)

if __name__ == "__main__":
	main()
