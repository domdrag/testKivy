from enum import Enum

class AdminCollectPhase(Enum):
    DROPBOX_SYNCHRONIZATION = 0
    SEARCH_LINKS = 1
    CONFIGURE_DAYS = 2
    EXTRACT_RULES_BY_DRIVER = 3
    HANDLE_MISSING_SERVICES = 4
    CHECK_UPDATE_NEEDED = 5
    DELETE_NECESSARY_DATA = 6
    EXTRACT_RULES = 7
    WRITE_DECRYPTED_SERVICES = 8
    WRITE_DECRYPTED_SHIFTS = 9
    SET_LAST_RECORD = 10
    UPLOAD_DATA_TO_DROPBOX = 11
    UPDATE_BACKUP_DIRECTORY = 12
    END = 13
