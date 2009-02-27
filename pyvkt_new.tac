
from twisted.application import service

from twisted.words.protocols.jabber import component
import ConfigParser
import pyvkt_new
config = ConfigParser.ConfigParser()
config.read("pyvk-t_new.cfg")

#import component_example

application = service.Application("pyvk-t")

# set up Jabber Component
srvAddr="tcp:%s:%s"%(config.get("general","server"),config.getint("general","port"))
sm = component.buildServiceManager(
    config.get("general","transport_jid"), 
    config.get("general","secret"),
    (srvAddr)
)


# Turn on verbose mode
pyvkt_new.LogService().setServiceParent(sm)

# set up our example Service
s = pyvkt_new.pyvk_t()
s.setServiceParent(sm)

sm.setServiceParent(application)

