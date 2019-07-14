import dlbase64


def Analyze(s):
	config = {
		'server':"khabarovsk-2.abyss.moe",
		'server_ipv6': "::",
		'server_port': 30094,
		'local_address': "127.0.0.1",
		'local_port': 1080,
		'password': "D18Art",
		'method': "chacha20-ietf",
		'protocol': "auth_chain_a",
		'protocol_param': "",
		'obfs': "plain",
		'obfs_param': "",
		'speed_limit_per_con': 0,
		'speed_limit_per_user': 0,
		'additional_ports' : "{}", 
		'additional_ports_only' : "false", 
		'timeout': 120,
		'udp_timeout': 60,
		'dns_ipv6': "false",
		'connect_verbose_info': 0,
		'redirect': "",
		'fast_open': "false"
	}

	  
	spilted = s.split(':')  
	pass_param = spilted[5]
	pass_param_spilted = pass_param.split('/?')
	passwd = dlbase64.debase64_2(pass_param_spilted[0])
	passwd = passwd.decode('utf-8')

	try:
		obfs_param = re.search(r'obfsparam=([^&]+)',pass_param_spilted[1]).group[1]
	except:
		obfs_param=""
	try:
		protocol_param = re.search(r'protoparam=([^&]+)', pass_param_spilted[1])
		protocol_param = decode(protocol_param)
	except:
		protocol_param = ''
	try:
		remarks = re.search(r'remarks=([^&]+)', pass_param_spilted[1]).group(1)
		remarks = dlbase64.debase64_2(remarks)
		remarks = remarks.decode('utf-8')
	except:
		remarks = ''
	try:
		group = re.search(r'group=([^&]+)', pass_param_spilted[1]).group(1)
		group = decode(group)
	except:
		group = ''


	config['server'] = spilted[0]
	config['server_port'] = int(spilted[1])
	config['password'] = passwd
	config['method'] = spilted[3]
	config['protocol'] = spilted[2]
	config['obfs'] = spilted[4]
	config['protocol_param'] = protocol_param
	config['obfs_param'] = obfs_param

	return [config,group,remarks]
