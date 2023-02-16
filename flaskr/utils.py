def float_converter(value):
   if (',' in value):
      temp = value.partition(',')
      value = temp[0] + "." + temp[2]

   return float(value)
