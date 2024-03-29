from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__= (None, None, False, None)

def test_func():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

def test_asdict():
    t = Task('testing', 'Chau', True, 1)
    t_2 = t._asdict()
    expected = {'summary': 'testing', 'owner': 'Trang', 'done': True, 'id': 1}
    assert t_2 == expected