class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen, result = {}, []

        for s in strs:
            s_srt = ''.join(sorted(s))

            if s_srt in seen:
                result[seen[s_srt]].append(s)
            else:
                result.append([s])
                seen[s_srt] = len(result) - 1

        return result        