def yield_infinite_abc():
    yield 'A'
    print('hello')
    yield 'B'
    print('world')



for v in yield_infinite_abc():
  print('v', v)