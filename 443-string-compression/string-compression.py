class Solution:
    def compress(self, chars: list[str]) -> int:
        put = 0
        take = 0

        while take < len(chars):
            count = 0
            letter = chars[take]
            while take < len(chars) and chars[take] == letter:
                count += 1
                take += 1
            chars[put] = letter
            put += 1
            if count > 1:
                for s in str(count):
                    chars[put] = s
                    put += 1
        return put            