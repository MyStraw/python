while True:
  s = input('뭐라도 쳐봐 : ')
  if s == 'quit' : 
    break
  if len(s) <3:
    print('넘 짧잖아')
    continue
  print('충분히 길게 쳤구만')