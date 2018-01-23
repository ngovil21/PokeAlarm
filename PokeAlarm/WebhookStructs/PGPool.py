import logging
import traceback



log = logging.getLogger('WebhookStructs')


class PGPool:

    def __init__(self):
        raise NotImplementedError(
            "This is a static class not meant to be initiated")

    @staticmethod
    def make_object(data):
        try:
            kind = data.get('type')
            if kind == 'pgpool':
                return PGPool.pgpool(data.get('message'))
            else:
                log.error("Invalid type specified ({}). ".format(kind)
                          + "Are you using the correct map type?")
        except Exception as e:
            log.error("Encountered error while processing webhook "
                      + "({}: {})".format(type(e).__name__, e))
            log.debug("Stack trace: \n {}".format(traceback.format_exc()))
        return None

    @staticmethod
    def pgpool(data):

        pool = {
            'id': '{}-{:32}-{:32}'.format(data.get('subtype'), data.get('system_id'), data.get('username')),
            'subtype': data.get('subtype'),
            'system_id': data.get('system_id'),
            'username': data.get('username'),
            'auth_service': data.get('auth_service'),
            'latitude': float(data.get('latitude')),
            'longitude': float(data.get('longitude')),
            'level': int(data.get('level')),
            'xp': int(data.get('xp')),
            'encounters': int(data.get('encounters')),
            'last_modified': data.get('last_modified'),
            'warn': data.get('warn'),
            'shadowbanned': data.get('shadowbanned'),
            'banned': data.get('banned'),
            'ban_flag': data.get('ban_flag'),
            'captcha': data.get('captcha'),
            'rareless_scans': int(data.get('rareless_scans')),
            'message': data.get('message'),
            'good_low_level': int(data.get('good_low_level')),
            'good_high_level': int(data.get('good_high_level')),
            'good_total': int(data.get('good_total'))
        }

        return pool


def get_bool_str(i):
    if i is None or "null":
        return "Unknown"
    if i:
        return "True"
    else:
        return "False"
