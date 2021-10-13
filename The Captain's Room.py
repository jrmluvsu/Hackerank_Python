k, nums = int(input()),list(map(int, input().split()))
u_num = set(nums)
print(((sum(u_num)*k)-(sum(nums)))//(k-1))