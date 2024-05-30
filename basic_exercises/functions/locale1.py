def extract_language(locale):
  return locale[0:2]
  
def extract_region(locale):
  locale = locale.split('_')
  region = locale[1].split('.')[0]
  return(region)

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR