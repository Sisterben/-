#search and replace
s = """Simple is better than complex.Complex is better than complicated."""
s.lower().count('mp')
s.lower().count('mp',10)
s.lower().count('mp',10, 30)
pass
print('Example of str.find():')
s = """Simple is better than complex.Complex is better than complicated."""
s.lower().find('mpl')
s.lower().find('mpl',10)
s.lower().find('mpl',10, 20)
print()
pass
print('Example of str.rfind():')
s = """Simple is better than complex.Complex is better than complicated."""
s.lower().rfind('mpl')
s.lower().rfind('mpl',10)
s.lower().rfind('mpl',10, 20)
print()
pass
s = """Simple is better than complex.Complex is better than complicated."""
print("s.lower().startswith('S'):",  s.lower().startswith('s'))
print("s.lower().startswith('b'):",  s.lower().startswith('b'))
print("s.lower().startswith('e', 11, 20):",  s.lower().startswith('e', 11, 20))
pass
s = """Simple is better than complex.Complex is better than complicated."""
print("s.lower().endswith('.'):",  s.lower().endswith('.'))
print("s.lower().endswith('.', 10):",  s.lower().endswith('.', 10))
print("s.lower().endswith('.', 10, 20):",  s.lower().endswith('.', 10 ,20))
pass
s = """Simple is better than complex.Complex is better than complicated."""
print('mpl' in s)
#str.replace()
#str.expandtabs(tabsize=8)专门用于替换制表符
pass
#去除子字符
#str.strip([chars])去除字符串首尾的***
#str.lstrip or str.rstrip
#拆分字符串
#str.partition,str.splitlines,str.split