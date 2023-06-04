import json
class Model:
    def save(self, file_path):
        a1=list(filter (lambda x: not x.startswith ('_'), dir (C1)))
        with open (file_path, 'w') as f:
            json.dump(a1, f)


class C1(Model):
 title = '1'
 text = '2'
 author = '3'
c = C1()
c.save('data.json')
