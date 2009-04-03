# /////////////// This is a change on the new branch ///////////////
import re

string = u'ticket#123'
string = u'ticket#123[hold]'
string = u'ticket#123[assign:justin]'

# ////////////////////////////////////////////////////

regex = r'ticket#(?P<ticket_id>[\d]+)(?:\[(?P<ticket_action>[\w]+)(?::(?P<ticket_assign_to>[\w]+)\])?)?'
regex = re.compile(regex)
matches = regex.finditer(string)
spans = []
regex.findall(string)

for match in matches:
	start = match.start()
	end = match.end()
	spans.append([start, end])

if len(spans) != 0:
	for key in range(0, len(spans)):
		span = spans.pop()
		ticket = string[span[0]:span[1]]
		ticket_id = regex.findall(ticket)
		print "%s" % (ticket_id)