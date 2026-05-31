class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        path_sections = path.split("/")
        for section in path_sections:
            if section == "." or section == "":
                continue
            elif section == "..":
                # remove until last "/" if exists
                if res == "":
                    continue
                res = "/".join(res.split("/")[:-1])
            else:
                res += "/" + section
        
        if res == "":
            res = "/"
        return res