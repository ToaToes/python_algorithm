'''
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址

IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。
同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。

ip地址的类型，可能为
IPv4,   IPv6,   Neither

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
#
class Solution:

    def solve(self , IP: str) -> str:
      # check if its hexdecimal
      def is_hexdecimal(s):
        try:
          int(s, 16)
          return True
        except ValueError:
          return False
      
      # check if its IPv4
      def validIPv4(ip):
        for i in ip:
          if i == '': # if its Empty -> 10.2..4 
            return "Neither"
          elif not i.isdigital(): # if its not number -> 1g2.5.6.4
            return "Neither"
          elif int(i) > 255: # if it exceeds -> 256.345.12.4
            return "Neither"
          elif len(i) > 1 and i[0] = '0': # if starts with 0 -> 12.03.1.2
            return "Neither"
        return True

      # check if its IPv6
      def validIPv6(ip):
        for i in ip:
          if i == '': # if Empty
            return "Neither"
          elif not s_hexdecimal(i): # if not hexdecimal
            return "Neither"
          elif i.isdigital() and len(i) > 1 and int(i) == 0: # if not valid -> contains '0000', and also it has to be a Number at least
            return "Neither"
        return True

      check = "Neither"
      
      # check '.' and ':' to find if its IPv4 or IPv6
      for i in IP:
        if i == '.':
          check = validIPv4(IP)
          break
        elif i == ':':
          check = validIPv6(IP)
          break

      return check
