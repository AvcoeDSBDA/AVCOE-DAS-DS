class TokenRing:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = [None] * num_nodes

    def set_node(self, node_id, data):
        self.nodes[node_id] = data

    def run(self):

        token = True
        current_node = 0

        while True:

            # Check if token received
            if token:

                print(f"Node {current_node}: Received token")

                # Process current node data
                print(f"Node {current_node}: Processing data '{self.nodes[current_node]}'")

                # Pass token to next node
                next_node = (current_node + 1) % self.num_nodes

                # Stop after full rotation
                if next_node == 0:
                    print("Token completed full rotation")
                    break

                current_node = next_node


# Create token ring with 4 nodes
token_ring = TokenRing(4)

# Set node data
token_ring.set_node(0, "Data 1")
token_ring.set_node(1, "Data 2")
token_ring.set_node(2, "Data 3")
token_ring.set_node(3, "Data 4")

# Run algorithm
token_ring.run()