# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]


def add_object(o, depth):       # 게임 월드에 객체 추가
    objects[depth].append(o)


def add_objects(ol, depth):     # 게임 월드에 객체 '들' 추가
    objects[depth] += ol


def remove_object(o):           # 게임 월드에서 객체 제거
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')



def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects:
        del o
    for layer in objects:
        layer.clear()

