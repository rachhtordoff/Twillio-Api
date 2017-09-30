import os

APP_NAME = os.environ['APP_NAME']

# text server
TEXT_ACCOUNT = 'AC947b1fb75af13bc22c5ed4f27c69da74'
TEXT_TOKEN = '7bf0525b7c22784b9c80b8b8f8c4d36d'


FLASK_LOG_LEVEL = os.environ['FLASK_LOG_LEVEL']

LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            '()': 'text_message_api.extensions.JsonFormatter'
        },
        'audit': {
            '()': 'text_message_api.extensions.JsonAuditFormatter'
        }
    },
    'filters': {
        'contextual': {
            '()': 'text_message_api.extensions.ContextualFilter'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        },
        'audit_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'audit',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'application': {
            'handlers': ['console'],
            'level': FLASK_LOG_LEVEL
        },
        'audit': {
            'handlers': ['audit_console'],
            'level': 'INFO'
        }
    }
}
