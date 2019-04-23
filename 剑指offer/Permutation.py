'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

def Permutation(ss):

    if len(ss) == 0:
        return []
    if len(ss) == 1:
        return [ss]
    res = set()
    # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...全部取到，然后递归求解
    for i in range(len(ss)):
        # 依次固定了元素，然后递归求解
        for j in Permutation(ss[:i] + ss[i + 1:]):
            # set集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同情况）
            res.add(ss[i] + j)
    return sorted(res)




# test
strs = "abc"
print(Permutation(strs))