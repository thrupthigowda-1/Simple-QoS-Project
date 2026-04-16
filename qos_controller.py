from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed
    src = str(packet.src)
    dst = str(packet.dst)

    msg = of.ofp_flow_mod()

    # High priority flow: h1 -> h2
    if src == "00:00:00:00:00:01" and dst == "00:00:00:00:00:02":
        log.info("HIGH PRIORITY: h1 -> h2")
        msg.priority = 100
        msg.actions.append(of.ofp_action_output(port=2))

    # Low priority / restricted flow: h1 -> h3
    elif src == "00:00:00:00:00:01" and dst == "00:00:00:00:00:03":
        log.info("LOW PRIORITY: h1 -> h3")
        msg.actions.append(of.ofp_action_output(port=3))

    # Default forwarding behavior
    else:
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("QoS Priority Controller Started")
