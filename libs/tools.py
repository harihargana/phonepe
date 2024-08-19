import json

def load_api_cfg(f):
  try:
    cfg_file=open(f)
  except:
    raise Exception(f'''File {f} is missing in this program's folder.''')
  try:
    cfg = json.load(cfg_file)
  except:
    raise Exception(f'Ensure that {f} is in JSON format.')
  try:
    if 'api' not in cfg:
      raise Exception(f'''{f} is missing 'api' config.''')
    api_cfg= cfg['api']
    if 'service_name' not in api_cfg:
      raise Exception(f''''service_name' is missing in {f}''') 
    if 'key' not in api_cfg:
      raise Exception(f''''key' is missing in {f}''') 
    if 'version' not in api_cfg:
      raise Exception(f''''version' is missing in {f}''') 
    return api_cfg
  except Exception as e:
    print(e)

def load_db_cfg(f):
  try:
    cfg_file=open(f)
  except:
    raise Exception(f'''File {f} is missing in this program's folder.''')
  try:
    cfg = json.load(cfg_file)
  except:
    raise Exception(f'Ensure that {f} is in JSON format.')
  try:
   if 'db' not in cfg:
     raise Exception(f'''{f} is missing 'db' config.''')
   db_cfg= cfg['db']
   if 'project_id' not in db_cfg:
     raise Exception(f''''project_id' is missing in {f}''') 
   if 'region' not in db_cfg:
     raise Exception(f''''region' is missing in {f}''') 
   if 'instance_name' not in db_cfg:
     raise Exception(f''''instance_name' is missing in {f}''') 
   if 'user' not in db_cfg:
     raise Exception(f''''user' is missing in {f}''') 
   if 'passwd' not in db_cfg:
     raise Exception(f''''passwd' is missing in {f}''') 
   if 'name' not in db_cfg:
     raise Exception(f''''name' is missing in {f}''')
   return db_cfg
  except Exception as e:
    print(e)
