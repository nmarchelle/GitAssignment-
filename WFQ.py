from collections import deque


# Function to parse input packet stream and build queues
def build_queues(input_stream):
    premium_queue = deque()
    standard_queue = deque()
    economy_queue = deque()

    for packet in input_stream:
        priority = packet[0]
        if priority == 'P':
            premium_queue.append(packet)
        elif priority == 'S':
            standard_queue.append(packet)
        elif priority == 'E':
            economy_queue.append(packet)

    return premium_queue, standard_queue, economy_queue


# Function to apply WFQ and print output
def apply_wfq(premium_q, standard_q, economy_q):
    while premium_q or standard_q or economy_q:
        # Print 3 Priority packets until Priority queue is empty
        for _ in range(3):
            if premium_q:
                print("Priority Queue:", premium_q.popleft())
            else:
                break

        # Print 2 Standard packets until Standard queue is empty
        for _ in range(2):
            if standard_q:
                print("Standard Queue:", standard_q.popleft())
            else:
                break

        # Print 1 Economy packet until Economy queue is empty
        if economy_q:
            print("Economy Queue:", economy_q.popleft())


# Input Packet Stream
input_packets = [
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee", "E Vicky",
    "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete", "P Dee", "S Bill",
    "S Chase", "E Price", "P Dee", "E Sue"
]

# Build queues
premium, standard, economy = build_queues(input_packets)

# Apply WFQ and print output
apply_wfq(premium, standard, economy)
