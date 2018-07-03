
def read_file(filename):
	lines =[]
	with open(filename,'r') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'tina':
			person = 'tina'
			continue
		elif line == 'connie':
			person = 'connie'
			continue
		if person: #如果person有value 才執行下行
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open (filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert (lines)
	write_file('output.txt', lines)

main()

