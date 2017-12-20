import tornado.web

from controller import *

class Application(tornado.web.Application):
    handlers = [
            (r"/login",LoginHandler),
            (r"/reg",RegHandler),

            (r"/user",UserHandler),
            (r"/user/reset",ResetUserHandler),

            # (r"/course/(?P<profile_name>\S*)",CourseHandler),
            (r"/course",CourseHandler),
            (r"/course/task",CourseTaskHandler),
            (r"/course/task/status",CrouseTaskStatus),
            (r"/course/user",CrouseUser),

            (r"/task",TaskHandler),
            (r"/task/unfinished",TaskUnfinishedHndler),
            (r"/course/signin",SignInHandler),
            
        ]