
CM_TEST = '''
			SELECT * 
			FROM spl_users.device_users
		'''

CM_GET_EMAIL = '''
			SELECT email
			FROM spl_users.device_users
			WHERE imei=%s
		'''

CM_INSERT_DEVICE = '''
                INSERT INTO spl_users.device_users (imei, device_name, email, password, password_pattern, password_face, create_time, update_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
  				device_name = VALUES(device_name),
  				email = VALUES(email)
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