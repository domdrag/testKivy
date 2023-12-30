from src.data.manager.notifications_manager import getNotifications
from src.share.trace import TRACE

def getNotificationImages(notificationName):
    NOTIFICATIONS = getNotifications()
    imagesFileNamePattern = NOTIFICATIONS[notificationName]['IMAGES_FILE_NAME_PATTERN']
    numOfPages = NOTIFICATIONS[notificationName]['NUM_OF_PAGES']
    imagesPathPattern = 'data/central_data/notifications_files/' + imagesFileNamePattern
    imagesPathList = [imagesPathPattern + str(pageNum) + '.png'
                      for pageNum in range(1, numOfPages + 1)]
    TRACE('Found notification images: ' + str(imagesPathList))

    return imagesPathList