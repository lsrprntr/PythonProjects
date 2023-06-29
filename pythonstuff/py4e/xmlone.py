import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="init">
    +1 7343034456
    </phone>
    <email hide="yes"/>
</person>
'''
other = '''
<stuff>
    <users>
        <user x="2">
            <id>002</id>
            <name>Chucky</name>
        </user>
        </users>
</stuff>
'''

otherr = ET.fromstring(other)
lst=otherr.findall('users/user')
print(lst)

tree = ET.fromstring(data)
print(tree.find('name').text)
