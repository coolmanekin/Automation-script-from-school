import win32evtlog
EVENT_ID_LOGON = 4624
hand = win32evtlog.OpenEventLog(None, "Security")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
query = "EventID={}".format(EVENT_ID_LOGON)
user_net_set = set()
events = win32evtlog.ReadEventLog(hand, flags, 0)

while events:
    for event in events:
        if event.EventID == EVENT_ID_LOGON:
            username = event.StringInserts[5]
            source_network_address = event.StringInserts[18]
            if username and source_network_address:
                user_net_pair = (username, source_network_address)
                if user_net_pair not in user_net_set:
                    print("Username: {}, Source Network Address: {}".format(username, source_network_address))
                    user_net_set.add(user_net_pair)
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    
win32evtlog.CloseEventLog(hand)
