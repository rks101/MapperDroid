

normal_permissions = [
'android.permission.ACCESS_NOTIFICATION_POLICY',
'android.permission.BLUETOOTH',
'android.permission.BLUETOOTH_ADMIN',
'android.permission.BROADCAST_STICKY',
'android.permission.CHANGE_NETWORK_STATE',
'android.permission.CHANGE_WIFI_MULTICAST_STATE',
'android.permission.CHANGE_WIFI_STATE',
'android.permission.FLASHLIGHT',
'android.permission.FOREGROUND_SERVICE',
'android.permission.GET_PACKAGE_SIZE',
'android.permission.READ_APP_BADGE',
'android.permission.READ_SYNC_SETTINGS',
'android.permission.READ_SYNC_STATS',
'android.permission.RECEIVE_BOOT_COMPLETED',
'android.permission.SET_WALLPAPER',
'android.permission.SET_WALLPAPER_HINTS',
'android.permission.USE_BIOMETRIC',
'android.permission.VIBRATE',
'android.permission.WAKE_LOCK',
'android.permission.WRITE_SYNC_SETTINGS',
'com.android.alarm.permission.SET_ALARM',
'com.android.launcher.permission.INSTALL_SHORTCUT',
]

dangerous_permissions = [
'android.permission.ACCEPT_HANDOVER',
'android.permission.ACCESS_BACKGROUND_LOCATION',
'android.permission.ACCESS_COARSE_LOCATION',
'android.permission.ACCESS_FINE_LOCATION',
'android.permission.ADD_VOICEMAIL',
'android.permission.ANSWER_PHONE_CALLS',
'android.permission.BODY_SENSORS',
'android.permission.CALL_PHONE',
'android.permission.CAMERA',
'android.permission.GET_ACCOUNTS',
'android.permission.PROCESS_OUTGOING_CALLS',
'android.permission.READ_CALENDAR',
'android.permission.READ_CALL_LOG',
'android.permission.READ_CONTACTS',
'android.permission.READ_PHONE_NUMBERS',
'android.permission.READ_PHONE_STATE',
'android.permission.READ_SMS',
'android.permission.RECEIVE_MMS',
'android.permission.RECEIVE_SMS',
'android.permission.RECEIVE_WAP_PUSH',
'android.permission.RECORD_AUDIO',
'android.permission.SEND_SMS',
'android.permission.USE_SIP',
'android.permission.WRITE_CALENDAR',
'android.permission.WRITE_CALL_LOG',
'android.permission.WRITE_CONTACTS',
'android.permission.WRITE_EXTERNAL_STORAGE'
]

signature_permissions = [
'android.permission.BIND_ACCESSIBILITY_SERVICE',
'android.permission.CLEAR_APP_CACHE',
'android.permission.REQUEST_INSTALL_PACKAGES',
'android.permission.WRITE_SETTINGS'
]

deprecated_permissions = [
'android.permission.AUTHENTICATE_ACCOUNTS',
'android.permission.CLEAR_APP_USER_DATA',
'android.permission.GET_TASKS',
'android.permission.MANAGE_ACCOUNTS',
'android.permission.READ_PROFILE',
'android.permission.PERSISTENT_ACTIVITY',
'android.permission.USE_CREDENTIALS',
'android.permission.USE_FINGERPRINT',
'com.android.launcher.permission.UNINSTALL_SHORTCUT',
]

unknown_permissions = [
'com.amazon.device.messaging.permission.RECEIVE',
'com.anddoes.launcher.permission.UPDATE_COUNT',
'com.facebook.appmanager.UNPROTECTED_API_ACCESS',
'com.facebook.katana.permission.C2D_MESSAGE',
'com.facebook.katana.permission.CROSS_PROCESS_BROADCAST_MANAGER',
'com.facebook.katana.permission.RECEIVE_ADM_MESSAGE',
'com.facebook.katana.provider.ACCESS',
'com.facebook.mlite.provider.ACCESS',
'com.facebook.orca.provider.ACCESS',
'com.facebook.pages.app.provider.ACCESS',
'com.facebook.permission.prod.FB_APP_COMMUNICATION',
'com.facebook.receiver.permission.ACCESS',
'com.facebook.lite.permission.C2D_MESSAGE',
'com.facebook.wakizashi.provider.ACCESS',
'com.google.android.c2dm.permission.RECEIVE',
'com.google.android.gms.permission.ACTIVITY_RECOGNITION',
'com.google.android.providers.gsf.permission.READ_GSERVICES',
'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
'com.instagram.android.permission.C2D_MESSAGE',
'com.instagram.android..permission.C2D_MESSAGE',
'com.instagram.android..permission.RECEIVE_ADM_MESSAGE',
'com.instagram.direct.permission.DIRECT_APP_THREAD_STORE_SERVICE',
'com.instagram.direct.permission.PROTECTED_DEEPLINKING',
'com.linkedin.android.permission.C2D_MESSAGE',
'com.nokia.pushnotifications.permission.RECEIVE',
'com.snapchat.android.permission.UPDATE_STICKER_INDEX',
]

third_party_permissions = [
'com.htc.launcher.permission.READ_SETTINGS',
'com.htc.launcher.permission.UPDATE_SHORTCUT',
'com.huawei.android.launcher.permission.CHANGE_BADGE',
'com.huawei.android.launcher.permission.WRITE_SETTINGS',
'com.huawei.android.launcher.permission.READ_SETTINGS',
'com.majeur.launcher.permission.UPDATE_BADGE',
'com.oppo.launcher.permission.READ_SETTINGS',
'com.oppo.launcher.permission.WRITE_SETTINGS',
'com.sec.android.provider.badge.permission.READ',
'com.sec.android.provider.badge.permission.WRITE',
'com.sonyericsson.home.permission.BROADCAST_BADGE',
'com.sonymobile.home.permission.PROVIDER_INSERT_BADGE',
'me.everything.badger.permission.BADGE_COUNT_WRITE',
'me.everything.badger.permission.BADGE_COUNT_READ',
]

excl_permissions = normal_permissions + signature_permissions + deprecated_permissions + unknown_permissions + third_party_permissions

#print(excl_permissions)

