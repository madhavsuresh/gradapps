import web
from time import strptime, strftime


urls = ('/(\w*)', 'grad', '/todo/(\w*)',
        'addTodo', '/addprof/(\w*)', 'addProf')
render = web.template.render('templates/')
app = web.application(urls, globals())


class addTodo:
    def POST(self, school):
        i = web.input()
        with open('./todo', 'a') as tdo:
                tdo.write(i['todo1'] + '\n')
        raise web.seeother('/' + school)


class addProf:
    def POST(self, school):
        i = web.input()
        with open('./' + school, 'a') as profz:
            print i['profz']
            profz.write(i['profz'] + '\n')
        raise web.seeother('/' + school)


class grad:
    def GET(self, school):
        school = school.lower()
        gopher = {}
        school_list = []
        f = open('./dbz')
        keys = f.readline().strip().split(';')[1:]
        for line in f:
            info = line.split(';')
            gopher[info[0]] = zip(keys, info[1:])
            deadline = strptime(info[2], '%m/%d/%y %I%p')
            school_list.append((info[0], deadline))
        school_list.sort(key=lambda r: r[1])
        out_school = map(lambda l: (l[0],
                         strftime('%b. %d %I%p', l[1])), school_list)
        f.close()
        f = open('./' + school)
        prof_list = []
        for line in f:
            prof_list.append(tuple(line.split(';')))
        f.close()
        f = open('./todo')
        tdlist = []
        for line in f:
            tdlist.append(line)
        f.close()
        return render.resp(school, gopher[school], 
                           out_school, tdlist, prof_list)


if __name__ == '__main__':
    app.run()
