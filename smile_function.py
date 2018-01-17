def monkey_trouble(a_smile, b_smile):
  if a_smile & b_smile:
    return True
  elif ((a_smile == False) & (b_smile ==  False)):
    return True
  else:
    return False


def sum_double(a, b):
    if a == b:
        return(a*4)
    else:
        return(a+b)

def diff21(n):
    if n > 21:
        return(2*(n-21))
    else:
        return(abs(21-n))


def parrot_trouble(talking, hour):
  if (talking and (int(hour) < 7 or int(hour) > 20)):
    return True
  else:
    return False

def makes10(a, b):
    # Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
    if (int(a) == 10 or int(b) == 10 or int(a) + int(b) == 10):
        return True
    else:
        return False


def not_string(str):
  try:
      if str.lower().index('not') == 0:
        return str
      else:
        return('not '+str)
  except:
        return('not '+str)


def front_back(str):
  if len(str) == 1:
    return str
  else:
    d=str[-1]+str[1:-1]+str[0]
    return d


def front3(str): 
#"""Given a string, we'll say that the front is the first 3 chars of the string.
#If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. """
    if len(str) <= 3:
      d=str*3
    else:
      d=str[:3]*3
    return d

def string_times(str, n):
  #Given a string and a non-negative int n, return a larger string that is n copies of the original string.
  return(str*n)

def string_bits(str):
  #Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
  k=""
  j=0
  while j <= len(str):
      k=k+str[j]
      if len(str) > 2:
          j=j+2
      else:
          break
  return k
   
  
def string_splosion(str):
  #Given a non-empty string like "Code" return a string like "CCoCodCode".
  final=''
  for i in range(len(str)+1):
    new=str[0:i]
    final=final + new 
  return final
    
def last2(str):
  #hixxxhi" yields 1 (we won't count the end substring)
  last2=str[-2:]
  num=str[:-2].count(last2)
  return(num)

def array_count9(nums):
  return nums.count(9)
  
def array_front9(nums):
  if nums[:3].count(9) > 0:
    return True
  else:
    return False

def array123(nums):
  i=0
  while i <= len(nums)-1:
    if nums[i:i+3] == [1,2,3]:
      return True
    i += 1
  return False

    
print(array123([1,2,4,5,6,7,7,8,9,10]))
  
