class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = []
        for w in strs:
            result.append('#{}#{}'.format(len(w), w))
            # print(result)
        return ''.join(result)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        idx = 0
        diff = 0
        result = []
        while idx < len(s):
            if s[idx] == '#':
                diff += 1
                if diff % 2 == 1:
                    idx += 1
                    num = 0
                else:
                    idx += 1
                    result.append(s[idx:idx+num])
                    idx += num
            else:
                num *= 10
                num += int(s[idx])
                idx += 1
            # print('idx : {}, diff : {}, num : {}, result : {}'.format(idx, diff, num, result))
        
        return result

            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))