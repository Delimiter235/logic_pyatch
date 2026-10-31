class Solution: 
    def longest_common_prefix_matrix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # 1. 拿第一个字符串当做“标尺”
        base_str = strs[0]
        
        # 2. 外层循环：遍历标尺的每一个字符（列扫描）
        # 索引 i 代表：当前检查的是第几列
        for i in range(len(base_str)):
            char_to_check = base_str[i]
            
            # 3. 内层循环：遍历剩下的每一个字符串（行扫描）
            # 索引 j 代表：当前检查的是第几行
            for j in range(1, len(strs)):
                
                current_str = strs[j]
                
                # 【关键点】这里有两个“失败条件”，只要满足一个就说明前缀断了
                # 条件 A：当前字符串太短了，根本没有第 i 位（防越界）
                # 条件 B：当前字符串的第 i 位和标尺不一样class Solution:

                if len(current_str) == i or current_str[i] != char_to_check:
                    return base_str[:i]
                
                pass

        return base_str
