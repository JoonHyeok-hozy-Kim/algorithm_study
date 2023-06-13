import re

def solution():
    N = int(input())
    result_set = set()

    def single_tag_finder(S, depth=0):
        # print('{}Single : {}'.format('  '*depth, S))
        p = re.compile(r'<\s*(\w+)\s*\/>')
        m = p.search(S)
        if m:
            result_set.add(m.group(1))
            s, e = m.start(), m.end()
            if s > 0:
                normal_tag_finder(S[:s], depth+1)
            if e < len(S):
                single_tag_finder(S[e:], depth+1)
        else:
            normal_tag_finder(S, depth+1)


    def normal_tag_finder(S, depth=0):
        # print('{}Normal : {}'.format('  '*depth, S))
        p = re.compile(r'(<\s*(\w+)\s*(\w+\s*=\s*"[^"^\s]+"){0,1}\s*>).*(<\/\s*\2\s*>)')
        m = p.search(S)
        if m:
            result_set.add(m.group(2))
            new_s, new_e = m.start() + len(m.group(1)), m.end() - len(m.group(4))
            normal_tag_finder(S[new_s:new_e], depth+1)
    

    for _ in range(N):
        s = input()
        single_tag_finder(s)
        
    for i, v in enumerate(sorted(result_set)):
        print(v, end="")
        if i < len(result_set)-1:
            print(";", end="")
    print()


def solution2():
    N = int(input())
    result_set = set()

    def single_tag_finder(S, depth=0):
        # print('{}Single : {}'.format('  '*depth, S))
        p = re.compile(r'<\s*(\w+)\s*\/>')
        m = p.search(S)
        if m:
            # result_set.add(m.group(1))
            s, e = m.start(), m.end()
            if s > 0:
                normal_tag_finder(S[:s], depth+1)
            if e < len(S):
                single_tag_finder(S[e:], depth+1)
        else:
            normal_tag_finder(S, depth+1)


if __name__ == '__main__':
    solution()
        
'''
4
<a/><d >asdf< f d="asdf">asdfasdf</f>asdf</d><b/><c/>
<z >asdf< f d="asdf">asdfasdf</f>asdf</z><b/><c/>
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

1
<d >asdf< f d="asdf">asdfasdf</f>asdf</d><b/><c/>
'''