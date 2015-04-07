#!/usr/bin/env python
from operator import itemgetter

import mcstatus

from tornado import ioloop
from tornado import web


class StatusHandler(web.RequestHandler):
    def get(self):
        server = mcstatus.MinecraftServer.lookup('192.168.2.4:25565')
        status = server.status()
        players = [p.__dict__ for p in status.players.sample or []]
        self.finish({'players_max': status.players.max,
                     'players_online': status.players.online,
                     'players': sorted(players, key=itemgetter('name')),
                     'version': status.version.name,
                     'port': 25565,
                     'hostname': 'minecraft.poisonpenllc.com',
                     'online': True,
                     'desc': status.description})

application = web.Application([
    (r"/", StatusHandler),
    (r"/status", StatusHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()
