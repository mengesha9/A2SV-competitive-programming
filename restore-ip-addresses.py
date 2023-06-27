class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []

        def back(ip, string, parts):
            if parts == 4:
                if not string:
                    result.append(ip)
                return

            for i in range(1, min(4, len(string) + 1)):
                if i > 1 and string[0] == '0':  
                    continue
                part = string[:i]
                if int(part) <= 255:
                    back(ip + part + ('.' if parts < 3 else ''), string[i:], parts + 1)

        back('', s, 0)
        return result