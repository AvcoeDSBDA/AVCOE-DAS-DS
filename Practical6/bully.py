class BullyAlgorithm:

    def __init__(self, nodeId, nodes):
        self.nodeId = nodeId
        self.nodes = nodes

    def startElection(self):

        highestNodeId = self.nodeId

        # Send election messages
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} sends Election message to Node {i}")

        # Wait for OK messages
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} waiting for OK message from Node {i}")

        # Receive OK messages
        for i in range(self.nodeId + 1, len(self.nodes) + 1):

            if i in self.nodes:
                print(f"Node {self.nodeId} received OK message from Node {i}")
                highestNodeId = i

        # Coordinator selection
        if highestNodeId != self.nodeId:

            print(f"Node {highestNodeId} becomes the new coordinator")

        else:

            print(f"Node {self.nodeId} is the new coordinator")


# List of nodes
nodes = [1, 2, 3, 4, 5]

# Create object
bully = BullyAlgorithm(3, nodes)

# Start election
bully.startElection()