# 是否启用禁用列表
enable = True

# 禁用规则（黑名单）
# person为个人，其中的QQ号会被禁止与机器人进行私聊或群聊交互
# 示例: person = [2854196310, 1234567890, 9876543210]
# group为群组，其中的群号会被禁止与机器人进行交互
# 示例: group = [123456789, 987654321, 1234567890]
#
# 支持正则表达式，字符串都将被识别为正则表达式，例如：
# person = [12345678, 87654321, "2854.*"]
# group = [123456789, 987654321, "1234.*"]
# 若要排除某个QQ号或群号（即允许使用），可以在前面加上"!"，例如：
# person = ["!1234567890"]
# group = ["!987654321"]
# 排除规则优先级高于包含规则，即如果同时存在包含规则和排除规则，排除规则将生效，例如：
# person = ["1234.*", "!1234567890"]
# 那么1234567890将不会被禁用，而其他以1234开头的QQ号都会被禁用
person = [2854196310]  # 2854196310是Q群管家机器人的QQ号，默认屏蔽以免出现循环
group = [204785790, 691226829]  # 本项目交流群的群号，默认屏蔽，避免在交流群测试机器人
