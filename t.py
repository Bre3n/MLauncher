from winotify import Notification, audio
toast = Notification(
    app_id="Mlauncher",
    title="Notification",
    duration="short",

)
toast.show()