
CM_TEST = '''
			SELECT * 
			FROM spl_users.device_users
		'''

CM_GET_EMAIL = '''
			SELECT email, device_name
			FROM spl_users.device_users
			WHERE imei=%s
		'''

CM_INSERT_DEVICE = '''
                INSERT INTO spl_users.device_users (imei, device_name, email, password, password_pattern, password_face, create_time, update_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                device_name = VALUES(device_name),email = VALUES(email),password = VALUES(password),password_pattern = VALUES(password_pattern),password_face = VALUES(password_face)
'''

CM_LOG_ACCESS = u'''
                INSERT INTO spl_users.log_access_app (imei, device_name, app_name, access_time, gps, network_ip, package, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
'''

CM_EMAILS = '''
			SELECT email
			FROM spl_users.device_users
		'''

CM_GET_LOG = '''
			SELECT * FROM spl_users.log_access_app where email=%s and access_time > %s;
		'''

CM_GET_YOUR_LOG = '''
			SELECT * FROM spl_users.log_access_app where email=%s and imei=%s and access_time > %s;
		'''

CM_CHECK_ACCESS_APP = '''
			SELECT * FROM spl_users.forbid_access_app where imei=%s and email=%s and package=%s;
'''

CM_ADD_APP_TO_FORBID = '''
			 INSERT INTO spl_users.forbid_access_app(imei, email, package)
             VALUES (%s, %s, %s)
             ON DUPLICATE KEY UPDATE
             imei=VALUES(imei), email=VALUES(email),package=VALUES(package)
'''

CM_FORGET_PASSWORD = '''
		SELECT password, device_name
		FROM spl_users.device_users
		WHERE imei=%s and email=%s
'''

CM_UPDATE_PASSWORD_DEVICE = '''
					UPDATE spl_users.device_users
					SET password=%s, update_time=%s
					WHERE imei=%s
'''

CM_UPDATE_PASSWORD_PATTERN_DEVICE = '''
					UPDATE spl_users.device_users
					SET password_pattern=%s, update_time=%s
					WHERE imei=%s
'''

CM_UPDATE_PASSWORD_FACE_DEVICE = '''
					UPDATE spl_users.device_users
					SET password_face=%s, update_time=%s
					WHERE imei=%s
'''