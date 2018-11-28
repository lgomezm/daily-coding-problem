class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
	if node == None:
		return ''
	return '['+node.val+','+serialize(node.left)+','+serialize(node.right)+']'

def deserialize(text):
	return innerDeserialize(text, 1)

def innerDeserialize(text, curLevel):
	if text == '':
		return None
	elif not text.startswith('[') and not text.endswith(']'):
		print('Malformed text')
		return None
	level = curLevel-1
	parts = []
	strPart = ''
	for i in range(len(text)):
		if text[i] == '[':
			level = level+1
			if curLevel != level:
				strPart = strPart+text[i]
		elif text[i] == ',':
			if curLevel == level:
				parts.append(strPart)
				strPart = ''
			else:
				strPart = strPart+text[i]
		elif text[i] == ']':
			if level == curLevel:
				parts.append(strPart)
			else:
				strPart = strPart+text[i]
			level = level-1
		else:
			strPart = strPart+text[i]
	if len(parts) != 3:
		print("Invalid tree")
		return None
	return Node(parts[0], innerDeserialize(parts[1], curLevel+1), innerDeserialize(parts[2], curLevel+1))

node = Node('root', Node('left', Node('left.left')), Node('right'))
text = serialize(node)
print(text)
print(serialize(deserialize(text)))