import requests, bs4, re, sys, os, textwrap

if len(sys.argv) == 2:
    link = sys.argv[1]
else:
    link = input('Please enter homework page URL: ')

print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True, file=sys.stderr)


# monkey patch to disable buffering


def is_ipython(line):
    return re.search(r'(?:In ?\[\d{1,}\]|Out ?\[\d{1,}\])', line, re.I|re.M) is not None


def remove_comments(line):
    return re.sub(r'\s*# .+$', '', line)


def extract_code(line):
    type = re.search(r'In|Out', line, re.I).group(0)
    return re.sub(r'(In|Out)\s*\[\d{1,}\]:\s*', '', line), type


print('Sending HTTP request...')
content = requests.get(link).text
print('Parsing response HTML...')
soup = bs4.BeautifulSoup(content, 'html.parser')

code_blocks = list(map(lambda c: c.text.strip(), soup.find_all('code')))
file_name = next(filter(lambda s: re.fullmatch(r'^hw\d{1,}pr\d{1,}\.py$', s) is not None, code_blocks))

print('Parsing expected input/output for homework %s problem %s...' % tuple(re.findall(r'\d{1,}', file_name)))

subproblems = [['']]
for i, block in enumerate(soup.find('div', {'class': 'main'})):
    if block.name == 'h4' or block.name == 'h3':
        if len(subproblems[-1]) == 1:
            subproblems.pop()
        try:
            subproblems.append([block.text or block.tt.text.strip()])
        except AttributeError:
            subproblems.append([''])
    if block.name == 'pre':
        pre_text = block.text.strip()
        if not pre_text:
            print(block)
            try:
                pre_text = block.code.text.strip()
            except TypeError:
                pre_text = ''
        subproblems[-1].append(pre_text)
    elif block.name == 'code':
        pre_text = block.text.strip()
        if not pre_text:
            try:
                pre_text = block.pre.text.strip()
            except TypeError:
                pre_text = ''
        subproblems[-1].append(pre_text)

if len(subproblems[-1]) == 1:
    subproblems.pop()

out_content = \
    f"""
import unittest, sys, os
sys.path.append(os.path.abspath(os.getcwd()))

try:
    from {file_name[:-3]} import *
except ImportError:
    print("Unable to find {file_name}. Please make sure it is either in the current working directory"
          "or is in the same directory as this script.", file=sys.stdout, flush=True)
    sys.exit(1)
"""

for i, subproblem in enumerate(subproblems):
    block_out = ''
    pre_blocks = subproblem[1:]
    if not subproblem[0].strip():
        subproblem[0] = f'p{i}'
    print("\nParsing test cases for " + subproblem[0])
    for j, pre in enumerate(pre_blocks):
        stack = []
        counter = 0
        pre_out = ''
        if is_ipython(pre):
            for line in pre.splitlines():
                if is_ipython(line):
                    code, type = extract_code(remove_comments(line))
                    if type == 'In':
                        print(f'Test case {counter} expected input: ' + code)
                        stack.append(code)
                    else:
                        print(f'Test case {counter} expected output: ' + code + '\n')
                        
                        tmp = []
                        tmp.append(f'self.assertEqual({stack.pop()}, {code})')
                        tmp.extend(stack)
                        assertion = '\n'.join(tmp[::-1])
                        
                        pre_out += assertion + '\n'
                        counter += 1
                        stack = []
                else:
                    pre_out+=line+'\n'
            
            if pre_out:
                block_out += f'    def test_test{j}(self):\n'
                block_out += ' ' * 8 + 'try:\n'
                block_out += textwrap.indent(pre_out, ' ' * 12)
                block_out += ' ' * 8 + 'except NameError as e:\n'
                block_out += ' ' * 12 + 'self.skipTest(e.args[0])\n\n'
    
    if block_out:
        out_content += f"\n\nclass {re.sub(r'[^a-zA-Z0-9]', '', subproblem[0]).capitalize()}(unittest.TestCase):\n"
        out_content += block_out

file_name_to_write = file_name[:-3] + '_test.py'
print('Writing assertions to ' + file_name_to_write + '...')
f = open(file_name_to_write, 'w+')
f.write(out_content.strip())
f.write("""


if __name__ == '__main__':
    unittest.main(verbosity=2)
""")
f.close()
print('File wrote to ' + os.path.join(os.getcwd(), file_name_to_write))
