from bs4 import BeautifulSoup

hop_ups = []
parts = []

with open('1.html', 'r') as f:
	soup = BeautifulSoup(f, 'html.parser')
	o = soup.findAll("div", { "class" : "t s6_1" })

	for line in o:
		line = str(line)
		line = line.split('>')[1].split('<')[0]
		if line[0].isdigit():
			line = line.split(" ")[0]
			hop_ups.append(line)


